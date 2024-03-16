import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Teste_Cadastro():

    url = "https://www.giulianaflores.com.br/"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.faker = Faker()

    def teardown_method(self, method):
        self.driver.quit()

    def gerar_cpf(self):
        num = [random.randint(0, 9) for x in range(9)]
        num_str = ''.join(str(x) for x in num)
        return f'{num_str[:3]}.{num_str[3:6]}.{num_str[6:9]}-00'

    def test_cadastro(self):
        nome_fake = self.faker.name()
        cpf_fake = self.gerar_cpf()
        email_fake = self.faker.email()

        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "pLogIn").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_ibtNewCustomer").text == "Criar cadastro"
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys(nome_fake)
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys(cpf_fake)
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email_fake)
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("Teste123")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("08346-380")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("123")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("1198425-1234")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        self.driver.find_element(By.ID, "perfil-hidden").click()
     
       
       
