from page_objects.base_page import BasePage
import locators.developer_registration
import pytest


class DeveloperRegistration(BasePage):

    def click_the_start_now_button(self):
        self.wait_and_click(*locators.developer_registration.START_NOW_BUTTON)

    def write_data_in_the_email_input_field(self, text):
        self.send_text_to_element(*locators.developer_registration.EMAIL_INPUT_FIELD, text=text)
        self.check_element_attribute(*locators.developer_registration.EMAIL_INPUT_FIELD, attribute='value',
                                     attribute_result=text)
