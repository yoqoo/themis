import time

import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

'''
    深圳证券交易所
'''
measure_url = "http://www.szse.cn/disclosure/bond/measure/index.html"
punish_url = "http://www.szse.cn/disclosure/bond/punish/index.html"

site_name = "深圳证券交易所"

def scrapy(company_name, driver):
    _scrapy_measure(company_name, driver)
    _scrapy_punish(company_name, driver)

def _scrapy_measure(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(measure_url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    try:
        input_text = driver.find_element("xpath",'//*[@id="ZQ_JGCS_tab1_txtGjz"]')
        input_text.send_keys(company_name)
        search_btn = driver.find_element("xpath",'/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[4]/button')
        ActionChains(driver).move_to_element(search_btn).click(search_btn).perform()
        time.sleep(3)
    except NoSuchElementException:
        print("没找到对应元素")
    # 向下滚动200个像素
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)
    pyautogui.screenshot("screenshot/{}_{}_1.png".format(company_name, site_name))


def _scrapy_punish(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(punish_url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    try:
        input_text = driver.find_element("xpath",'//*[@id="ZQ_JLCF_tab1_txtGjz"]')
        input_text.send_keys(company_name)
        search_btn = driver.find_element("xpath",'/html/body/div[5]/div/div[2]/div/div/div[2]/div/div[4]/button')
        ActionChains(driver).move_to_element(search_btn).click(search_btn).perform()
        time.sleep(3)
    except NoSuchElementException:
        print("没找到对应元素")
    # 向下滚动200个像素
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)
    pyautogui.screenshot("screenshot/{}_{}_2.png".format(company_name, site_name))


if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')
