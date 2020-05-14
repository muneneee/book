from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from flask import current_app,abort
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    bio = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)


    comments = db.relationship('Comment', backref = 'user', lazy ='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment =  db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_comment(self):
        db.session.add(self)
        db.session.commit()



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}'




class Donation_post(db.Model):
    __tablename__='donate'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category=db.Column(db.String)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            return abort(403)
    def not_auth(self):
        return "You are not authorised to use the admin dashboard"
