# -*- coding: utf-8 -*-

from __init__ import db

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),unique = True)
	users = db.relationship('User',backref = 'role')

	def __repr__(self):
		return self.name


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64),unique = True,index = True)
	role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

	def __repr__(self):
		return self.username
		
		