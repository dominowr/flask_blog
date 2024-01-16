from app.post.entities.post_entity import Post
from app.post.comments.forms.comment_form import CommentPostForm
from flask.views import View
from flask import request, render_template
from flask_login import current_user


class ReadView(View):
    def dispatch_request(self):
        id = request.args.get("id")
        post = Post.query.get_or_404(id)
        form = CommentPostForm()
        return render_template("post.html", post=post, comments = post.comments,
                                logged_in=current_user.is_authenticated, form=form)