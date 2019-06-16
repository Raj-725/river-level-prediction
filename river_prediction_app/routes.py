from flask import render_template, url_for, flash, redirect

from river_prediction_app import app, db
from river_prediction_app import river_api
from river_prediction_app.forms import RegistrationForm
from river_prediction_app.models import Subscription, RiverLevel


@app.route("/")
@app.route("/home/")
def home():
    data = {'prediction': 'Level will go up', 'current_level': '0.5', 'station_name': 'Western Avenue',
            'latest_time': '15/06/2019 12:00'}
    data = RiverLevel.query.order_by(RiverLevel.id.desc()).first()
    return render_template('home.html', data=data)


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Email {form.email.data} has been registered  for updates.', 'success')
        subscription = Subscription(name=form.name.data, email=form.email.data, location=form.location.data,
                                    reason=form.reason.data)
        subscription.save()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/delete-subscriptions/")
def delete_subscriptions():
    deleted_subscriptions = Subscription.query.delete()
    db.session.commit()
    flash(f'{deleted_subscriptions} email subscription(s) has been deleted.', 'info')
    return redirect(url_for('home'))


@app.route("/river-levels/")
def get_river_levels():
    river_level_obj = river_api.get_river_level()
    river_level = RiverLevel(**river_level_obj)
    river_level.save()
    flash(f'{river_level} has been updated.', 'info')
    return redirect(url_for('home'))
