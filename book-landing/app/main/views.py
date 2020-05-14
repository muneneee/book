from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import CommentForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Comment



@main.route('/')
def index():

    comment_form = CommentForm()

    all_comments = Comment.query.all()

    
    title = 'Home'
    return render_template('index.html',title = title,comment=all_comments,comment_form = comment_form)



@main.route('/', methods = ['GET','POST'])
@login_required
def comment():
    comment_form = CommentForm()
 
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(comment = comment, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('main.index'))

    all_comments = Comment.query.filter_by().all()

    
    return render_template('index.html' ,title = title, comment_form = comment_form)
