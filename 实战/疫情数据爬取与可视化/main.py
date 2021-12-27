from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import pyecharts
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType  # 引入主题


def crawl():
    html = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
    chrome_driver = r'D:\anaconda\envs\pytry\Lib\site-packages\selenium\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.set_window_size(1000, 800)  # 设置窗口大小
    try:
        browser.get(html)

        """
        browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')
        括号里填的内容，如果有空格由 . 代替
        """

        buttons = browser.find_elements_by_class_name('Common_1-1-321_3lDRV2')  # 查找该按钮
        for button in buttons:
            button.click()
        # time.sleep(1)  # 停止两秒
        with open('source_page.html', 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)
        print('source_page 爬取完成')
    finally:
        browser.close()


def analyse():
    texts = []
    with open('source_page.html', 'r', encoding='utf-8')as fp:
        file = fp.read()
        soup1 = BeautifulSoup(file, 'lxml')
        soup = BeautifulSoup(soup1.prettify(), 'lxml')
        temp = soup.find_all(attrs={'class': 'VirusTable_1-1-321_3m6Ybq'})
        for th in temp:
            texts.append(th.text.replace('\n', ' ').split(' '))
        for text in texts:
            for i in range(text.count('')):
                text.remove('')

        return texts


def draw(texts):
    arr = np.array(texts)
    province = list(arr[:, 0])
    now_exits = list(arr[:, 2])
    data = [list(z) for z in zip(province, now_exits)]
    c = (
        Map(init_opts=opts.InitOpts(width="1000px", height="600px"))  # 初始化地图大小
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2021年12月25日疫情图"),  # 配置标题
            visualmap_opts=opts.VisualMapOpts(
                type_="scatter"  # 散点类型
            )
        )
            .add("now_exists", data, maptype="china")  # 将list传入，地图类型为中国地图
            .render("Map1.html")
    )
    print('请打开Map1.html')

    c = (
        Map(init_opts=opts.InitOpts(width="1000px",
                                    height="600px", theme=ThemeType.ESSOS))  # 可切换主题
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2021年12月25日疫情图"),
            visualmap_opts=opts.VisualMapOpts(
                # min_=0,
                # max_=600,
                range_text=['人数', ''],  # 分区间
                is_piecewise=True,  # 定义图例为分段型，默认为连续的图例
                pos_top="middle",  # 分段位置
                pos_left="left",
                orient="vertical",
                # split_number=10,  # 分成10个区间
                pieces=[
                    {"min": 1000},  # 不指定 max，表示 max 为无限大（Infinity）。
                    {"min": 500, "max": 999},
                    {"min": 100, "max": 499},
                    {"min": 50, "max": 99},
                    {"min": 10, "max": 49},
                    {"min": 5, "max": 9},
                    # {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'},  # 表示 value 等于 123 的情况
                    {"max": 4, "color": 'white'}  # 不指定 min，表示 min 为无限大（-Infinity）。
                ]

            )
        )
            .add("现存感染人数", data, maptype="china")
            .render("Map2.html")
    )
    print('请打开Map2.html')


if __name__ == '__main__':
    crawl()
    texts = analyse()
    draw(texts)
