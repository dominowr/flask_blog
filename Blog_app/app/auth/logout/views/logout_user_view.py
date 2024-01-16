from flask import redirect, url_for
from flask.views import View
from flask_login import logout_user


class LogoutUserview(View):
    def dispatch_request(self):
        logout_user()
        return redirect(url_for("main.index"))