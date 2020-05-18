from sqlalchemy import Column, Integer, String
from crawler.database.db import Base


class Url(Base):
    __tablename__ = 'urls'
    url_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
