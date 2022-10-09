import time

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

url = 'http://wzdig.pbc.gov.cn:8080/search/pcRender?pageId=fa445f64514c40c68b1c8ffe859c649e'

site_name = "中国人民银行"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    try:
        input_text = driver.find_element("xpath", '//*[@id="q"]')
        input_text.send_keys(company_name)
        search_btn = driver.find_element("xpath", '//*[@id="mySearchFormAction"]/div/input[2]')
        ActionChains(driver).move_to_element(search_btn).click(search_btn).perform()
    except NoSuchElementException:
        print("没找到对应元素")
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))

if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')
