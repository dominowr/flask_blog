from app.auth.entities.user_entity import User
from flask.views import View
from flask import request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash


class LoginUserView(View):
    def dispatch_request(self):
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, request.form.get("password")):
            flash("User does not exist.")
            return redirect(url_for("auth.login_index"))

        login_user(user)

        return redirect(url_for("main.index"))
        
