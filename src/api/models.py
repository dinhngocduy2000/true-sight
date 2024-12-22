from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

todo_list_table = Table("todo_list",
                        Base.metadata,
                        Column("todo_id", Integer, primary_key=True, nullable=False,
                               autoincrement=True),
                        Column("description", String, nullable=True),
                        Column("status", String, nullable=False), Column("todo_name", String, nullable=False))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(128))
