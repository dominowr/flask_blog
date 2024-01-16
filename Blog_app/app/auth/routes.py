from app.auth import bp
from app.auth.register.views.register_index_view import RegisterIndexView
from app.auth.register.views.register_user_view import RegisterUserView
from .login.views.login_index_view import LoginIndexView
from .login.views.login_user_view import LoginUserView
from .logout.views.logout_user_view import LogoutUserview


bp.add_url_rule("/auth/register", view_func=RegisterIndexView.as_view("register_index"), methods=["GET"])
bp.add_url_rule("/auth/register", view_func=RegisterUserView.as_view("register_user"), methods=["POST"])
bp.add_url_rule("/auth/login", view_func=LoginIndexView.as_view("login_index"), methods=["GET"])
bp.add_url_rule("/auth/login", view_func=LoginUserView.as_view("login_user"), methods=["POST"])
bp.add_url_rule("/auth/logout", view_func=LogoutUserview.as_view("logout_user"), methods=["GET"])