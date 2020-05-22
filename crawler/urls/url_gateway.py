from crawler.urls.modul import Url, Url_Source
from crawler.decorator.session import atomicmethods
from sqlalchemy import func


@atomicmethods
class UrlsGateway:
    def __init__(self):
        self.url = Url

    def insert_url(self, session, *, name, server, time_visit, visited):
        try:
            session.add(Url(name=name, server=server, time_visit=time_visit, visited=visited))
        except Exception as e:
            return e

    def check_for_existing(self, session, *, name):
        return session.query(Url.name).filter(Url.name.like(f'%{name}%')).first()

    def get_urls(self, session):
        return session.query(Url.url_id, Url.name, Url.server, Url.time_visit, Url.visited).all()

    def get_urls_server(self, session):
        return session.query(func.count(Url.server), Url.server).group_by(Url.server).all()

    def url_visited(self, session, name):
        return session.query(Url.visited).filter(Url.name == name).first()[0]

    def get_id(self, session, name):
        return session.query(Url.url_id).filter(Url.name == name).first()[0]
    
    def url_visited_true(self, session, url):
        try:
            session.query(Url).filter(Url.name == url).update({'visited': True})
        except Exception as e:
            raise e


@atomicmethods
class Urls_Source_Gateway:
    def __init__(self):
        self.url = Url_Source

    def insert_url(self, session, *, name, server, time_visit, visited, parent_url):
        try:
            session.add(Url_Source(name=name, server=server, time_visit=time_visit, visited=visited, parent_url=parent_url)) # noqa
        except Exception as e:
            return e

    def check_for_existing(self, session, *, name):
        return session.query(Url_Source.name).filter(Url_Source.name == name).first()

    def get_urls_server(self, session):
        return session.query(func.count(Url_Source.server), Url_Source.server).group_by(Url_Source.server).all()
