"""
本文档采用selenium库模拟浏览器爬取数据
酷我的排行榜采用的是js渲染的方法，所以不能通过设置offset来切换页面
所以我选择了模拟点击，找到下一页的按钮，并模拟点击九次，获得10个网页源代码
并采用BeautifulSoup解析代码，通过 findall函数快速找到节点
最终用pandas生成excel表格并输出
"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd


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
        # input = browser.find_element_by_id('kw')  模拟窗口输入
        # input.send_keys('Python')
        # input.send_keys(Keys.ENTER)
        # wait = WebDriverWait(browser, 10)
        # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        # print(browser.current_url)
        # print(browser.get_cookies())
        # print(browser.page_source)
        eles = browser.find_elements_by_class_name('page-wrap')  # 找到该按钮
        ele = eles[0]
        ele_x = ele.location.get('x')
        ele_y = ele.location.get('y')
        browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置

        # 废案：采用了x、y轴点击的方式模拟点击
        # for i in range(2):  # 循环点击下一页，获取排行榜三百个数据
        #     # browser.execute_script('window.scrollBy(0,200)')  # 向下滚动200个像素
        #     browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置
        #     print(ele_x, ele_y)
        #     time.sleep(1)
        #     click_locxy(browser, ele_x + 500, 20)
        #     # ActionChains(browser).move_by_offset(770, 20).click().perform()  # 鼠标左键点击， 200为x坐标， 100为y坐标
        #     # ActionChains(browser).move_by_offset(-770, -20).perform()  # 将鼠标位置恢复到移动前
        #     time.sleep(1)
        # for i in range(6):  # 循环点击下一页，获取排行榜三百个数据
        #     # browser.execute_script('window.scrollBy(0,200)')  # 向下滚动200个像素
        #     browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置
        #     print(ele_x, ele_y)
        #     time.sleep(1)
        #     click_locxy(browser, ele_x + 530, 20, left_click=True)
        #     # ActionChains(browser).move_by_offset(770, 20).click().perform()  # 鼠标左键点击， 200为x坐标， 100为y坐标
        #     # ActionChains(browser).move_by_offset(-770, -20).perform()  # 将鼠标位置恢复到移动前
        #     time.sleep(1)
        with open('./source_page_1.html', 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)
        print('源文件 {} 爬取完成'.format(1))
        """
        browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')
        括号里填的内容，如果有空格由 . 代替
        """
        for i in range(9):
            browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置，要不然无法模拟点击
            button = browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')  # 查找该按钮
            # ActionChains(browser).move_to_element_with_offset(button, 500, 10).click().perform()
            button.click()
            time.sleep(2)  # 停止两秒
            with open('./source_page_{}.html'.format(i + 2), 'w', encoding='utf-8') as fp:
                fp.write(browser.page_source)
            print('源文件 {} 爬取完成'.format(i + 2))
    finally:
        browser.close()
    return './source_page.html'


def seeking_ranking_list():
    names = []
    artists = []
    albums = []
    num = 1
    index = 1
    for i in range(1, 11):
        print(index, '--------------')
        with open('./source_page_{}.html'.format(i), 'r', encoding='utf-8')as fp:
            file = fp.read()
        soup = BeautifulSoup(file, 'lxml')
        song_name = soup.find_all(attrs={'class': 'song_name flex_c'})
        song_album = soup.find_all(attrs={'class': 'song_album'})
        song_artist = soup.find_all(attrs={'class': 'song_artist'})
        for name, artist, album in zip(song_name, song_artist, song_album):
            names.append(name.a['title'])
            artists.append(artist.span['title'])
            albums.append(album.span['title'])
            print(num, name.a['title'], artist.span['title'], album.span['title'])
            num = num + 1
        index += 1
    df = pd.DataFrame([i for i in range(1, 300)])
    df.columns = ['排名']
    df.insert(1, '歌曲', names)
    df.insert(2, '艺术家', artists)
    df.insert(3, '专辑', albums)
    print(df)
    df.to_excel('排名表.xlsx', index=None)


if __name__ == '__main__':
    crawler('http://www.kuwo.cn/rankList')
    seeking_ranking_list()
