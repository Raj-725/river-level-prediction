from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
# Initialize database and perform migrations
db.init_app(app)
migrate = Migrate(app, db)


# create all db tables
@app.before_first_request
def create_tables():
    db.create_all()


mail = Mail(app)

from river_prediction_app import routes
from river_prediction_app.backgound_scheduler import JobScheduler

job_scheduler = JobScheduler()
# job_scheduler.schedule_email()
# job_scheduler.schedule_api_jobs()
