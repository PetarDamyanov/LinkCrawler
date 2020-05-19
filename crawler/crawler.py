from crawler.urls.url_gateway import UrlsGateway
from bs4 import BeautifulSoup as bs
import requests


def craw_url(url):
    request = None
    try:
        request = requests.get(url)
        soup = bs(request.content, 'html.parser')
        # urls_list = list()

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
                            # print("yay")
                        except Exception:
                            print("site broke")
                    else:
                        print("been here")

    except Exception:
        pass
'''
                contains_bg = url.count('.bg') > 0
                contains_hash = url.count('#') > 0
                js_stuff = url.count('javascript') > 0
                has_https = url.count('https://')
                if contains_bg and has_https:
                    if not contains_hash and not js_stuff:
                        urls_list.append(url)
                        try:
                            # pass
                            if UrlsGateway().check_for_existing(name=url) is None:
                                UrlsGateway().insert_url(name=url)
                                r_in = requests.get(url)
                                UrlsGateway().insert_url_server(server=r_in.get['Server'])
                                print(url)
                            else:
                                print('been here')
                        except Exception:
                            print('been here')
    except Exception:
        print('something wrong')
        return urls_list
'''

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
