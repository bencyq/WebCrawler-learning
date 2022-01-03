from bs4 import BeautifulSoup


def del_word(file):
    words = ['收起工具时间不限','所有网页和文件','站点内检索','搜索工具百度为您找到相关结果约100,000,000个']


def analyse():
    for times in range(17):
        with open(f'source_page\\source_page-{times + 1}.html', 'r', encoding='utf-8') as fp:
            file = fp.read()
            soup = BeautifulSoup(file, 'lxml')

            soup.find(attrs={'class': 'cr-content new-pmd'}).clear()
            soup.find(attrs={'class': 's_tab'}).clear()
            # soup.find(attrs={'class': 's_former'}).clear()
            # soup.find(attrs={'class': 'tsn_inner_2vlfmrelative_5Vbw9'}).clear()
            soup.find(attrs={'class': 'foot-container_2X1Nt'}).clear()
            print(soup.text)
