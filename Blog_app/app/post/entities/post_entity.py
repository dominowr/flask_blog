import app.auth.entities
import app.post.entities
from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, relationship
from typing import List


class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = Column(Integer, primary_key=True)
    author_id: Mapped[int] = Column(ForeignKey("user.id", ondelete='CASCADE'))
    author: Mapped["app.auth.entities.user_entity.User"] = relationship(back_populates="posts")
    title: Mapped[str] = Column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = Column(String(250), nullable=False)
    date: Mapped[str] = Column(String(250), nullable=False)
    body: Mapped[str] = Column(Text, nullable=False)
    img_url: Mapped[str] = Column(String(250), nullable=False)
    comments: Mapped[List["app.post.entities.comment_entity.Comment"]] = relationship(back_populates="parent_post")
    


