from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
from os import path
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
#mysql = MySQL()
DB_NAME = "database.db"
UPLOAD_FOLDER = "img"
app = Flask(__name__)

def create_app():

    # Encrypt the cookies and session data related to our website
    app.config['SECRET_KEY'] = 'thecodecrew'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cliugmsmoerigucse4t8o74tow34ot8xw39@3.120.159.145:3306/foodfinder'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    '''app.config['MYSQL_HOST'] = '3.120.159.145'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'cliugmsmoerigucse4t8o74tow34ot8xw39'
    app.config['MYSQL_DB'] = 'foodfinder'''

    #mysql.init_app(app)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
