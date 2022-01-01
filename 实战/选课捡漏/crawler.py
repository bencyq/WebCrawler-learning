import time
from selenium import webdriver
import numpy as np


def crawler(html):
    chrome_driver = r'D:\anaconda\envs\pytry\Lib\site-packages\selenium\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.set_window_size(1000, 800)  # 设置窗口大小
    try:
        browser.get(html)
        search_text_box = browser.find_element_by_class_name("form-control input-sm filter-input")
        search_text_box.send_keys(input('输入想选的课程'))
        search_button = browser.find_element_by_class_name('btn.btn-primary btn-sm')
        search_button.click()
        """
        browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')
        括号里填的内容，如果有空格由 . 代替
        """
        time.sleep(10)
    finally:
        browser.close()
    return './source_page.html'


if __name__ == '__main__':
    crawler('http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=19051509')