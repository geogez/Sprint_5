import pytest
from selenium import webdriver

@pytest.fixture()
def wd():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(5)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()