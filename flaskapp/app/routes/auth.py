import flask
from flask import Blueprint, render_template
from flask_login import login_user
from wtforms import Form, PasswordField, StringField, validators
from app.models import User

auth = Blueprint('auth', __name__)


class LoginForm(Form):
    username = StringField('Usuário', validators=[validators.DataRequired(
        message="É obrigatório o preenchimento do usuário")])
    password = PasswordField('Senha', validators=[validators.DataRequired(
        message='É obrigatório o preenchimento da senha')])

    def validate_on_submit(self):
        print(self.username)
        return True


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = User.get(username=form.username)
        login_user(user)

        flask.flash('Logged in successfully.')

        return flask.redirect(next or flask.url_for('index'))
    return render_template('login.html', form=form)
