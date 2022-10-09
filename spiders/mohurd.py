import time

import pyautogui

url = "https://www.mohurd.gov.cn/ess/?ty=a&query={}&ukl=&uka=&ukf={}&ukt=&sl=&ts=&te=&upg=1"
site_name = "中华人民共和国住房和城乡建设部"


def scrapy(company_name, driver, dest_path=None):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name, company_name))
    driver.maximize_window()
    driver.implicitly_wait(30)
    if dest_path is None:
        dest_path = "screenshot/{}_{}.png".format(company_name, site_name)
    pyautogui.screenshot(dest_path)


if __name__ == '__main__':
    from main import driver
    company_name = '测试公司1'
    scrapy(company_name, driver, "../screenshot/{}_{}.png".format(company_name, site_name))
    driver.quit()
