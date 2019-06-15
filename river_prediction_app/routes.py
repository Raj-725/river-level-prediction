from flask import render_template, url_for, flash, redirect
from river_prediction_app import app, db
from river_prediction_app.forms import RegistrationForm
from river_prediction_app.models import User, Post, Subscription

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home/")
def home():
    data = {'prediction': 'Level will go up', 'current_level': '0.5', 'station_name': 'Western Avenue',
            'latest_time': '15/06/2019 12:00'}
    return render_template('home.html', data=data)


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Email {form.email.data} has been registered  for updates.', 'success')
        subscription = Subscription(name=form.name.data, email=form.email.data, location=form.location.data,
                                    reason=form.reason.data)
        db.session.add(subscription)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
