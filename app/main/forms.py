from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectField,IntegerField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    category=SelectField('Category', choices=[('Primary-books','Primary books'),('Secondary-books', 'Secondary books'),('Others','Others')])
    number = IntegerField('Number of books', validators=[DataRequired()])
    submit = SubmitField('Donate')

class BeneficiaryForm(FlaskForm):
    btitle = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')