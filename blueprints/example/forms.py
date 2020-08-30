'''
This file serves for Flask-WTF,
you should create your forms there.
'''
from flask_wtf import FlaskForm  # Use only 'FlaskForm' instead of 'Form' because it will be removed in future versions
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp # Use only 'DataRequired' instead of 'Required' because it will be removed in future versions

'''
If you need to create regexp, you
should create const for that and add '_RE' as endpoint of it.
'''

NAME_RE = r'^[a-z]+$'

'''
If you need to make form for something model,
you should call your form the same.
Make the endpoint 'Form' of class of your form.
'''

class ExampleForm(FlaskForm):
	name = StringField(
		'Name',
		validators=[
			DataRequired(message='Name is required'),  # If you need to message your validator, do it with named arg
			Length(1, 64, message='Name can contain only 64 symbols'),
			Regexp(NAME_RE, message='Invalid input of Name')
		]
	)
	submit = SubmitField('Submit')