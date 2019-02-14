""" run server """
from server import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import app, db

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()
if __name__ == '__main__':
    manager.run()
