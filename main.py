from crawler.crawler import craw_url
from crawler.draw import plot_links
from crawler.urls.url_gateway import Urls_Source_Gateway


def main():
    start = "https://register.start.bg"
    craw_url(start)
    dict_urls = dict()
    for links in Urls_Source_Gateway().get_urls_server():
            dict_urls[links[0]] = links[1] # noqa
    print(dict_urls)
    plot_links(dict_urls)


if __name__ == '__main__':
    main()
