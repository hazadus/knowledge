References
Configure SSH
## References

> [!info] Pro Django - Tutorial 9 - CI/CD  
> Source Code: https://github.  
> [https://www.youtube.com/watch?v=zCz6xEFqOXE](https://www.youtube.com/watch?v=zCz6xEFqOXE)  
## Configure SSH
```Bash
# Locallly:
ssh-keygen -t rsa -b 4096 -f ~/.ssh/github
# NB: do not enter passphrase! Just hit enter!
```
On GitHub, go to “Settings → Secrets and Variables → Actions”, press “New repository secret” button.
Name variable `SSH_PRIVATE_KEY`
Cat private key _(long)_ with `cat /Users/hazadus/.ssh/github` or `cat /Users/hazadus/.ssh/github | pbcopy` and paste into form “Secret” field.
SSH into the server.
Cat public key _(short)_, copy into clipboard using `cat /Users/hazadus/.ssh/github.pub | pbcopy`
**Via SSH** open `nano ~/.ssh/authorized_keys`
Paste new key below existing one.
On GitHub, create new secret `SSH_HOST` with server IP and `SSH_USER` with username.
```YAML
name: Continuous Integration
on:
  push:
    branches:
      - main
concurrency:
  group: main
  cancel-in-progress: true
jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    steps:
      - name: Configure SSH
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
          SSH_HOST: ${{ secrets.SSH_HOST }}
          SSH_USER: ${{ secrets.SSH_USER }}
        run: |
          mkdir -p ~/.ssh/
          echo "$SSH_PRIVATE_KEY" > ~/.ssh/github
          chmod 600 ~/.ssh/github
          cat >>~/.ssh/config <<END
          Host target
            HostName $SSH_HOST
            User $SSH_USER
            IdentityFile ~/.ssh/github
            LogLevel ERROR
            StrictHostKeyChecking no
          END
      - name: Run Deploy
        run: |
          ssh target "cd /usr/projects/django-rss-reader && docker compose down && git pull && docker compose up -d --build --force-recreate"
```