import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

# NOTE: api documentation can be found in https://www.selenium.dev/selenium/docs/api/py/index.html
# NOTE: to download the chrome webdriver make sure the url below is the one you need based on docs:
#       https://chromedriver.chromium.org/downloads
# curl -OL https://chromedriver.storage.googleapis.com/110.0.5481.77/chromedriver_linux64.zip
URL = 'https://www.instagram.com/'
CHROME_WEBDRIVER_PATH = 'C:\\Users\\mhern\\development\\sample-projects\\chromedriver_win32\\chromedriver.exe'
FOLLOW_BUTTON_XPATH = "//*[starts-with(@id,'mount_0_0_')]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div/div/div[1]/button/div/div"


def __write_page_source_to_file(browser: webdriver.Chrome):
    with open('page_source.html', 'w') as file:
        source = browser.page_source.encode('ascii', errors='replace')
        file.write(source.decode())


def _get_credentials() -> tuple:
    username = input("username: ")
    password = getpass("password: ")
    return (username, password)


def login(browser: webdriver.Chrome) -> None:
    # find the input elements for user and password
    # prompt users for credentials
    # click on login
    username_xpath = '#loginForm > div > div:nth-child(1) > div > label > input'
    password_xpath = '#loginForm > div > div:nth-child(2) > div > label > input'
    login_xpath = '#loginForm > div > div:nth-child(3) > button'
    username_el = _find_input(browser, username_xpath)
    password_el = _find_input(browser, password_xpath)
    login_el = _find_input(browser, login_xpath)

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


def _find_input(browser: webdriver.Chrome, selector: str) -> WebElement:
    element = None
    try:
        element = browser.find_element(By.CSS_SELECTOR, selector)
    except:
        print(f'Could not find element with selector: {selector}')
    finally:
        return element


def get_list_of_account_urls():
    account_urls = []
    with open('account_urls.txt', 'r') as file:
        account_urls = file.readlines()
    return account_urls


def follow_accounts(browser: webdriver.Chrome, account_urls: list):
    for url in account_urls:
        print(f'Following {url}')
        browser.get(url)
        try:
            element = wait_and_get(browser, 5, By.XPATH, FOLLOW_BUTTON_XPATH)
            if 'following' not in element.text.lower():
                element.click()
            else:
                print(f'Already following {url}')
        except NoSuchElementException as e:
            print(f"Could not find follow button for account {url}, skipping")

    

def wait_and_get(browser: webdriver.Chrome, seconds: int, by: str, selector: str):
    time.sleep(seconds)
    element = browser.find_element(by, selector)
    return element


def main() -> None:
    ## Setup chrome options
    chrome_options = Options()
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--headless')

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(CHROME_WEBDRIVER_PATH)

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.get(URL)
    
    browser.implicitly_wait(5)

    login(browser)
    time.sleep(5)
    follow_accounts(browser, get_list_of_account_urls())

    time.sleep(10)
    browser.close()


if __name__ == '__main__':
    main()