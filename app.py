import osfrom flask import Flaskfrom flask_sqlalchemy import SQLAlchemyfrom config import Configuration, DevelopmentConfigapp = Flask(__name__, static_url_path='/static')# app = Flask(__name__, static_url_path='',#             static_folder='static',#             template_folder='templates')# app.config.from_object(os.environ['APP_SETTINGS'])# app.config['APP_SETTINGS'] = "config.DevelopmentConfig"# app.config['APP_SETTINGS'] = DevelopmentConfig2app.config.from_object(Configuration)app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falsedb = SQLAlchemy(app)import routesimport utilsimport modelsfrom routes import *if __name__ == "__main__":    app.run()# if __name__ == '__main__':  # pragma: no cover#     app.run(port=80)