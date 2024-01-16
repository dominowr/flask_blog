from app.auth.login.forms.login_form import LoginForm
from flask.views import View
from flask import render_template


class LoginIndexView(View):
    def dispatch_request(self):
        form = LoginForm()
        return render_template("login.html", form=form)