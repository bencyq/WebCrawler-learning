import requests

texts = []
with open('config.txt') as fp:
    _ = fp.readline()
    while True:
        text = fp.readline()
        texts.append(text)
        if text == '':
            texts.pop(-1)
            break
print(texts)
headers = {text.split(':')[0]: text.split(':')[1].strip('\n') for text in texts}
headers['Sec-Fetch-Mode'] = 'cors'
print(headers)
data = 'jxb_ids=2d5bb85684c9d793bbbfb162aa7b9fe9d51ee92ec65300df98d027343ea3a33d72e84ed976768906279a03c955d56165939104572635b91cdbe5c91c4ba7478ff548f87507ed9c5e23628ab8e7b490337e9f4c3c6cb438295257a3d0d7470976a4afd467e9a984a8afdce08862fc08a70db128d7fb74ef9d4d3ab647c925ec19&kch_id=A0507150&kcmc=(A0507150)%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86%EF%BC%88%E4%B9%99%EF%BC%89+-+4+%E5%AD%A6%E5%88%86&rwlx=1&rlkz=0&rlzlkz=1&sxbj=1&xxkbj=0&qz=0&cxbj=0&xkkz_id=D3CA48E77A1C4CD8E0536164A8C05380&njdm_id=2019&zyh_id=0523&kklxdm=01&xklc=2&xkxnm=2021&xkxqm=12'
url = 'http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=19051509'
data = requests.post(url, data=data)
with open('a.html', 'w') as f:
    f.write(data.text)
print(data.text)
print(data.url)
