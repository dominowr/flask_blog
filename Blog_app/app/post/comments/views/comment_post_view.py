from app.extensions import db
from app.post.entities.comment_entity import Comment
from app.post.entities.post_entity import Post
from flask import request, redirect, url_for
from flask.views import View
from flask_login import current_user


class CommentView(View):
    def dispatch_request(self, id):

        parent_post = Post.query.get_or_404(id)

        comment = Comment(
            parent_post = parent_post,
            author = current_user,
            body = request.form.get("body")
        )

        db.session.add(comment)
        db.session.commit()


        return redirect(url_for("blogpost.read_post", id=id))