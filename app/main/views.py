from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from app import db
from app.models import Donation_post
from .forms import PostForm
from . import main

@main.route("/")
@main.route("/index")
def index():
    page = request.args.get('page', 1, type=int)
    
    primarybooks=Donation_post.query.filter_by(category='Primary-books')
    secondarybooks=Donation_post.query.filter_by(category='Secondary-books')
    otherbooks=Donation_post.query.filter_by(category='Other-books')

    return render_template('index.html', primarybooks=primarybooks,secondarybooks=secondarybooks,otherbooks=otherbooks)



@main.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Donation_post(title=form.title.data, category=form.category.data,number=form.number.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Donation has been received!', 'success')
        return redirect(url_for('main.index'))
    return render_template('index.html', title='New Post',form=form, legend='New Post')





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
    return render_template('index.html', title='Update Donation',
                           form=form, legend='Update Donation')


