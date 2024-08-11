📂 [[Tooling]]

----
## Renewing Certificate
```Bash
# cd to project folder
cd /usr/projects/nuxt-content-portfolio/
# stop the app to free 80 port
docker compose down
# or
make down
# do the thing
certbot renew
```
![[attachments/Untitled 13.png|Untitled 13.png]]
```Bash
ls -al /etc/letsencrypt/archive/hazadus.ru/
# New files below with suffix "2":
```
![[attachments/Untitled 1 4.png|Untitled 1 4.png]]
Update `default.prod.conf` with new filenames:
![[attachments/Untitled 2 4.png|Untitled 2 4.png]]

----
📂 [[Tooling]]