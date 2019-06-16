from river_prediction_app import db


class CRUD():

    def save(self):
        if self.id is None:
            db.session.add(self)
        return db.session.commit()

    def destroy(self):
        db.session.delete(self)
        return db.session.commit()


class RiverLevel(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    river_name = db.Column(db.String(100))
    station_id = db.Column(db.String(100))
    station_name = db.Column(db.String(100))
    level = db.Column(db.String(100))
    time = db.Column(db.String(100))
    prediction = db.Column(db.String(100))
    avg_rain = db.Column(db.Float)

    def __repr__(self):
        return f"RiverLevel(River: '{self.river_name}', Station: '{self.station_name}', " \
            f"Current Level: '{self.level}', Prediction: '{self.prediction}')"


class Subscription(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    reason = db.Column(db.String(100))

    def __repr__(self):
        return f"Subscription('{self.name}', '{self.email}', '{self.location}', '{self.reason}')"
