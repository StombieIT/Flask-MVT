'''
In this file you should start your project
'''

from flask_script import Manager
from flask_migrate import MigrateCommand
from app import app
from views import (
	forbidden
)

manager = Manager(app)
manager.add_command('db', MigrateCommand)  # You should call command the same as your database exampler

if __name__ == '__main__':
	manager.run()