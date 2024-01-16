from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_security import Security
from flask_gravatar import Gravatar



db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
ckeditor = CKEditor()
login_manager = LoginManager()
csrf = CSRFProtect()
security = Security()
gravatar = Gravatar()
