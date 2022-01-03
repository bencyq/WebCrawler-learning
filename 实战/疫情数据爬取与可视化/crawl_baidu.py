from selenium import webdriver
import time


def crawl():
    html = 'https://www.baidu.com/s?wd='
    chrome_driver = r'D:\anaconda\envs\pytry\Lib\site-packages\selenium\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.set_window_size(1000, 800)  # 设置窗口大小
    try:
        browser.get(html + '疫情')
        # search_text = browser.find_element_by_class_name('s_ipt')
        # search_text.send_keys('疫情')
        # time.sleep(3)
        # search_button = browser.find_element_by_class_name("btn_wr s_btn_wr bg")
        # search_button = browser.find_element_by_xpath('//*[@id="s_btn_wr"]')
        # search_button.click()
        for times in range(17):
            time.sleep(1)
            with open(f'source_page\\source_page-{times + 1}.html', 'w', encoding='utf-8') as fp:
                fp.write(browser.page_source)
                print(f'source_page-{times + 1}.html is downloaded')
            eles = browser.find_elements_by_class_name('n')  # 找到该按钮
            ele = eles[-1]
            browser.execute_script("arguments[0].scrollIntoView();", ele)  # 滚动至该按钮可见位置
            ele.click()

    finally:
        browser.close()


crawl()
