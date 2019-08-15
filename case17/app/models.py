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
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
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
    manager = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<Admin {}>'.format(self.manager)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


class SuperCat(db.Model):
    __tablename__ = 'supercat'
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    subcat = db.relationship('Subcat', backref='supercat')
    goods = db.relationship('Goods', backref='supercat')

    def __repr__(self):
        return '<SuperCat {}>'.format(self.cat_name)


class SubCat(db.Model):
    __tablename__ = 'subcat'
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    super_cat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))
    goods = db.relationship('Goods', backref='subcat')

    def __repr__(self):
        return '<SubCat {}>'.format(self.cat_name)


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    original_price = db.Column(db.DECIMAL(10, 2))
    current_price = db.Column(db.DECIMAL(10, 2))
    picture = db.Column(db.String(255))
    introduction = db.Column(db.Text)
    views_count = db.Column(db.Integer, default=0)
    is_sale = db.Column(db.Boolean(), default=0)
    is_new = db.Column(db.Boolean(), default=0)

    supercat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))
    subcat_id = db.Column(db.Integer, db.ForeignKey('subcat.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    cart = db.relationship('Cart', backref='goods')
    orders_detail = db.relationship('OrdersDetail', backref='goods')

    def __repr__(self):
        return '<Goods {}>'.format(self.name)


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    user_id = db.Column(db.Integer)
    number = db.Column(db.Integer, default=0)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Cart {}>'.format(self.id)


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recevie_name = db.Column(db.String(255))
    recevie_address = db.Column(db.String(255))
    recevie_tel = db.Column(db.String(255))
    remark = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    orders_detail = db.relationship('OrdersDetail', backref='orders')

    def __repr__(self):
        return '<Orders {}>'.format(self.id)


class OrdersDetail(db.Model):
    __tablename__ = 'orders_detail'
    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    number = db.Column(db.Integer, default=0)

