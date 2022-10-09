import time

import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

'''
    上海证券交易所
'''

url = 'http://www.sse.com.cn/home/search/?webswd={}'

site_name = "上海证券交易所"

def scrapy(company_name, driver):
    driver.maximize_window()
    _scrapy_regulatory(company_name, driver)
    _scrapy_disposition(company_name, driver)


def _scrapy_regulatory(company_name, driver):
    driver.get(url.format(company_name))
    #driver.implicitly_wait(30)
    try:
        span = driver.find_element("xpath", '//*[@id="tab-switch0"]/span[6]')
        ActionChains(driver).move_to_element(span).click(span).perform()
        bondMeasures = driver.find_element("name", 'bondMeasures')
        time.sleep(3)
        ActionChains(driver).move_to_element(bondMeasures).click(bondMeasures).perform()
        time.sleep(2)
    except Exception:
        print("没找到对应元素")
        return
    # 向下滚动200个像素
    driver.execute_script('window.scrollBy(0,200)')
    pyautogui.screenshot("screenshot/{}_{}_1.png".format(company_name, site_name))


def _scrapy_disposition(company_name, driver):
    driver.get(url.format(company_name))
    #driver.implicitly_wait(30)
    try:
        span = driver.find_element("xpath", '//*[@id="tab-switch0"]/span[6]')
        ActionChains(driver).move_to_element(span).click(span).perform()
        bondMeasures = driver.find_element("name", 'disciplinary')
        time.sleep(3)
        ActionChains(driver).move_to_element(bondMeasures).click(bondMeasures).perform()
        time.sleep(2)
    except Exception:
        print("没找到对应元素")
        return
    # 向下滚动200个像素
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(2)
    pyautogui.screenshot("screenshot/{}_{}_2.png".format(company_name, site_name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrapy('杭州奥体博览中心建设投资有限公司')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
