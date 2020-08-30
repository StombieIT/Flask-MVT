'''
In this file you should configure permission for ModelView
of models of current blueprint.
'''

from flask import abort
from flask_admin.contrib.sqla import ModelView

class ExampleModelView(ModelView):  # Use name of it as the name of match model and endpoint as 'ModelView'
	def is_accessible(self):
		return False
	def inaccessible_callback(self, name, **kwargs):
		abort(403)