from app.auth.register.forms.register_index_form import RegisterForm
from flask.views import View
from flask import render_template


class RegisterIndexView(View):
    def dispatch_request(self):
        form = RegisterForm()
        return render_template("register.html", form=form)