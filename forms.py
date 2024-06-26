from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length, Regexp
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different one.')

class AccountForm(FlaskForm):
    username = StringField('New Username', validators=[DataRequired()], render_kw={"placeholder": "Leave blank to keep the same"})
    email = StringField('New Email', validators=[Email()], render_kw={"placeholder": "Leave blank to keep the same"})
    password = PasswordField('Current Password', validators=[DataRequired()], render_kw={"placeholder": "Required for any changes"})
    new_password = PasswordField('New Password', validators=[Length(min=8, message="Password must be at least 8 characters long"), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&].{7,}$', message="Password must include one lowercase letter, one uppercase letter, one digit, and one special character")], render_kw={"placeholder": "Leave blank to keep the same"})
    submit_username = SubmitField('Update Username')
    submit_email = SubmitField('Update Email')
    submit_password = SubmitField('Update Password')

class LoginForm(FlaskForm):
    # Updated field label to reflect that it can be either username or email
    username = StringField('Username/Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')