import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Teste_Login():

    URL = "https://www.giulianaflores.com.br/login.aspx"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_com_sucesso(self):
        self.driver.get(self.URL)
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("july@qualy.com")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste123")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        self.driver.find_element(By.ID, "perfil-hidden").click()
        element_text = self.driver.find_element(By.ID, "lblWelcome").text
        assert "juliana" in element_text
        element_text = self.driver.find_element(By.ID, "pLogOut").click()