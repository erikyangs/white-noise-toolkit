import urllib.request

# returns http response from get
def http_get(url):
    return urllib.request.urlopen(url).read()

# returns string with GET args. expects args in format [(param, value), ...]
def http_query(base, args):
    """
    >>> http_query("https://google.com", [])
    'https://google.com/'
    >>> http_query("https://google.com", [("a", 1)])
    'https://google.com/?a=1'
    >>> http_query("https://google.com", [("a", 1), ("b", 2)])
    'https://google.com/?a=1&b=2'
    """
    http_string = base + "/"

    if len(args) > 0:
        http_string += "?"

    for i in range(len(args)):
        param = args[i][0]
        value = args[i][1]

        http_string += "{}={}".format(param, value)

        if i < len(args) - 1:
            http_string += "&"
    return http_string


def random_org(min, max, plain):
    pass