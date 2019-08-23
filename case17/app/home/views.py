# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : Python-project-case
# @File      : views.py
# @Date      : 2019/8/14
# @Time      : 11:50

from . import home
from app.home.forms import RegisterForm
from flask import render_template


@home.route("/register/", methods=['GET', 'POST'])
def register():
    """
    登录
    :return:
    """
    form = RegisterForm()
    # ...
    return render_template('home/register.html', form=form)
