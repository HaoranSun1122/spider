import urllib.request, parse
import ssl


def test1():
    # urllib.request.urlopen('http://www.baidu.com')
    response = urllib.request.urlopen('https://www.baidu.com')
    print(response.read().decode('utf-8'))


def test2():
    url = 'https://biihu.cc//account/ajax/login_process/'
    headers = {
        # 假装自己是浏览器
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    dict = {
        'return_url': 'https://biihu.cc/',
        'user_name': 'xiaoshuaib@gmail.com',
        'password': '123456789',
        '_post_type': 'ajax',
    }
    data = bytes(parse.urlencode(dict), 'utf-8')
    req = request.Request(url, data=data, headers=headers, method='POST')
    response = request.urlopen(req, context=context)
    print(response.read().decode('utf-8'))


# test2()
