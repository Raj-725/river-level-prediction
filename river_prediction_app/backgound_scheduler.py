import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from river_prediction_app import river_api
from river_prediction_app.models import RiverLevel

email_interval = 12 * 60 * 60
river_level_interval = 3 * 60 * 60


class JobScheduler:
    def schedule(self, func_name, seconds):
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=func_name, trigger="interval", seconds=seconds)
        scheduler.start()
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    def schedule_email(self, interval=None):
        seconds = interval if interval is not None else email_interval
        print("Scheduling Email Alerts with Interval(Seconds): ", seconds)
        self.schedule(send_email, seconds)

    def schedule_river_level_prediction_job(self, interval=None):
        seconds = interval if interval is not None else river_level_interval
        print("Scheduling river_level_prediction with Interval(Seconds): ", seconds)
        self.schedule(get_river_levels, seconds)


def send_email():
    print("Emails Sent...")


def get_river_levels():
    river_level_obj = river_api.get_river_level()
    if river_level_obj is None:
        print("No Updates from River API")
        return
    river_level = RiverLevel(**river_level_obj)
    river_level.save()
    print("Updated River Level Data: ", river_level)
