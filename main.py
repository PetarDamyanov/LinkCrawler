from crawler.crawler import crawler_recursion


def main():
    start = "https://register.start.bg"
    # print(crawler_recursion(start))
    crawler_recursion(start, visited=None)


if __name__ == '__main__':
    main()
