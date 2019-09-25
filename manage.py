from app import create_app,db  
from flask_script import Manager,Server
from app.models import User


app = create_app()
manager.add_command('runserver',Server)
manager = Manager(app)

@maanger.shell
def add_shell():
    return{"db":db,"User":User,"Blog":Blog,"Comment":Commnet}

@manager.add_command
def test():
    import unittest
    tests = unitest.TestLoader().discover('tests')
    unittest.TextTestResult(verbosity=5).run(tests)
    
if __name__ == '__main__':
    manager.run()