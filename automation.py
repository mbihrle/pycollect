from selenium import webdriver
from selenium.webdriver.common.by import By


def selenium_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_browser = webdriver.Chrome(options=options)
    # chrome_browser = webdriver.Chrome()

    # print(chrome_browser)
    chrome_browser.maximize_window()
    # chrome_browser.get("https://www.seleniumeasy.com/test")
    chrome_browser.get('http://www.python.org')
    # chrome_browser.get(
    # "https://www.google.com/search?q=translate+google&rlz=1C1ONGR_deDE927DE927&oq=translate+google&aqs=chrome..69i57j69i65.5798j0j9&sourceid=chrome&ie=UTF-8")

    print(chrome_browser.title)
    # assert 'Welcome to Python.org' in chrome_browser.title
    btn_go = chrome_browser.find_element(By.ID, 'submit')
    print(btn_go.get_attribute('innerHTML'))
    searchfield = chrome_browser.find_element(By.ID, 'id-search-field')
    searchfield.clear()
    searchfield.send_keys('test selenium')

    btn_go.click()

    # chrome_browser.close()


if __name__ == '__main__':
    selenium_test()
