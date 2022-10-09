import time

import pyautogui
from selenium.webdriver import ActionChains

url = "http://search.mof.gov.cn/was5/web/search"
url = "http://www.mof.gov.cn/index.htm"
site_name = "中华人民共和国财政部"


def scrapy(company_name, driver, dest_path=None):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    driver.maximize_window()
    driver.implicitly_wait(30)
    input1 = driver.find_element("xpath", '//*[@id="andsen"]')
    driver.implicitly_wait(30)
    input1.send_keys(company_name)
    #radio_1 = driver.find_element("xpath", "/html/body/div[3]/div[1]/form/div[1]/label[4]/input")
    #ActionChains(driver).move_to_element(radio_1).click(radio_1).perform()
    time.sleep(30)
    return
    if dest_path is None:
        dest_path = "screenshot/{}_{}.png".format(company_name, site_name)
    pyautogui.screenshot(dest_path)


if __name__ == '__main__':
    from main import driver
    company_name = '测试公司1'
    scrapy(company_name, driver, "../screenshot/{}_{}.png".format(company_name, site_name))
    driver.quit()
