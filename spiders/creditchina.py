import json
import random

import pyautogui
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.creditchina.gov.cn/xinyongxinxi/index.html?index=0&scenes=defaultScenario&tableName' \
      '=credit_xyzx_tyshxydm&searchState=2&entityType=1,2,4,5,6,7,8&keyword={}'
site_name = "信用中国"

def scrapy(company_name, driver):
    # Use a breakpoint in the code line below to debug your script.
    driver.get(url.format(company_name))
    try:
        element = driver.find_element('class name', 'company-item')
        date_msg = element.get_attribute("data-message")
        data_dict = json.loads(date_msg)
        #print(data_dict)
        download_report(data_dict['accurate_entity_name_query'], data_dict['uuid'], data_dict['accurate_entity_code'])
    except NoSuchElementException:
        print(f'查找不到对应信息')
    #print(driver.title)
    pyautogui.screenshot("screenshot/{}_{}.png".format(company_name, site_name))



def download_report(name, uuid, entity_code):
    pdf_url = 'https://public.creditchina.gov.cn/credit-check/pdf/download?companyName={}&entityType=1&uuid={}&tyshxydm={}'.format(
        name, uuid, entity_code)
    ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    down_res = requests.get(url=pdf_url, headers={'User-Agent': ua})
    filename = './{}.pdf'.format(name)
    with open(filename, 'wb') as file:
        file.write(down_res.content)


def search_report(name, uuid, entity_code):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })
    url = 'https://www.creditchina.gov.cn/xinyongxinxixiangqing/xyDetail.html?searchState=1&entityType=1&keyword' \
          '={}&uuid={}&tyshxydm={}'.format(name, uuid, entity_code)
    driver.get(url)
    driver.implicitly_wait(20)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
