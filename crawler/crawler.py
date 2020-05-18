from crawler.links.url_gateway import UrlsGateway
from bs4 import BeautifulSoup as bs
import requests


def craw_url(url):
    request = requests.get(url)
    soup = bs(request.content, 'html.parser')
    urls_list = list()
    for link in soup.findAll('a'):
        url = link.get('href')
        if url:
            contains_bg = url.count('.bg') > 0
            contains_hash = url.count('#') > 0
            js_stuff = url.count('javascript') > 0
            has_hhtps = url.count('https://')
            if contains_bg and has_hhtps:
                if not contains_hash and not js_stuff:
                    urls_list.append(url)
                    try:
                        # pass
                        print(url)
                        if UrlsGateway().check_for_existing(name=url) is None:
                            UrlsGateway().insert_url(name=url)
                    except Exception as e:
                        print('been here')
                        pass
    return urls_list


def crawler_recursion(url):
    for link in craw_url(url):
        # if link != url:
        if UrlsGateway().check_for_existing(name=link) is not None:
            # print(link)
            result = crawler_recursion(link)
            if result is not None:
                # print(result)
                return result
