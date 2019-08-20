# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : Python-project-case
# @File      : forms.py
# @Date      : 2019/8/14
# @Time      : 11:50

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, ValidationError, length


class RegisterForm(FlaskForm):
    username = StringField(
        label='账户：',
        validators=[
            DataRequired("用户名不能为空！"),
            Length(min=3, max=50, message="用户名长度必须在3到50位之间")
        ]
    )
