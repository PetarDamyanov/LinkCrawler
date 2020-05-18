from crawler.links.modul import Url
from crawler.decorator.session import atomicmethods


@atomicmethods
class UrlsGateway:
    def __init__(self):
        self.url = Url

    def insert_url(self, session, *, name):
        try:
            session.add(Url(name=name))
            return name
        except Exception as e:
            return e

    def check_for_existing(self, session, *, name):
        return session.query(Url.name).filter(Url.name == name).first()
