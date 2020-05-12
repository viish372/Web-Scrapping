from crontab import CronTab

my_cron = CronTab(user='lst')
for job in my_cron:
    my_cron.remove_all()
    my_cron.write()