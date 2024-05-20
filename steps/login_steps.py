from behave import *

# * se importa tot din librarie

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()
#verificam in login_page metoda pe care am scris-o - metoda open

@then('The URL is  "https://www.fonduri-structurale.ro/contul-meu/inregistrare"')
#utilizam ca metoda aceeasi definire pentru ca libraria behave doar asa o recunoaste
def step_impl(context):
    assert context.login_page.is_url_correct("https://www.fonduri-structurale.ro/contul-meu/inregistrare"), "LOGIN"
#mosteneste din base_page compararea URL si apelez din logimn _page metoda is url correct
#introducem URL care ma astept sa fie

@when('I enter "mvisovan@gmail.com" in the email input')
def step_impl(context):
   context.login_page.set_email("mvisovan@gmail.com")

@when('I enter "123456" in the password input')
def step_impl(context):
    context.login_page.set_password("123456789")

@when('I click login button')
def step_impl(context):
    context.login_page.click_button_register()

@then('I should see the red message "Ești înregistrat?"')
def step_impl(context):
    assert context.login_page.is_main_error_message_displaid(), "Error mesage not displayed"
    #assert context.login_page.main_error_message_contains_text("Ești înregistrat?"), ("Error message is not contain expected text")
