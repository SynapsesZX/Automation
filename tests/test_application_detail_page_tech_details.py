import time

import pytest

import conftest
from page_objects.developer_login import DevLogin
from page_objects.tech_details import ApplicationDetailPageTechDetail
from page_objects.developer_registration import DeveloperRegistration
from api.application_detail_page import ApiSetup
from page_objects.base_page import BasePage


class TestApplicationDetailPageTechDetails:

    def test_test(self, driver):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApiSetup(driver)
        app = user.get_app_id()
        user.open_link(
            f"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{app}")
        user = ApplicationDetailPageTechDetail(driver)
        user.click_edit_icon()
        user.select_mobile_native()
        user = ApiSetup(driver)
        time.sleep(10)
        user.delete_app(app)

    def test_test2(self, driver):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApiSetup(driver)
        app = user.change_app_status_to_in_progress()
        # app_id = user.get_app_id()
        user.open_link(
            f"https://qa-h360-marketplace.softservetest.com/developer/dashboard/application/{app}")
        time.sleep(10)
        user.delete_app(app)

    def test_test3(self, driver, api_setup_created_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()

        user = ApplicationDetailPageTechDetail(driver)

        user.proceed_to_the_application_detail_page_with_created_status(api_setup_created_status)
        user.click_edit_icon()
        user.select_version()
        user.select_mobile_native()
        user.select_patient_context()
        user.select_the_allergy_introlerance_scope()
        user.write_the_valid_url_to_the_smart_launch_url_field()
        user.write_the_valid_url_to_the_redirect_url_field()
        user.click_the_save_button()
        time.sleep(30)

    def test_app_with_created_status(self, driver, api_setup_with_in_progress_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_created_status(api_setup_with_in_progress_status)
        time.sleep(40)

    def test_app_with_in_review_status(self, driver, api_setup_with_in_review_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_in_review_status(api_setup_with_in_review_status)
        time.sleep(40)

    def test_app_with_approved_status(self, driver, api_setup_with_approved_status):
        user = DevLogin(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.dev_login()
        user = ApplicationDetailPageTechDetail(driver)
        user.proceed_to_the_application_with_approved_status(api_setup_with_approved_status)
        time.sleep(40)

    @pytest.mark.parametrize(('text'), [('Igor'), ('Semen')])
    def test_registration(self, driver, text):
        user = DeveloperRegistration(driver)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer/dashboard')
        user.click_the_start_now_button()
        user.write_data_in_the_email_input_field(text)
        time.sleep(4)
