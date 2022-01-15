from selenium import webdriver

browser = webdriver.Firefox(executable_path='geckodriver.exe')
html = 'https://cas.hdu.edu.cn/cas/login?service=https%3A%2F%2Fi.hdu.edu.cn%2Ftp_up%2F'
browser.get(html)