import urllib.request
import random
from PIL import Image

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
    response = b''

    # split up queries
    max_query_size = 10000
    while num > 0:
        if num >= max_query_size:
            url = random_org_url(max_query_size, min, max)
        else:
            url = random_org_url(num, min, max)
        response += http_get(url)
        num -= max_query_size

    if response[-1:] == b'\n':
        response = response[:-1]

    num_string = response.decode('UTF-8')
    num_string_list = num_string.split("\n")
    
    num_list = [int(num_string) for num_string in num_string_list]
    return num_list

# uses python's random library to generate random numbers to not use up bits on API
def get_test_random(num, min, max):
    return [random.randint(min, max) for _ in range(num)]

# converts one-dimensional list to list of len 3 tuples
def num_list_to_RGB_tuples(num_list):
    """
    >>> num_list_to_RGB_tuples([1,2,3,4,5,6])
    [(1, 2, 3), (4, 5, 6)]
    """
    if len(num_list) % 3 != 0:
        raise ValueError("List of numbers not divisible by 3 to make RGB 3-tuples")
    else:
        result = []
        i = 0
        while i < len(num_list):
            result.append((num_list[i], num_list[i+1], num_list[i+2]))
            i += 3
        return result

# generate RGB image of width w and height h using values from num_list
def generate_img(w, h, RGB_tuples):
    img = Image.new('RGB', (w, h))
    img.putdata(RGB_tuples)
    img.save('image.png')
    img.show()

def main():
    width = 128
    height = 128
    num_list = get_random_numbers(width * height * 3, 0, 255)
    RGB_list = num_list_to_RGB_tuples(num_list)
    generate_img(width, height, RGB_list)

if __name__ == '__main__':
    main()

