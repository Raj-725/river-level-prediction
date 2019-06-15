import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from .river_api import print_date_time


class JobScheduler:
    def schedule(self, func_name, seconds):
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=func_name, trigger="interval", seconds=seconds)
        scheduler.start()
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    def schedule_email(self):
        seconds = 3
        self.schedule(print_date_time, seconds)

    def schedule_api_jobs(self):
        seconds = 1
        self.schedule(print_date_time, seconds)


def send_email():
    print("Sent")
