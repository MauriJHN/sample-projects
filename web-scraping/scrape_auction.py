import json
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.bondroberts.com/product/view/17988/Quai_d'Orsay_No._50_2020_Semi_bo%C3%AEte_nature_box_of_10_cigars."
CHROME_WEBDRIVER_PATH = 'C:\\Users\\mhern\\development\\sample-projects\\chromedriver_win32\\chromedriver.exe'

def __write_page_source_to_file(browser:webdriver.Chrome) -> None:
    with open('page_source.html', 'w') as file:
        source = browser.page_source.encode('ascii', errors='replace')
        file.write(source.decode())


def _get_credentials() -> tuple:
    username = input("username:")
    password = getpass("password:")
    return (username, password)


def login(browser:webdriver.Chrome) -> None:
    # TODO: if needed, find login xpaths
    username_xpath = 'tbd'
    password_xpath = 'tbd'
    login_xpath = 'tbd'
    username_el = wait_and_get(browser, 5, username_xpath)
    password_el = wait_and_get(browser, 5, password_xpath)
    login_el = wait_and_get(browser, 5, login_xpath)

    if None in (username_el, password_el, login_el):
        print("Login failed, exiting")
        exit(1)

    username_el.clear()
    password_el.clear()
    username, password = _get_credentials()
    username_el.send_keys(username)
    password_el.send_keys(password)
    login_el.click()
    print('Successfully logged in!')
    

def wait_and_get(browser:webdriver.Chrome, seconds:int, selector:str, by:str = By.XPATH) -> WebElement:
    time.sleep(seconds)
    element = None

    try:
        element = browser.find_element(by, selector)
    except:
        print(f'Could not find element with selector:{selector}')
    finally:
        return element
    return element


def parse_extra_info(extra_info_text: str) -> dict:
    extra_info_list = extra_info_text.split('\n')
    extra_info_data = {}

    for i in range(0, len(extra_info_list), 2):
        extra_info_data[extra_info_list[i-1]] = extra_info_list[i]

    return extra_info_data


def scrape_data(browser:webdriver.Chrome):
    title_xpath = '/html/body/div[7]/div[1]/div/div[2]/h1'
    auction_window_xpath = '/html/body/div[7]/div[1]/div/div[2]/h3'
    price_xpath = '/html/body/div[7]/div[1]/div/div[2]/div[1]/span'
    extra_info_box_xpath = '/html/body/div[7]/div[1]/div/div[2]/div[7]'

    title_element = wait_and_get(browser, 2, title_xpath)
    auction_window_element = wait_and_get(browser, 2, auction_window_xpath)
    price_element = wait_and_get(browser, 2, price_xpath)
    extra_info_box_element = wait_and_get(browser, 2, extra_info_box_xpath)

    info = {
        "Title": title_element.text,
        "Auction Window": auction_window_element.text,
        "Current Auction Price": price_element.text,
        "Extra Info Box": parse_extra_info(extra_info_box_element.text)
    }

    print(json.dumps(info, indent=4))


def main() -> None:
    ## Setup chrome options
    chrome_options = Options()
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--headless')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(CHROME_WEBDRIVER_PATH)

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.implicitly_wait(5)
    browser.get(URL)
    scrape_data(browser)
    url_list = [
        'https://www.bondroberts.com/product/view/18101/Bol%C3%ADvar%20Belicosos%20Finos',
        'https://www.bondroberts.com/product/view/18092/Ram%C3%B3n%20Allones%20Gigantes',
        'https://www.bondroberts.com/product/view/18112/La%20Gloria%20Cubana%20Inmensos'
    ]

    for u in url_list:
        browser.get(u)
        scrape_data(browser)
        time.sleep(5)

    time.sleep(10)
    browser.close()


if __name__ == '__main__':
    main()