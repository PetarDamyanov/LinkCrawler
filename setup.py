from crawler.database.db import *
from crawler.urls.modul import Url, Url_Source # noqa


def main():

    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
