from crawler.crawler import craw_url, inside_crawl
from crawler.draw import plot_links
from crawler.urls.url_gateway import UrlsGateway


def main():
    start = "https://register.start.bg"
    # craw_url(start)
    # inside_crawl()

    if UrlsGateway().get_urls_server():
        dict_urls = dict()
        for links in UrlsGateway().get_urls_server():
                dict_urls[links[0]] = links[1] # noqa
        print(dict_urls)
        plot_links(dict_urls)


if __name__ == '__main__':
    main()
