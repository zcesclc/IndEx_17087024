from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    user_ref = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    forecast = db.relationship("Forecast",backref= 'users')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class City(db.Model):
    __tablename__ = 'City'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    forecasts = db.relationship("Forecast", backref='cities')

class Forecast(db.Model):
    __tablename__ = 'Forecast'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('City.id'), nullable=False)


