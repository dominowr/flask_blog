from flask import Blueprint


bp = Blueprint("blogpost", __name__, template_folder="templates", static_folder="static", static_url_path="/main/static")

from app.post import routes