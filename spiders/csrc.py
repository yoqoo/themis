import time

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

'''
    中国证券监督管理委员会
'''
url = 'http://www.csrc.gov.cn/guestweb4/s?searchWord={}&' \
      'column=%25E5%2585%25A8%25E9%2583%25A8&' \
      'pageSize=10&pageNum=0&' \
      'siteCode=bm56000001&' \
      'sonSiteCode=&checkHandle=1&searchSource=1&' \
      'govWorkBean=%257B%257D&sonSiteCode=&' \
      'areaSearchFlag=-1&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&manualWord=123&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0'
site_name = "中国证券监督管理委员会"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    driver.maximize_window()
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')
