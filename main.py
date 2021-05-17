import urllib.request



# urllib.request.urlopen('http://www.baidu.com')
response = urllib.request.urlopen('https://www.baidu.com')
print(response.read().decode('utf-8'))