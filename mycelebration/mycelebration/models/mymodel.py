from datetime import date
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(String(120), unique=True)
    password = Column(String(30))
    registered_holidays = relationship("Holiday")

    def __repr__(self):
        return self.name


class Holiday(Base):
    __tablename__ = 'holidays'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    date = Column(Date, default=date.today())
    user = Column(Integer, ForeignKey('users.id'), default=1)

    def __repr__(self):
        return self.name

Index('my_index', MyModel.name, unique=True, mysql_length=255)
