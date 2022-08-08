import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://google.com";

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    browser.get(link);

    search_input = browser.find_element(By.NAME, 'q');
    search_input.send_keys("Hello, Google!");

    search_buttom = browser.find_element(By.NAME, 'btnK');
    search_buttom.click();

finally:
    time.sleep(30)
    browser.quit()
