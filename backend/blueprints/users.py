import re

from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    session,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc

from backend.core.db import db
from backend.models import User

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        valid = True
        user = User.query.filter(
            User.username == request.form['username']
        ).first()
        if not user:
            flash('Пользователь с таким именем не найден')
            valid = False
        if user and not check_password_hash(
                user.password, request.form['password']
        ):
            flash('Введен неправильный пароль')
            valid = False
        if valid:
            # TODO заменить на нормальный логин
            flash('вы успешно авторизовались')
            session['login'] = True
            session['user_id'] = user.id
    return render_template('login.html', data=request.form)


@users_blueprint.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        valid = True
        if len(request.form['username']) < 4:
            flash('Имя пользователя должно содержать минимум 4 символа')
            valid = False
        if User.query.filter(
                User.username == request.form['username']
        ).first():
            flash('Пользователь с таким именем уже зарегистрирован')
            valid = False
        if not re.match(r'^[0-9A-Za-z_-]+$', request.form['username']):
            flash(
                'Имя пользователя может содержать только буквы латинского '
                'алфавита, цифры, нижнее подчеркивание и дефис'
            )
            valid = False
        if len(request.form['email']) < 4:
            flash('Адрес почты должен содержать минимум 4 символа')
            valid = False
        if User.query.filter(
                User.email == request.form['email']
        ).first():
            flash('Пользователь с таким email уже зарегистрирован')
            valid = False
        if not re.match(r'^[^@ ]+@[^@ ]+\.[^@ ]+$', request.form['email']):
            flash('Введен некорректный email')
            valid = False
        if request.form['password'] != request.form['password2']:
            flash('Пароли не совпадают')
            valid = False
        if len(request.form['password']) < 8:
            flash('Длина пароля должна быть минимум 8 символов')
            valid = False
        if valid:
            try:
                new_user = User(
                    username=request.form['username'],
                    email=request.form['email'],
                    password=generate_password_hash(request.form['password']),
                    first_name=request.form['first_name'],
                    last_name=request.form['last_name'],
                    middle_name=request.form['middle_name'],
                    is_active=True,
                    about=request.form['about'],
                    # TODO поменять на аплоад изображения
                    user_image=request.form['user_image'],
                )
                db.session.add(new_user)
                db.session.commit()
            except exc.SQLAlchemyError:
                db.session.rollback()
            return redirect(url_for('users.login'))
    return render_template('registration.html', data=request.form)
