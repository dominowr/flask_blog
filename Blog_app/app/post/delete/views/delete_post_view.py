from app.extensions import db
from app.helpers.role_checker_decorator import has_role
from app.post.entities.post_entity import Post
from flask.views import View
from flask import redirect, url_for


class DeleteView(View):
    @has_role("admin")
    def dispatch_request(self, id):
        post = Post.query.get_or_404(id)

        db.session.delete(post)
        db.session.commit()

        return redirect(url_for("main.index"))