from crawler.urls.modul import Url
from crawler.decorator.session import atomicmethods


@atomicmethods
class UrlsGateway:
    def __init__(self):
        self.url = Url

    def insert_url(self, session, *, name, server):
        try:
            session.add(Url(name=name, server=server))
        except Exception as e:
            return e

    def check_for_existing(self, session, *, name):
        return session.query(Url.name).filter(Url.name == name).first()

    def get_urls_server(self, session):
        return session.query(Url.name, Url.server).all()
