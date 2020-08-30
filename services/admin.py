'''
In this file you should create IndexView of your admin panel.
You should import there models and ModelViews of blueprints
and add view of them
'''

from flask import abort
from flask_admin import Admin, AdminIndexView
from .db import db
from blueprints.example.models import Example
from blueprints.example.admin import ExampleModelView

class IndexView(AdminIndexView):
	def is_accessible(self):
		return False
	def inaccessible_callback(self, name, **kwargs):
		abort(403)

admin = Admin(index_view=IndexView())
admin.add_view(ExampleModelView(Example, db.session, endpoint='examples'))  # You should change endpoint to the name of table of current model