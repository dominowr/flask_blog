from app.post.create.forms.create_post_form import CreatePostForm
from app.post.entities.post_entity import Post
from app.helpers.role_checker_decorator import has_role
from flask.views import View
from flask import render_template, request


class UpdateIndexView(View):
    @has_role("admin")
    def dispatch_request(self):
        id = request.args.get("id")
        post = Post.query.get_or_404(id)

        edit_form = CreatePostForm(
            title = post.title,
            subtitle = post.subtitle,
            author = post.author,
            img_url = post.img_url,
            body = post.body,
        )

        return render_template("make-post.html", template_folder="post/templates", post=post, form=edit_form, is_edit=True)
    