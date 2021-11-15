"""
UA伪装(UA:User-Agent 为请求载体的身份标识)
门户网站会通过UA来检测是一个浏览器还是一段爬虫程序在请求，所以要进行UA伪装
具体的方法是通过网页的NetWork找到Headers的User-Agent
"""
import requests

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
    }
    url = 'http://www.sogou.com/web?query='
    keyword = input('enter a word:')
    param = {
        'query': keyword
    }
    response = requests.get(url, param, headers=headers)
    page_text = response.text
    print(page_text)
    with open('./02 {}.html'.format(keyword), 'w', encoding='utf-8') as fp:
        fp.write(page_text)
