from app.extensions import db
from app.auth.entities.role_entity import Role
from app.auth.entities.user_entity import User
from flask.views import View
from flask_login import login_user
from werkzeug.security import generate_password_hash
from flask import request,redirect, url_for, flash


class RegisterUserView(View):
    def dispatch_request(self):

        user = User.query.filter_by(email=request.form.get("email")).first()

        if user:
            flash("This email is already registered.")
            return redirect(url_for("auth.register_index"))
        
        new_user = User(
            email = request.form.get("email"),
            active = 1,
            password = generate_password_hash(request.form.get("password"), method="pbkdf2", salt_length=10),
            name = request.form.get("name")
        )

        
        user_role = Role.query.filter_by(name="user").first()

        if not user_role:
            user_role = Role(name="user", description="Regular user")
            db.session.add(user_role)

        new_user.roles.append(user_role)

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("main.index"))