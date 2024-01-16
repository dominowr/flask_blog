from app.main import bp
from app.main.views.main_index_view import MainIndexView


bp.add_url_rule("/", view_func=MainIndexView.as_view("index"), methods=["GET"])