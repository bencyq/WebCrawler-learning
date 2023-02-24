import time
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np


def crawler(html):
    chrome_driver = r'D:\anaconda\envs\pytry\Lib\site-packages\selenium\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.set_window_size(1000, 800)
    try:
        browser.get(html)
        time.sleep(1)
        button = browser.find_element_by_id('importance')
        button.click()
        time.sleep(1)
        with open('source_page_1.html', 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)
        eles = browser.find_elements_by_class_name('page')
        eles[1].click()
        time.sleep(1)
        with open('source_page_2.html', 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)

    finally:
        browser.close()
    return


def analyse(file):
    soup1 = BeautifulSoup(file, 'lxml')
    soup = BeautifulSoup(soup1.prettify(), 'lxml')
    lis = soup.find_all(attrs={'class': 'live-item'})
    text = []
    for l in lis:
        text.append(l.text[:-203].replace('\n', '').replace(' ', '') + '\n')
    return text


if __name__ == '__main__':
    html = 'https://wallstreetcn.com/live/global'
    crawler(html)
    with open('source_page_1.html', 'r', encoding='utf-8') as fp:
        file1 = fp.read()
    with open('source_page_2.html', 'r', encoding='utf-8') as fp:
        file2 = fp.read()
    with open('text.txt', 'w', encoding='utf-8') as fp:
        fp.writelines(analyse(file1))
        fp.writelines(analyse(file2))
