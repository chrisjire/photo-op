from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand  
from flask_script import Manager,Server
from app.models import User


app = create_app()

manager = Manager(app)
manager.add_command('runserver',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell():
    return{"db":db,"User":User}

# @manager.test
# def test():
#     import unittest
#     tests = unitest.TestLoader().discover('tests')
#     unittest.TextTestResult(verbosity=5).run(tests)
    
if __name__=='__main__':
  manager.run()