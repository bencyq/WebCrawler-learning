from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException


def crawler():
    html = 'https://cas.hdu.edu.cn/cas/login?service=https%3A%2F%2Fi.hdu.edu.cn%2Ftp_up%2F'
    # chrome_driver = 'chromedriver.exe'
    # option = webdriver.ChromeOptions()
    # # option.add_argument('--headless')
    # # option.add_argument("--disable-gpu")
    # option.add_experimental_option('excludeSwitches', ['enable_automation'])
    # browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
    # browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": '''
    #             Object.defineProperty(navigator, 'webdriver', {
    #               get: () => undefined
    #             })
    #           '''
    # })
    # browser = webdriver.Chrome(executable_path=chrome_driver)
    browser = webdriver.Firefox(executable_path='geckodriver.exe')
    browser.set_window_size(1500, 800)  # 设置窗口大小
    try:
        browser.get(html)
        time.sleep(2)
        while True:
            flag = input('请自行登录网站至自主选课界面，并在完成操作后输入1\n')
            if flag == '1':
                break
            else:
                print('输入错误，请重新输入')
        time.sleep(3)
        windows = browser.window_handles
        browser.switch_to.window(windows[-1])
        search_text = browser.find_element_by_name('searchInput')

        class_name = input('请输入教学班级：\n')
        search_text.send_keys(class_name)
        search_button = browser.find_element_by_name('query')

        search_button.click()
        class_type = input('请输入课程类型（主修、通识、体育、特殊）\n')
        class_check = browser.find_element_by_id('nav_tab')
        eles = class_check.find_elements_by_tag_name('li')
        # class_check = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/div/div[2]/div[1]/div[2]')
        for ele in eles:
            if class_type in ele.text:
                ele.click()
        print('已找到课程，准备开始捡漏Orz')
        # select_button = browser.find_elements_by_class_name('btn.btn-primary.btn-sm')[-1]
        while True:
            time.sleep(0.5)
            browser.find_elements_by_class_name('btn.btn-primary.btn-sm')[-1].click()
            time.sleep(0.2)
            while True:
                try:
                    time.sleep(0.3)
                    if '退选' not in browser.find_element_by_class_name('panel-body.table-responsive').text:
                        browser.find_element_by_id('btn_ok').click()
                    else:
                        print('选课成功！！！')
                    break
                except NoSuchElementException as e:
                    continue

        """
        browser.find_element_by_class_name('li-page.iconfont.icon-icon_pagedown')
        括号里填的内容，如果有空格由 . 代替
        """

        time.sleep(10)
    # except Exception:
    #     print(Exception)
    #     print('程序出错！\n可能是由于尝试次数过多被暂时封IP，或者其他网络问题\n请检查网络重试，或者等待一会再试')
    finally:
        browser.close()


if __name__ == '__main__':
    crawler()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('程序已退出！')
    os.system('pause')
