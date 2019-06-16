from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Time in seconds
EMAIL_INTERVAL = 24 * 60 * 60
RIVER_LEVEL_PREDICTION_INTERVAL = 3 * 60 * 60

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

SENDER_EMAIL = 'YOUR GMAIL HERE'
app.config['MAIL_USERNAME'] = SENDER_EMAIL
app.config['MAIL_PASSWORD'] = 'YOUR GMAIL APP KEY'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize database and perform migrations
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


# create all db tables
@app.before_first_request
def create_tables():
    db.create_all()


from river_prediction_app.mail import SendMail

send_email = SendMail(app, sender_email=SENDER_EMAIL)

from river_prediction_app import routes

from river_prediction_app.backgound_scheduler import JobScheduler

job_scheduler = JobScheduler(send_email)
job_scheduler.schedule_email(EMAIL_INTERVAL)
job_scheduler.schedule_river_level_prediction_job(RIVER_LEVEL_PREDICTION_INTERVAL)
