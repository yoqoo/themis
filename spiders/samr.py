import time

import pyautogui

url = "https://www.samr.gov.cn/search4/s?searchWord={}&x=0&y=0&column=%E5%85%A8%E9%83%A8&siteCode=bm30000012"
site_name = "国家市场监督管理总局"


def scrapy(company_name, driver, dest_path=None):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    driver.maximize_window()
    if dest_path is None:
        dest_path = "screenshot/{}_{}.png".format(company_name, site_name)

    time.sleep(3000)
    pyautogui.screenshot(dest_path)


if __name__ == '__main__':
    from main import driver
    company_name = '测试公司1'
    scrapy(company_name, driver, "../screenshot/{}_{}.png".format(company_name, site_name))
    driver.quit()
