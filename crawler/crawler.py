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
            if UrlsGateway().check_for_existing(name=link) is None:
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
                            print(url)
                            if UrlsGateway().check_for_existing(name=url) is None:
                                try:
                                    r_in = requests.head(url, timeout=3)
                                    UrlsGateway().insert_url(name=r_in.url, server=r_in.headers["Server"], time_visit=datetime.now()) # noqa
                                except Exception:
                                    pass
                            else:
                                print('been here')
                        except Exception:
                            pass

    except Exception:
        pass


def inside_crawl():
    for links in UrlsGateway().get_urls():
        if links[4] == 0:
            print(links[4])
            request = None
            try:
                id_link = links[0]
                request = requests.get(links[1])
                soup = bs(request.content, 'html.parser')

                for link in soup.findAll('a'):

                    url = link.get('href')
                    if url:
                        urls_https = url.count('https://') > 0
                        urls_hhtp = url.count('http://') > 0
                        url_bg = url.count('.bg') > 0
                        normal_link = (url_bg and (urls_hhtp or urls_https))
                        if normal_link or url.count('https://register.start.bg'):
                            try:
                                print(url)
                                if Urls_Source_Gateway().check_for_existing(name=url) is None:
                                    try:
                                        r_in = requests.head(url, timeout=3)
                                        Urls_Source_Gateway().insert_url(name=r_in.url, server=r_in.headers["Server"], time_visit=datetime.now(), visited=True, parent_url=id_link) # noqa
                                    except Exception:
                                        # print(e)
                                        pass
                                else:
                                    print('been here')
                            except Exception:
                                pass

            except Exception:
                pass