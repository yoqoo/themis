import time

import pyautogui
from selenium import webdriver

'''
    中华人民共和国工业和信息化部
'''

url = "https://www.miit.gov.cn/search/index.html?websiteid=110000000000000&pg=&" \
      "p=&tpl=&category=&q={}&jsflIndexSeleted="
site_name = "中华人民共和国工业和信息化部"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    driver.maximize_window()
    driver.implicitly_wait(30)
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))


if __name__ == '__main__':
    from main import driver
    scrapy('杭州奥体博览中心建设投资有限公司', driver)
