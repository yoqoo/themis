import os
import time

from selenium import webdriver
import pyautogui

url = "https://www.mee.gov.cn/searchnew/?searchword={}"
site_name = "中华人民共和国生态环境部"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.maximize_window()
    driver.get(url.format(company_name))
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))



if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')
