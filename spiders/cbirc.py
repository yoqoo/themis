import time

import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

'''
    中国银行保险监督管理委员会
'''
url = 'http://www.cbirc.gov.cn/cn/view/pages/index/index.html'
site_name = "中国银行保险监督管理委员会"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url)
    driver.maximize_window()
    try:
        input_text = driver.find_element("xpath", '//*[@id="search"]')
        input_text.send_keys(company_name)
        search_btn = driver.find_element("xpath", '//*[@id="goJiansuo"]')
        ActionChains(driver).move_to_element(search_btn).click(search_btn).perform()
    except NoSuchElementException:
        print("没找到对应元素")
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))
