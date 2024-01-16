from app.extensions import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from flask_security import RoleMixin

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer(), db.ForeignKey("user.id", ondelete='CASCADE')),
                       db.Column("role_id", db.Integer(), db.ForeignKey("role.id", ondelete='CASCADE'))
                       )


class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(80), unique=True)
    description: Mapped[str] = Column(String(100))
