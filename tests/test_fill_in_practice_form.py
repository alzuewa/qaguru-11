import allure
from allure import severity_level

from models.data import user_data
from pages.registration_form_page import RegistrationPage

@allure.suite('Registration')
@allure.severity(severity_level=severity_level.BLOCKER)
@allure.tag('acceptance')
def test_fill_in_practice_form(setup_browser):
    registration_page = RegistrationPage()
    user = user_data.test_user

    registration_page.open_form()
    registration_page.register_user(user)
    registration_page.should_have_registered_user_with_data(user)
