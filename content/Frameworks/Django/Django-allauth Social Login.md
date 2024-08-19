Integrate Telegram With Your Django Site Using django-allauth

=============================================================

Issues

------

  

Let me start with the problems encountered, since you are possibly going to stumble upon the same things.

  

The first one is documentation. Like many large open source projects, django-allauth suffers from poor documentation. In the particular case of django-allauth and Telegram, all the specifics I could find at time of writing was this:

  

![](https://blog.konsente.com/img/posts/django-allauth-telegram.png)

  

To compound the problem, Telegram documentation was not a lot better. You were told what to do in great detail, but there was nothing that told you what errors you could encounter and how to remedy them.

  

That’s the original reason for this article: it wants to provide more detailed documentation of what to do and how for the combination Django/django-allauth/Telegram/python-telegram-bot.

  

In particular, it seems that our use case is still not dominant and that the main problems in the documentation come from a focus on different ways of doing things. So, if what you want is the same as what we want (authenticate and communicate using Telegram identities), then follow along.

  

Step-By-Step Process

--------------------

  

1\. Create Telegram Bots

------------------------

  

This part is a piece of cake. Just follow the instructions on [Telegram’s documentation site](https://core.telegram.org/bots/tutorial#obtain-your-bot-token). Basically, from the account you want to create the bot on (your account, not the bot’s account), you send the `/newbot` message to the @BotFather account. That will guide you through a process. At the end of it, you’ll get the most important piece of information: the bot **token**.

  

The bot token itself is composed of two parts, separated by a colon. The first part is your bot ID, a pure number. The second part is the secret (in Base64 encoding or something similar).

  

You should create _two_ bots. One to use for development, one for production. That’s because in the django-allauth implementation, django uses a callback, and as a result the bot needs to know where calls are coming from and where they are sent to.

  

Imagine that you want to implement Telegram bot functionality on `example.com`. Then you want the bot to only accept login requests coming from `example.com` and redirect them to `example.com` for confirmation. Since your development environment will not generally point to `example.com`, it’s better to have two bots, or you’ll have to change the domain every time you move from development to production.

  

As part of creating the bots, add an image using the `/setuserpic` command (to @BotFather) and the domain using `/setdomain`. The process is interactive and asks for the information needed.

  

Note that the only way we could get the domain to work in development was to set it to `http://0.0.0.0:8000/accounts/telegram/login/callback/`. Any other domain (e.g. using localhost, or 127.0.0.1, or any URL other than the one mentioned) failed to produce a full flow.

  

2\. Install django-allauth

--------------------------

  

Note: this presumes you are adding django-allauth to an existing Django project. If you do not have a Django project already, follow the tutorial to create one, or download an existing open source project. You are much better off starting with the project and familiarizing yourself with Django and _then_ add django-allauth functionality than trying to do all at once.

  

Go into your Django environment and add allauth by typing `pip install django-allauth`.

  

Note that if you use docker or other virtualization, you need to add django-allauth to your requirements.txt file.

  

3\. Configure django-allauth

----------------------------

  

The configuration of django-allauth consists, in our case, in the general configuration of the package and the specific configuration of the provider we want, Telegram.

  

The general configuration is described [here](https://docs.allauth.org/en/latest/installation/quickstart.html). It involves adding allauth specific settings to the general configuration file, settings.py, and adding the allauth URLs to the urls.py file for the project.

  

Follow these instructions closely. They are not too hard to implement, especially if you know your way around Django in general. Notice that in the general instructions, you are asked to add an incredibly long list of provider accounts. For our purposes, the only one that matters is `allauth.socialaccount.providers.telegram`. You can include other ones, but unless you also configure their parameters, it won’t do much good.

  

One thing mysteriously not mentioned in the above configuration quickstart is that you need to add the SITE\_ID parameter to the settings. It seems to matter little which ID you use, so maybe `SITE_ID=1` is a good start.

  

Due to our specific configuration, we also needed to add the line, `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` to our settings. That may be necessary or not for your configuration.

  

4\. Telegram-specific Settings

------------------------------

  

The configuration of the Telegram social app is very simple. All you need to do is add the section:

  

SOCIALACCOUNT_PROVIDERS = {

'telegram': {

'APP': {

'client_id': '<client_id>',

'secret': environ.get('DJANGO_SECRET_TELEGRAM', '<client_id>:<secret>'),

},

},

}

  

to your settings file. The client ID is the numeric part of the token you got from @BotFather, while the secret is the entire token (including ID and colon). Please notice that, while the client ID is not particularly sensitive, the secret very much is. As such, you should treat it with the same respect and reverence as any other secret in your settings. Here, it is set from the environment variable `DJANGO_SECRET_TELEGRAM`, which necessitates an `import environ` at the beginning of the settings file. The only reason there is a default set here is to highlight the syntax used. You should not add the production token to the settings file.

  

Also notice that if you created two bots, you should determine which one to use here, by changing the environment or by using `if` statements:

  

if DJANGO_PRODUCTION:

SOCIALACCOUNT_PROVIDERS = {

'telegram': {

'APP': {

'client_id': environ.get('DJANGO_UID_TELEGRAM', '<client_id_prod>'),

'secret': environ.get('DJANGO_SECRET_TELEGRAM', '<client_id_prod>:<secret_prod>'),

},

},

}

else:

SOCIALACCOUNT_PROVIDERS = {

'telegram': {

'APP': {

'client_id': environ.get('DJANGO_UID_TELEGRAM', '<client_id_dev>'),

'secret': environ.get('DJANGO_SECRET_TELEGRAM', '<client_id_dev>:<secret_dev>'),

},

},

}

  

Note that this presumes you defined a variable, `DJANGO_PRODUCTION`, that is set to `True` if the system is in production mode.

  

5\. Configure urls.py

---------------------

  

This one was already mentioned. You need to add the line `path('accounts/', include('allauth.urls')),` to the list of URL patterns in your urls.py file. Notice that each app generally has a urls.py file, and you are asked to put the line into the master urls.py for the project, not that of any dependent apps.

  

6\. Configure the Login Template

--------------------------------

  

You can style your login template however you want! All it needs to add is the line `{% load socialaccount %}` somewhere at the top, so that the template tags for social accounts are recognized, and then somewhere else the link for the telegram account in the form of `{% provider_login_url "telegram" %}`. This is a redirect, so a button with a link target or a plain anchor tag will work. (E.g. `<a href="{% provider_login_url "telegram" %}">Login with Telegram</a>`) As mentioned, you can style the login however you want.

  

Telegram itself provides a nifty widget that you can generate and copy to your template interactively. Some users reported that this is the only thing that worked for them. We, on the other hand, found that the widget doesn’t like interacting with Vue/Vuetify components and simply gets swallowed. Because we had no issue with the original Telegram link from allauth, we stuck with it.

  

7\. Sending Messages

--------------------

  

Once users have authenticated via django-allauth and Telegram, their user accounts will have a field, `socialaccount_set`. This _doesn’t_ set the social accounts, but is a _set_ of social accounts. That’s because django-allauth makes the assumption that a user could have a whole slew of different socials.

  

To send a message, you first have to install `python-telegram-bot`. Read the section above regarding django-allauth installation for details, in particular using `pip install` and adding python-telegram-bot to your requirements.txt.

  

How do you connect with a Telegram user? If you read the documentation on bots, it tells you that the users need to first have connected with your bot. That’s not the case here, since the users already granted permission to receiving messages as part of the signup process.

  

As a result, you can simply loop through the social accounts registered for a user and directly send a message. In practical terms, this looks like:

  

def send_via_telegram(user, message):

socials = user.socialaccount_set.all()

tg = list(filter(lambda s: s.provider == 'telegram', socials))

if tg.length > 0:

bot = telegram.Bot(settings.SOCIALACCOUNT_PROVIDERS['telegram']['APP']['secret'])

asyncio.run(bot.send_message(tg[0].uid, message))

  

It takes a short while to set up the bot object, so you may want to cache it somewhere. Also, don’t forget to `import telegram`.

  

Also, you should implement a way to receive messages from the user and forward them to someone that can interact with them.

----
📂 [[Django]] | Последнее изменение: 24.05.2024 13:34