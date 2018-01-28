import urllib.request

# python -m doctest -v app.py

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

# creates http request string with arguments num, min, max
def random_org_url(num, min, max):
    """
    >>> random_org_url(10, 1, 6)
    'https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new'
    """
    base_url = "https://www.random.org/integers"
    http_url = http_query(base_url, [("num", num), ("min", min), ("max", max), ("col", 1), ("base", 10), ("format", "plain"), ("rnd", "new")])

    return http_url

# calls get request of numbers with args num, min, max; returns list of random numbers
def get_random_numbers(num, min, max):
    url = random_org_url(num, min, max)
    response = http_get(url)

    if response[-1:] == b'\n':
        response = response[:-1]

    num_string = response.decode('UTF-8')

    return num_string.split("\n")

