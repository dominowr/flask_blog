from app.extensions import db
from app.post.entities.post_entity import Post
from app.helpers.role_checker_decorator import has_role
from flask.views import View
from flask import request, redirect, url_for
from flask_security import current_user
from datetime import datetime


class CreateView(View):
    @has_role("admin")
    def dispatch_request(self):

        post = Post(
            title = request.form.get("title"),
            subtitle = request.form.get("subtitle"),
            body = request.form.get("body"),
            img_url = request.form.get("img_url"),
            author = current_user,
            date = datetime.now().strftime("%B %d, %Y")
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("main.index"))