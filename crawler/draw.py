import matplotlib.pyplot as plt


def plot_links(dict_urls):
    keys = list(dict_urls.keys())
    values = list(dict_urls.values())

    X = list(range(len(keys)))

    plt.bar(X, list(values), align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram.png")
