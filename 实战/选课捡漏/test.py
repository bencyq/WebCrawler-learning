import requests


def requests_form():
    url = 'http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=19051509'
    data = {'k1': 'v1', 'k2': 'v2'}
    response = requests.post(url, data)
    return response


if __name__ == "__main__":
    response1 = requests_form()

    print("From形式提交POST请求：")
    print(response1.text)
