from browser import Browser

#creeam metode pe care le vom putea folosi in orice pagina
class BasePage(Browser):

    def find(self,locator):
        return self.driver.find_element(*locator)

    # definim o metoda de tip type pentru scriere pe un input
    def type(self,locator,text):
        self.find(locator).send_keys(text)
        #gaseste locatorul si scrie textul

    #ia text de pe un element
    def get_text(self, locator):
        return self.find(locator).text

    #comparare daca URL e corect
    def is_url_correct(self,expected_url):
        return self.driver.current_url==expected_url
    #se poate utiliza acum assert is_url_correct in toate celelate pagini
