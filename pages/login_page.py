from selenium.webdriver.common.by import By

from pages.base_page import BasePage


#dupa ce s-au definit metodele se poate analiza pagina de login
#incep sa definesc locatorii

class LoginPage(BasePage):
    LOGIN_PAGE_URL= "https://www.fonduri-structurale.ro/contul-meu/inregistrare"
    INPUT_EMAIL = (By.ID,"username")
    INPUT_PASSWORD =(By.ID, "password")
    BUTTON_LOGIN =(By.CLASS_NAME, "btn-primary")
    ERROR_MESSAGE = (By.CLASS_NAME, "panel-title")

    # definim metodele
    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)
    #metoda care deschide pagina

    def set_email(self, text):
        self.type(self.INPUT_EMAIL,text)
    #metoda definita pentru a scrie pe elemente este type
    #se scrie locatorul pe care vrem sa scriu si apoi textul pe care vreau sa il scriu
    #metoda care introduce emailul
    # parametrizam pentru a putea refolosi metoda

    def set_password(self,text):
        self.type(self.INPUT_PASSWORD,text)
    # metoda definita pentru a scrie pe elemente este type
    # se scrie locatorul pe care vrem sa scriu si apoi textul pe care vreau sa il scriu
    # metoda care introduce parola
    # parametrizam pentru a putea refolosi metoda

    def click_button_register(self):
        self.find(self.BUTTON_LOGIN).click()
    # metoda definita pentru a scrie pe elemente este find
    # apasa butonul de logare

    def is_main_error_message_displaid(self):
        return self.find(self.ERROR_MESSAGE).is_displayed()
    # returneaza True sau False functie de mesajul afisat
    # metoda definita pentru a scrie pe elemente este find
    # apasa butonul de logare

    def main_error_message_contains_text(self, text):
        return text in self.get_text(self.ERROR_MESSAGE)