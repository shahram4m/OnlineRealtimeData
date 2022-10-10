from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from helper.csvDataHelper import *

#job for update table from csv every 24 hour this is optional by user
def start():
    print('job started at:', str(datetime.now()))
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Calcutta'})
    scheduler.add_job(read_csv_data, 'interval', minutes=60*24)
    scheduler.start()