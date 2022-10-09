import time

import pyautogui

url = "https://s.lrn.cn/jsearchfront/search.do?websiteid=110000000000000&searchid=1&pg=20&p=1&tpl=13&cateid=1&total=25&q={}&pq=&oq=&eq=&dimension_module=&dimension_tag=&pos=&sortFields=&begin=&end="
site_name = "中华人民共和国自然资源部"


def scrapy(company_name, driver, dest_path=None):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
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
