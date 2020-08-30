'''
First of all, you should import there exampler of your db class
from services and then, create your models
'''

from services.db import db

class Example(db.Model):
	__tablename__ = 'examples'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(64),
		unique=True,
		nullable=False
	)
	def __repr__(self):
		return '<Example %r>' % self.name
