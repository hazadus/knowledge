### Common commands

- `!$` - use argument of previous command, e.g. `cd !$`
- `!!` - run previous command, e.g. `sudo !!`
- `alias gerp=grep` - create alias for command
- `command_1; command_2; command_3` - run three commands sequentially
- `(command_1 &); (command_2 &)` - parallel run two commands
- `command_1 && command_2` - run command_2 if command_1 executed successfully.
- `cd -` - return to previous directory `$OLDPWD`
- `ps ax` - list all running processes. Here, a shows processes from all users and x shows processes that are not connected with the Terminal
- `ps ax | grep <name>` - show only lines with `name`
- `tail -f <logfile>` - read bottom of the file
- `ln -s /usr/projects/flask-demo/run_flask.sh run_flask` - soft link from _source_ to _target_
- `ln file.txt file-hardlink.txt` – hardlink from source to target
- `w` – who logged in
- `lsof` – list of open files
- `lsof -i :5000` – show process which uses port 5000

----
### Terminal key shortcuts

- `Ctrl+R <condition>` - search previous commands
- `Alt+.` - select argument of previous commands by pressing `.`
- `Ctrl+A` - cursor to the beginning of line
- `Ctrl+E` - cursor to the end of line
  
----

### System Info
_list system info stuff here!_
- `cat /etc/os-release` – show detailed OS info
- `uname -r` – kernel version
- `uname -a` – System Info
- `uptime` – show uptime
- `uptime -p` – pretty, just uptime
- `echo $SHELL` – shell process  
- `echo $0`
- `env` – list env vars
- `top` – show the list of processes ordered by what is consuming the most CPU and will refresh the order of the list every second to provide a current snapshot in time. (**Tip**: use `q` to quit `top` after you start it.)
### Disk usage
- `df -H` – disk usage info (drives)
- `du -a ~/projects/newspaper/ | sort -n -r | head -n 10` – folders disk usage sorted in descending order
- `ncdu` (`apt install ncdu`) – cool utility with text interface.
- `journalctl --disk-usage` – how much space used by logs in /var/log/journal/
- `sudo journalctl --vacuum-size=100M` – reduce logs size to 100M by deleting old stuff

---

### Download / upload Files

> [!info] Example syntax for Secure Copy (scp)  
> scp allows files to be copied to, from, or between different hosts.  
> [http://www.hypexr.org/linux_scp_help.php](http://www.hypexr.org/linux_scp_help.php)  
```Bash
# Copy the file "foobar.txt" from a remote host to the local host
$ scp your_username@remotehost.edu:foobar.txt /some/local/directory
# Copy the file "foobar.txt" from the local host to a remote host
$ scp foobar.txt your_username@remotehost.edu:/some/remote/directory
# Copy directory from local to remote
scp -r ~/Projects/js-mp3-player/ root@188.225.72.155:/usr/projects/
# Copy from remote to local
scp -r root@85.193.89.177:/root/projects/ ~/webbackup/
scp -r root@188.225.72.155:/usr/projects/SdclHessleAudio/mp3s/ ~/Downloads/mixes4web/mp3/
```
### Apt
```Bash
sudo apt update
sudo apt -y upgrade
```
### cron

> [!info] How To Use Cron to Automate Tasks on Ubuntu 18.04 | DigitalOcean  
> Cron is a time-based job scheduling daemon found in Unix-like operating systems, including Linux distributions.  
> [https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804)  
```Bash
# edit
crontab -e
# view
crontab -l
# Must be added under `root`:
20 * * * * docker exec newspaper-web-1 python manage.py random_image
0 22 * * * docker exec journal-web python manage.py create_report
```
### wget
```Bash
# https://adamj.eu/tech/2023/03/07/download-documentation-website-with-wget/
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/
wget --directory-prefix=./uploads/pages -x --mirror --convert-links --adjust-extension --page-requisites --no-parent https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/
```