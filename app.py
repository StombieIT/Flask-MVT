'''
In this file you should create exampler app of Flask class.
'''
from flask import Flask

app = Flask(__name__)

'''
Besides, you can import there file of your settings
and change configuration of your app from object of it.
'''

import settings

app.config.from_object(settings)

'''
Then, you have to import your services there and init
them with init_app() and transfer to it your app
to avoid circular imports.
I would recommend you to create different dir for them.
'''

from services.db import db
from services.admin import admin
from services.migrate import migrate

db.init_app(app)
admin.init_app(app)
migrate.init_app(app, db)

'''
So, after that you can import your blueprints
from similar dir and register them hear.
'''

from blueprints.example.example import example
from blueprints.example.api import api_example

app.register_blueprint(example, url_prefix='/example')
app.register_blueprint(api_example, url_prefix='/api/example')
