from bs4 import BeautifulSoup as bsp
from selenium import webdriver
import config as cc

def tokenAbi(address, driver=None):
    try:
        filename = f'ABI_{address}.txt'
        with open(f"abi/{filename}") as f:
            abi = f.readlines()
            return abi[0]
    except IOError:
        abi = findAbi(address, driver)
        return abi


def findAbi(address, driver=None):
    url = f'https://bscscan.com/address/{address}#code'

    if not driver:
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--proxy-server=" + cc.PROXY)
        options.add_argument('--ignore-certificate-errors')
        # profile = webdriver.FirefoxProfile()
        # profile.accept_untrusted_certs=True
        driver = webdriver.Chrome(options=options)

    driver.get(url)
    page_soup = bsp(driver.page_source, features="lxml")
    abi = page_soup.find_all("pre", {"class": "wordwrap js-copytextarea2"})

    with open(f'abi/ABI_{address}.txt', 'w') as f:
        f.write(abi[0].text)

    driver.delete_all_cookies()
    driver.get("chrome://settings/clearBrowserData")
    # driver.close()
    return abi[0].text
