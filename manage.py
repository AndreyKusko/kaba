import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from flask_alchemydumps import AlchemyDumps, AlchemyDumpsCommand


app.config.from_object(os.environ['APP_SETTINGS'])
manager = Manager(app)


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# init Alchemy Dumps
alchemydumps = AlchemyDumps(app, db)
manager.add_command('alchemydumps', AlchemyDumpsCommand)


if __name__ == '__main__':
    manager.run()