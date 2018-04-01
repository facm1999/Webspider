#导入相关库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pyquery import PyQuery as pq
import time

#打开浏览器
browser=webdriver.Chrome()
browser.get("http://www.taobao.com")

#定位元素
def search():
    element=WebDriverWait(browser,10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,"#q"))
    )
    global i
    i=input("the name of you want")
    element.send_keys(i)
    submit=WebDriverWait(browser,10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button"))
    )
    submit.click()
    html=browser.page_source
    return html

def next():
    submit = WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.next > a"))
    )
    submit.click()
    html=browser.page_source
    return html

def parse(html):
    doc=pq(html)
    items=doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product={
            'image':item.find('.pic .pic-link .img').attr('src'),
            'content':item.find('.pic .pic-link .img').attr('alt')
        }
        print(product)

def main():
    parse(search())
    for i in range(1,10):
        parse(next())
        time.sleep(3)

if __name__=='__main__':
    main()

