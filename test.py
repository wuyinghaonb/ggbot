import requests

url = 'https://www.google.com'
response = requests.get(url)

if response.status_code == 200:
    print('123')
else:
    print('请求失败，状态码：', response.status_code)