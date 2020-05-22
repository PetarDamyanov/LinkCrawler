from crawler.crawler import craw_url, craw_inside
from crawler.draw import plot_links
from crawler.urls.url_gateway import UrlsGateway


def main():
    start = "https://register.start.bg"
    craw_url(start)
    # craw_inside('http://www.ibg.bg/')

    # if UrlsGateway().get_urls_server():
    #     dict_urls = dict()
    #     for links in UrlsGateway().get_urls_server():
    #             dict_urls[links[0]] = links[1] # noqa
    #     print(dict_urls)
    #     plot_links(dict_urls)


if __name__ == '__main__':
    main()
