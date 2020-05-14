from datetime import datetime
from flask import current_app
from app import db


class Donation_post(db.Model):
    __tablename__='donate'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category=db.Column(db.String)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Request_post(db.Model):
    __tablename__='request'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category=db.Column(db.String)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)
    location= db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey
    ('users.id'), nullable=False)
