import time

import pyautogui

url = "http://yan.bcpcn.com/website/xyjl.jsp?keyword={}&searchtype=1&page=1"
site_name = "盐业信用管理与公共服务平台"


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
