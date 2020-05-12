from crontab import CronTab

my_cron = CronTab(user='lst')
job = my_cron.new(command='python /home/lst/ctab/kitemain.py')
job.minute.every(1)
my_cron.write()