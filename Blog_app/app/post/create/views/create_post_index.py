from app.post.create.forms.create_post_form import CreatePostForm
from app.helpers.role_checker_decorator import has_role
from flask.views import View
from flask import render_template


class CreateIndexView(View):
    @has_role("admin")
    def dispatch_request(self):
        form = CreatePostForm()
        return render_template("make-post.html", form=form)