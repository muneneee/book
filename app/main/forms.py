from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required


class CommentForm(FlaskForm):
    comment = TextAreaField("Leave a comment", validators = [Required()])
    submit = SubmitField("Post")


class PostForm(FlaskForm):
    title = StringField('Book Title', validators=[Required()])
    category=SelectField('Category', choices=[('Primary-books','Primary books'),('Secondary-books', 'Secondary books'),('Others','Others')])
    number = IntegerField('Number of books', validators=[Required()])
    submit = SubmitField('Donate')
