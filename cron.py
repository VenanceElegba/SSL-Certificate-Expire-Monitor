from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='python3 main.py')
job.dow.on('MON', 'FRI')
cron.write()
