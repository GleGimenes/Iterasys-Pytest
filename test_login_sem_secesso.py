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

    def test_login_sem_sucesso(self):
        self.driver.get(self.URL)
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("joaogilberto@qualidade.com")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste123")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        assert self.driver.find_element(By.ID, "ContentSite_divMessages").text == "ATENÇÃO - e-mail ou senha inválidos!"