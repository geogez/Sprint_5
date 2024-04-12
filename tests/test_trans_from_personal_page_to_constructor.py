from locators import Locators
from data import *

class TestToConstructor:
    def test_trans_from_personal_page_to_constructor_using_constr_butn(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.constructor).click()
        check_text_bread = wd.find_element(*Locators.bread).text
        check_active_element = wd.find_element(*Locators.active_section).text
        assert check_text_bread == check_active_element


    def test_trans_from_personal_page_to_constructor_using_logo_butn(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.logo).click()
        check_text_bread = wd.find_element(*Locators.bread).text
        check_active_element = wd.find_element(*Locators.active_section).text
        assert check_text_bread == check_active_element
