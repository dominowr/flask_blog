import os
import click
from dotenv import load_dotenv
from flask import Flask
from config import Config
from app.extensions import db, migrate, ckeditor, login_manager, security, csrf, gravatar, bootstrap as bts
from app.auth.entities.role_entity import Role
from app.auth.entities.user_entity import User
from flask_security import SQLAlchemySessionUserDatastore
from werkzeug.security import generate_password_hash
from app.main import bp as main_bp
from app.post import bp as post_bp
from app.auth import bp as auth_bp

load_dotenv()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Load users, roles for a session
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)
    bts.init_app(app)
    login_manager.init_app(app)
    security.init_app(app, user_datastore)
    csrf.init_app(app)
    gravatar.init_app(app)

    @app.cli.command("create-admin")
    @click.argument("name")
    @click.argument("email")
    @click.argument("password")
    def create_admin(name, email, password):
        hashed_password = generate_password_hash(password, method="pbkdf2", salt_length=10)
        user_datastore.create_user(email=email, password=hashed_password, name=name)
        user_datastore.create_role(name="admin", description="Administrator")
        user_datastore.add_role_to_user(email, "admin")
        db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(auth_bp)

    return app
