from sqlalchemy import ForeignKey, BOOLEAN, Column, Integer, String, DateTime
from crawler.database.db import Base
from sqlalchemy.orm import relationship


class Url(Base):
    __tablename__ = 'urls'
    url_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    server = Column(String)
    time_visit = Column(DateTime)
    visited = Column(BOOLEAN, default=False)


class Url_Source(Base):
    __tablename__ = 'urls_source'
    url__source_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    server = Column(String)
    time_visit = Column(DateTime)
    visited = Column(BOOLEAN)
    parent_url = Column(Integer, ForeignKey(Url.url_id))
    parent = relationship(Url, backref='urls_source')
