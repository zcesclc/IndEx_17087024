from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

from app.models import User


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    user_ref = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email(message='Valid email address required')])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def validate_user_ref(self,user_ref):
        user = User.query.filter_by(user_ref=user_ref.data).first()
        if user is not None:
            raise ValidationError(
                'An account is already registered for that username. Please create another username.')
