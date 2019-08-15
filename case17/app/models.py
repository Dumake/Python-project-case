# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : Python-project-case
# @File      : models.py
# @Date      : 2019/8/14
# @Time      : 11:53
from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Srting(100))
    password = db.Column(db.Srting(100))
    email = db.Column(db.Srting(100), unique=True)
    phone = db.Column(db.Srting(11), unique=True)
    consumption = db.Column(db.DECIMAL(10, 2), default=0)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    orders = db.relationship('Orders', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.Srting(100), unique=True)
    password = db.Column(db.Srting(100))

    def __repr__(self):
        return '<Admin {}>'.format(self.manager)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


class SuperCat(db.Model):
    __tablename__ = 'supercat'
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.Srting(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    subcat = db.relationship('Subcat', backref='supercat')
    goods = db.relationship('Goods', backref='supercat')

    def __repr__(self):
        return '<SuperCat {}>'.format(self.cat_name)


