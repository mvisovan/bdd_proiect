from browser import Browser
from pages.login_page import LoginPage


# cream metoda  si definim functia utilizeand nume metoda si context
def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()


# se creaza o variabila pentru pagina de login pentru a putea accesa din Login Page metode

def after_all(context):
    context.browser.close()
# metoda face close
