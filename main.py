from crawler.crawler import crawler_recursion, craw_url
from crawler.draw import plot_links
from crawler.urls.url_gateway import UrlsGateway



def main():
    start = "https://register.start.bg"
    # print(crawler_recursion(start))
    # crawler_recursion(start, visited=None)
    if UrlsGateway().get_urls_server():
        dict_urls = dict()
        for links in UrlsGateway().get_urls_server():
            # print(links)
                dict_urls[links[0]] = links[1]
        # print(dict_urls)
        plot_links(dict_urls)
    else:
        craw_url(start)




if __name__ == '__main__':
    main()
