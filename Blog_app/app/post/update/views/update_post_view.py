from app.extensions import db
from app.post.entities.post_entity import Post
from app.helpers.role_checker_decorator import has_role
from app.post.create.forms.create_post_form import CreatePostForm
from flask.views import View
from flask import redirect, request, url_for


class UpdateView(View):
        @has_role("admin")
        def dispatch_request(self, id):
            update_form = CreatePostForm(request.form)
            post = Post.query.get_or_404(id)


            post.title = update_form.title.data
            post.subtitle = update_form.subtitle.data
            post.author = update_form.author.data
            post.img_url = update_form.img_url.data
            post.body = update_form.body.data

            db.session.commit()

            return redirect(url_for("main.index"))