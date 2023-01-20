from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SingletonChromeBrowser(object):
    __instance = None
    driver = None

    def __new__(cls, *args, **kwargs):
        if not SingletonChromeBrowser.__instance:
            SingletonChromeBrowser.__instance = object.__new__(cls)
        return SingletonChromeBrowser.__instance

    def __init__(self, options=['--start-maximized', '--disable-gpu', '--no-sandbox']):
        if self.driver is None:
            chrome_options = webdriver.ChromeOptions()

            if options is not None:
                for option in options:
                    chrome_options.add_argument(option)

            chrome_driver_path = Path(__file__).parent.parent / 'drivers' / 'chromedriver.exe'
            chrome_service = Service(executable_path=chrome_driver_path)
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

    def quit(self):
        self.driver.quit()
