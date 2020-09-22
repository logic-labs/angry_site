from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.types import TIMESTAMP
from angry_site_flask.db_psql import Base
from datetime import datetime
from sqlalchemy.schema import ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    passwd = Column(String(256), unique=True)

    def __init__(self, name=None, passwd=None):
        self.name = name
        self.passwd = passwd

    def __repr__(self):
        return "<User %r>" % (self.name)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"), unique=False)
    created = Column(TIMESTAMP, default=datetime.utcnow, unique=False, nullable=False)
    title = Column(Text, unique=False)
    body = Column(Text, unique=False)

    def __init__(self, author_id=None, created=None, title=None, body=None):
        self.author_id = author_id
        self.created = created
        self.title = title
        self.body = body

    def __repr__(self):
        return "<Post %r>" % (self.title)
