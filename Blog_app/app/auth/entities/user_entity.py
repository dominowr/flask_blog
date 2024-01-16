import app.post.entities
import app.auth.entities
from app.auth.entities.role_entity import roles_users
from app.extensions import db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, relationship
from flask_security import UserMixin
from typing import List


class User(db.Model,UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String, nullable=False)
    password: Mapped[str] = Column(String, nullable=False)
    name: Mapped[str] = Column(String(15), nullable=False)
    active: Mapped[bool] = Column(Boolean)
    roles: Mapped[List["app.auth.entities.role_entity.Role"]] = relationship(secondary=roles_users)
    posts: Mapped[List["app.post.entities.post_entity.Post"]] = relationship(back_populates="author")
    comments: Mapped[List["app.post.entities.comment_entity.Comment"]] = relationship(back_populates="author")