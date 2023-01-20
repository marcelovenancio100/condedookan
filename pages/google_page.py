from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.chrome_browser import SingletonChromeBrowser


class GooglePageLocator(object):
    INPUT_SEARCH = '[name="q"]'
    BUTTON_SEARCH = '.FPdoLc [name="btnK"]'
    TITLE_RESULT = '[data-attrid="title"]'


class GooglePage(SingletonChromeBrowser):
    def get_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        self.driver.get(url)

    def send_keys_input_pesquisa(self):
        input_pesquisa = self.get_element(GooglePageLocator.INPUT_SEARCH)
        input_pesquisa.send_keys('Python')

    def click_button_pesquisar(self):
        button = self.get_element(GooglePageLocator.BUTTON_SEARCH)
        button.click()

    def get_text_title_resultado(self):
        element = self.get_element(GooglePageLocator.TITLE_RESULT)
        return element.text
