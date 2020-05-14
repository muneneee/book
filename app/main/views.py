from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import CommentForm
from app.models import Donation_post
from .forms import PostForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Comment, Subscriber



@main.route('/')
def index():

    primarybooks=Donation_post.query.filter_by(category='Primary-books')
    secondarybooks=Donation_post.query.filter_by(category='Secondary-books')
    otherbooks=Donation_post.query.filter_by(category='Others')


    donations = Donation_post.query.filter_by().all()


    comment_form = CommentForm()

    all_comments = Comment.query.all()

    
    title = 'Home'
    return render_template('index.html',title = title,comment=all_comments, donations=donations, comment_form = comment_form, primarybooks=primarybooks,secondarybooks=secondarybooks,otherbooks=otherbooks)



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





@main.route('/donation', methods=['GET', 'POST'])
@login_required
def new_post():
    donation_form = PostForm()
    if donation_form.validate_on_submit():
        post = Donation_post(title=donation_form.title.data, category=donation_form.category.data,number=donation_form.number.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Donation has been received!', 'success')

        subscribers = Subscriber.query.all()
        for subscriber in subscribers:
            mail_message("Yur donation has been received and recorded", "email/new_post", subscriber.email, subscriber = subscriber)

        return redirect(url_for('main.index'))
    return render_template('donation.html', title='New Post',donation_form=donation_form)





@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])

def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Donation has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('index.html', title='Update Donation',form=form, legend='Update Donation')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    post = post.query.filter_by(user_id = user.id).order_by(post.posted.desc())

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, post = post)



