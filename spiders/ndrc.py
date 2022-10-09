import time

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

'''
中华人民共和国发展和改革委
https://www.ndrc.gov.cn/
'''

url = "https://so.ndrc.gov.cn/s?siteCode=bm04000007&tab=all&toolsStatus=1"
site_name = "中华人民共和国发展和改革委"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url)
    driver.implicitly_wait(10)
    try:
        search_element = driver.find_element("xpath",'//*[@id="qt"]')
        search_element.send_keys(company_name)
        search_btn = driver.find_element("xpath",'//*[@id="searchBtn"]')
        driver.execute_script("arguments[0].click();", search_btn)
    except NoSuchElementException:
        print("查找不到元素")
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
