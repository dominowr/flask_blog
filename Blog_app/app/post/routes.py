from app.post import bp
from app.post.create.views.create_post_index import CreateIndexView
from app.post.create.views.create_view import CreateView
from app.post.read.views.read_post_view import ReadView
from app.post.update.views.update_post_index_view import UpdateIndexView
from app.post.update.views.update_post_view import UpdateView
from app.post.delete.views.delete_post_view import DeleteView
from app.post.comments.views.comment_post_view import CommentView


bp.add_url_rule("/post/create", view_func=CreateIndexView.as_view("create_index"), methods =["GET"])
bp.add_url_rule("/post/create", view_func=CreateView.as_view("create_post"), methods=["POST"])
bp.add_url_rule("/post/read", view_func=ReadView.as_view("read_post"), methods=["GET"])
bp.add_url_rule("/post/update", view_func=UpdateIndexView.as_view("update_index"), methods=["GET"])
bp.add_url_rule("/post/update/<int:id>", view_func=UpdateView.as_view("update_post"), methods=["POST"])
bp.add_url_rule("/post/delete/<int:id>", view_func=DeleteView.as_view("delete_post"), methods=["POST"])
bp.add_url_rule("/post/comment/<int:id>", view_func=CommentView.as_view("comment_post"), methods=["POST"])
