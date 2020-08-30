'''
In this file you should import your app and make
routes of it.
But I would recommend you to use it only for errors
and another services like flask-caching. If you want
to make routes for main index, you should create
blueprint for it.
'''

from flask import render_template
from app import app

@app.errorhandler(403)
def forbidden(error):  # Use descriptions of errors as name of function, but not error status code
	return render_template('index/forbidden.html')  # Call the same your template
	# Use 'index' as name of dir with app templates
