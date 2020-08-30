'''
You should use this file as creating of your blueprint and
routing of it.
I would recommend you use the name of file and exampler of blueprint
the same as the name of current dir to avoid problems with readability
of your code.
Besides, you have to create another dir in templates with name
the same as this dir and put templates of this blueprint
in it.
The same thing you should do with static folder if you need it.
You can import default and installed libraries there, not files
from this app.
'''

from flask import Blueprint, render_template

example = Blueprint('example', __name__)

'''
If you need to import something else (files from this app),
you should do it there, after creating a blueprint
to avoid circular imports.
'''

from .models import Example
from .forms import ExampleForm

'''
You should make your routes after importing and all settings
of services (for example) or something else.
'''

@example.route('/')
def index():
	return render_template('example/index.html')
