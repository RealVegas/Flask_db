from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=35)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Такая эл. почта уже используется')


class UpdateForm(FlaskForm):
    username = StringField('Изменить имя пользователя', validators=[DataRequired(), Length(min=2, max=35)])
    email = StringField('Изменить E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Введите новый пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите новый пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сохранить изменения')
    not_submit = SubmitField('Отменить изменения')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомни меня')
    submit = SubmitField('Войти')