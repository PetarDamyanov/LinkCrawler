from crawler.database.db import *
from crawler.urls.modul import Url # noqa


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
