from crawler.urls.url_gateway import UrlsGateway, Urls_Source_Gateway
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


def craw_url(url):
    request = None
    try:
        request = requests.get(url)
        soup = bs(request.content, 'html.parser')
        for link in soup.findAll('a'):
            url = link.get('href')

            if url:

                urls_https = url.count('https://') > 0
                urls_hhtp = url.count('http://') > 0
                url_bg = url.count('.bg') > 0
                normal_link = (url_bg and (urls_hhtp or urls_https))

                if url.count('.php') == 0 and url_bg:
                    num = url.find('.bg')
                    num += 3
                    url = url[:num:]

                if url.count('link.php') > 0:
                    url = f'https://register.start.bg/{url}'

                if normal_link or url.count('https://register.start.bg'):
                    try:

                        if UrlsGateway().check_for_existing(name=url) is None:
                            # print(url)
                            try:
                                r_in = requests.head(url, timeout=3)
                                UrlsGateway().insert_url(name=r_in.url, server=r_in.headers["Server"], time_visit=datetime.now(), visited=False) # noqa
                                print(r_in.url)
                                try:
                                    craw_inside(r_in.url)

                                except Exception:
                                    pass

                            except Exception:
                                pass

                        elif UrlsGateway().url_visited(url) is False:
                            craw_inside(url)

                    except Exception:
                        pass

    except Exception:
        pass


def craw_inside(url):

    if UrlsGateway().url_visited(url) is False:

        UrlsGateway().url_visited_true(url)
        request = requests.get(url)
        soup = bs(request.content, 'html.parser')
        id_link = UrlsGateway().get_id(url)

        for link in soup.findAll('a'):

            url = link.get('href')

            if url:

                urls_https = url.count('https://') > 0
                urls_hhtp = url.count('http://') > 0
                url_bg = url.count('.bg') > 0
                normal_link = (url_bg and (urls_hhtp or urls_https))

                if normal_link or url.count('https://register.start.bg'):
                    try:
                        r_in = requests.head(url, timeout=3)
                        Urls_Source_Gateway().insert_url(name=r_in.url, server=r_in.headers["Server"], time_visit=datetime.now(), visited=True, parent_url=id_link) # noqa

                        print(r_in.url)
                    except Exception:
                        pass
                else:
                    print('been here')
