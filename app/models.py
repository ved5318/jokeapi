from sqlalchemy import Boolean, Column, Integer, String, Text
from .database import Base

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    joke_type = Column(String(20))
    joke = Column(Text, nullable=True)
    setup = Column(Text, nullable=True)
    delivery = Column(Text, nullable=True)
    nsfw = Column(Boolean, default=False)
    political = Column(Boolean, default=False)
    sexist = Column(Boolean, default=False)
    safe = Column(Boolean, default=True)
    lang = Column(String(10))