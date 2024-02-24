# import os
import allure
import pytest
from selene import browser

from model.pages.main_page import MainPage

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from utils import attach
# from dotenv import load_dotenv


# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()

BASE_URL = "https://amwine.ru"


@pytest.fixture(scope='function')
def setup_browser():
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "100.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )

    # browser.config.driver = driver
    browser.config.base_url = BASE_URL
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.timeout = 6.0

    yield browser

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def start(setup_browser):
    with allure.step("Открываем страницу магазина, подтверждаем возраст и город"):
        main_page = MainPage()
        main_page.open_with_years_and_city_confirmation()
