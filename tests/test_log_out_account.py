from locators import Locators
from data import *

class TestExitAccount:
    def test_log_out_account(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.exit_button).click()
        check_text_enter = wd.find_element(*Locators.text_enter).text
        assert check_text_enter == 'Вход'
