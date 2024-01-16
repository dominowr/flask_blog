from app.post.entities.post_entity import Post
from flask.views import View
from flask import render_template


class MainIndexView(View):
    def dispatch_request(self):
        posts = Post.query.all()
        return render_template("index.html", all_posts=posts)