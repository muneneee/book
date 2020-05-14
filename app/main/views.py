from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from .. import db
from app.models import Donation_post
from .forms import PostForm
from . import main


@main.route("/")
@main.route("/index")
def index():
    
     primarybooks=Donation_post.query.filter_by(category='Primary-books')
     secondarybooks=Donation_post.query.filter_by(category='Secondary-books')
     otherbooks=Donation_post.query.filter_by(category='Other-books')

     donations = Donation_post.query.filter_by().all()


     title = 'Home'


     return render_template('index.html', primarybooks=primarybooks,secondarybooks=secondarybooks,otherbooks=otherbooks, donations=donations, title = title)



@main.route('/donation', methods=['GET', 'POST'])
def new_post():
    donation_form = PostForm()
    if donation_form.validate_on_submit():
        post = Donation_post(title=donation_form.title.data, category=donation_form.category.data,number=donation_form.number.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Donation has been received!', 'success')
        return redirect(url_for('main.index'))
    return render_template('donate_form.html', title='New Post',donation_form=donation_form)


@main.route('/request', methods=['GET', 'POST'])
def new_request():
    request_form = PostForm()
    if request_form.validate_on_submit():
        post = Donation_post(title=request_form.title.data, category=request_form.category.data,amount=request_form.amount.data,
        location=request_form.location.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Donation has been received!', 'success')
        return redirect(url_for('main.index'))
    return render_template('request_form.html', title='New Request',request_form=request_form)
