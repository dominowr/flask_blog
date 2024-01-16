import app.auth.entities
import app.post.entities
from app.extensions import db
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship


class Comment(db.Model):
    __tablename__ = "comment"
    id: Mapped[int] = Column(Integer, primary_key=True)
    author_id: Mapped[int] = Column(ForeignKey("user.id", ondelete='CASCADE'))
    author: Mapped["app.auth.entities.user_entity.User"] = relationship(back_populates="comments")
    body: Mapped[str] = Column(Text, nullable=False)
    post_id: Mapped[int] = Column(ForeignKey("post.id"))
    parent_post: Mapped["app.post.entities.post_entity.Post"] = relationship(back_populates="comments")
