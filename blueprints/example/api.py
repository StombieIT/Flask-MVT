'''
If you need to create api for your app,
you should do it there and create special blueprint
for it.
You can import default and installed libraries there, not files
from this app.
'''

from flask import Blueprint, jsonify

api_example = Blueprint('api_example', __name__)

'''
If you need to import something else (files from this app),
you should do it there, after creating a blueprint
to avoid circular imports.
'''

from .models import Example

'''
You should make your routes after importing and all settings
of services (for example) or something else.
'''

@api_example.route('/examples/', methods=['GET'])
def examples():
	examples = Example.query.all()
	examples_json = [
		{
			'id': example.id,
			'name': example.name
		}
		for example in examples
	]
	return jsonify(examples_json)