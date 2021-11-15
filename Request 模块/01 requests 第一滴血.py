"""
基本流程：
1.指定url
2.发起请求
3.获取响应数据
4.存储
"""

import requests

if __name__ == '__main__':
    url = 'http://www.sogou.com'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    with open('./01.html', 'w', encoding='utf-8')as fp:
        fp.write(page_text)
