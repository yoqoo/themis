import time

import pyautogui

url = "https://cec.org.cn/search/index.html?search={}"
site_name = "中国电力企业联合会"


def scrapy(company_name, driver, dest_path=None):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    driver.maximize_window()
    if dest_path is None:
        dest_path = "screenshot/{}_{}.png".format(company_name, site_name)
    pyautogui.screenshot(dest_path)


if __name__ == '__main__':
    from main import driver
    company_name = '测试公司1'
    scrapy(company_name, driver, "../screenshot/{}_{}.png".format(company_name, site_name))
    driver.quit()
