import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


def click_locxy(dr, x, y, left_click=True):
    '''
    dr:浏览器
    x:页面x坐标
    y:页面y坐标
    left_click:True为鼠标左键点击，否则为右键点击
    '''
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
        ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
        ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前


def crawler(html):
    chrome_driver = r'D:\anaconda\envs\pytry\Lib\site-packages\selenium\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.set_window_size(1000, 800)  # 设置窗口大小
    try:
        browser.get(html)
        eles = browser.find_elements_by_class_name('prev')  # 找到该按钮
        ele = eles[0]
        ele_x = ele.location.get('x')
        ele_y = ele.location.get('y')
        browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置

        with open('./source_page_1.html', 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)
        print('源文件 {} 爬取完成'.format(1))
        """
        browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')
        括号里填的内容，如果有空格由 . 代替
        """
        for i in range(365):
            # browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置，要不然无法模拟点击
            button = browser.find_element_by_class_name('prev')  # 查找该按钮
            # ActionChains(browser).move_to_element_with_offset(button, 500, 10).click().perform()
            button.click()
            time.sleep(1)  # 停止两秒
            with open('./source_page_{}.html'.format(i + 2), 'w', encoding='utf-8') as fp:
                fp.write(browser.page_source)
            print('源文件 {} 爬取完成'.format(i + 2))
    finally:
        browser.close()
    return './source_page.html'


def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    result = result.replace('和', '').replace('的', '').replace('图片', '').replace('谈', '').replace('月', '').replace('以',
                                                                                                                  '')

    return result


def analyse():
    text = []
    for i in range(1, 367):
        print(f'\r第{i}页解析中。。。', end='')
        with open('./source_page_{}.html'.format(i), 'r', encoding='utf-8')as fp:
            file = fp.read()
        soup = BeautifulSoup(file, 'lxml')
        temp = soup.find_all(attrs={'class': 'news-list'})
        for th in temp:
            for t in th.find_all('a'):
                text.append(t.text)
    with open('a.txt', 'w') as fp:
        for t in text:
            fp.write(t)
            fp.write('\n')


def draw():
    with open("a.txt") as fp:
        text = fp.read()
        text = trans_CN(text)
        mask = np.array(image.open("pic.png"))
        wordcloud = WordCloud(
            mask=mask,
            font_path="C:\\Windows\\Fonts\\simhei.ttf"
        ).generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()
        image_produce.save('result.png')


if __name__ == '__main__':
    # crawler('http://paper.people.com.cn/rmrb/html/2021-12/21/nbs.D110000renmrb_01.htm')
    # analyse()
    draw()
