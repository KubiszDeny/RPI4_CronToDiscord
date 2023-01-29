import subprocess

def send_notify(msg_title, msg_description):
    from discord_webhook import DiscordWebhook, DiscordEmbed
    discord_api = "https://discord.com/api/webhooks/ID-XXXX/TOKEN-XXXXXXXXXXXXXXXXXXX"
    webhook = DiscordWebhook(url=discord_api)
    embed = DiscordEmbed(title=msg_title, description=msg_description, color='f80303')
    webhook.add_embed(embed)

    webhook.execute()

#Rpi-Cron - Update / Upgrade / Autoremove / Autoclean / PipUpdate
get_update = subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE).stdout.decode('utf-8')
get_upgrade = subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], stdout=subprocess.PIPE).stdout.decode('utf-8')
get_autoremove = subprocess.run(['sudo', 'apt-get', 'autoremove'], stdout=subprocess.PIPE).stdout.decode('utf-8')
get_autoclean = subprocess.run(['sudo', 'apt-get', 'autoclean'], stdout=subprocess.PIPE).stdout.decode('utf-8')
upg_pythonpip = subprocess.run(['sudo','pip3', 'install', '--upgrade', 'pip', '--root-user-action=ignore'], stdout=subprocess.PIPE).stdout.decode('utf-8')

#Notify to Discord using WebHook
send_notify("System Update", get_update)
send_notify("System Upgrade", get_upgrade)
send_notify("System AutoRemove", get_autoremove)
send_notify("System AutoClean", get_autoclean)
send_notify("Python Pip-Update", upg_pythonpip)

#crontab -e
#Timing: https://crontab.guru

#Tady se spustí aktualizační cron
#0 1 * * * python /cron.py

#Kill tmux (Debug)
#50 4 * * * pkill tmux

#TTV Discord bot to crontab
#0 5 * * * pgrep tmux || (tmux new-session -d 'cd /home/pi/Enhanced-TTVDropBot && npm run start:production')

#Run crontab now 
#crontab -l | grep -v '^#' | cut -f 6- -d ' ' | while read CMD; do eval $CMD; done
