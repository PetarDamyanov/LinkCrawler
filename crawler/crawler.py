from crawler.urls.url_gateway import UrlsGateway
from bs4 import BeautifulSoup as bs
import requests


def craw_url(url):
    request = None
    try:
        request = requests.get(url)
        soup = bs(request.content, 'html.parser')

        for link in soup.findAll('a'):
            url = link.get('href')
            if url:
                if url.count('link.php') > 0:
                    url = f'https://register.start.bg/{url}'
                if url.count('https://register.start.bg') > 0:
                    # print(url)
                    if UrlsGateway().check_for_existing(name=url) is None:
                        try:
                            r_in = requests.get(url, timeout=3)
                            print(r_in.url)
                            try:
                                UrlsGateway().insert_url(name=r_in.url, server=r_in.headers["Server"])
                            except Exception as e:
                                print(e)
                        except Exception:
                            print("site broke")
                    else:
                        print("been here")

    except Exception:
        pass

'''
Used before
def crawler_recursion(url, visited):

    if visited is None:
        visited = list()

    if url is not None:
        visited.append(url)
        if craw_url(url):
            for link in craw_url(url):
                if link not in visited:
                    result = crawler_recursion(link, visited)
                    if result is not None:
                        # print(result)
                        return result
'''
