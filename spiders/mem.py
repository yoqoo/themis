import time

from selenium import webdriver

url = "https://www.mem.gov.cn/was5/web/sousuo/index.html?sw={}&date1=&date2=&stype=0"
site_name = "中华人民共和国应急管理部"

def scrapy(company_name, driver):
    driver.get(url.format(company_name))
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.save_screenshot("screenshot/{}_{}.png".format(company_name, site_name))

if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')
