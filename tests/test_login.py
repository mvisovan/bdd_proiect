import unittest

from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def test_error_login(self):
    #cream login page si importam din login_pages_clasa cereata acolo LoginPage
        login_page = LoginPage()
    #acum putem folosi din login_page
        login_page.open()
        login_page.set_email("mvisovan@gmail.com")
        login_page.set_password("123456789")
        login_page.click_button_register()
        assert login_page.is_main_error_message_displaid(), "Error message is not displayed?"
