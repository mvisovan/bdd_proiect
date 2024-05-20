# creat in afara folderelor pentru a putea instantia driverul
# gandit intr-un mod simplu
# logica driverului trebuie facuta intr-un fisier separat pentru o buna organizarea codului
# se declara
from selenium import webdriver

class Browser:
    # instantiez driverul
    driver = webdriver.Chrome()
    # maximizez fereastra
    driver.maximize_window()
    # pun un wait implicit de cateva secunde
    driver.implicitly_wait(3)

    # mai definesc metoda - close -  care inchide driverul

    def close(self):
        self.driver.close()
