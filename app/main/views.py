from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import CommentForm,BeneficiaryForm
from app.models import Donation_post,User
from .forms import PostForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Comment,Request_post
from ..gmail import mail_message



@main.route('/')
def index():

    comment_form = CommentForm()

    all_comments = Comment.query.all()

    
    title = 'Home'
    return render_template('index.html',title = title,comment=all_comments, donations=donations, comment_form = comment_form)



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
        return redirect(url_for('main.index'))
    return render_template('donation.html', title='New Post',donation_form=donation_form)



@main.route('/donations')
def donations():

    primarybooks=Donation_post.query.filter_by(category='Primary-books')
    secondarybooks=Donation_post.query.filter_by(category='Secondary-books')
    otherbooks=Donation_post.query.filter_by(category='Others')


    donations = Donation_post.query.filter_by().all()


    comment_form = CommentForm()

    all_comments = Comment.query.all()

    
    title = 'Donations'
    return render_template('donations.html',title = title, donations=donations, primarybooks=primarybooks,secondarybooks=secondarybooks,otherbooks=otherbooks)



@main.route('/request', methods=['GET', 'POST'])
@login_required
def new_request():
    request_form = BeneficiaryForm()
    if request_form.validate_on_submit():
        request = Request_post(title=request_form.title.data, email = request_form.email.data,category=request_form.category.data,number=request_form.number.data)
        db.session.add(request)
        db.session.commit()

        mail_message("Your request is been processed","gmail/process",request.email,request=request)

    

        flash('Your Donation has been received!', 'success')
        return redirect(url_for('main.index'))
    return render_template('request.html', title='New Request',request_form=request_form)





@main.route('/approved')
def approval():
    if Request_post.approved == True:
        return mail_message("Your request has been approved","gmail/approval",request.email,request = request)

    return redirect(url_for('main.index'))



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    post = post.query.filter_by(user_id = user.id).order_by(post.posted.desc())
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, post = post) 



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form,user=user)

    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))