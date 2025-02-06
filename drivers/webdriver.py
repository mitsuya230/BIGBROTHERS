from selenium import webdriver
from config.config import Config

class WebDriverManager:
    def __init__(self):
        self.config = Config('config/config.ini')
        self.driver = None

    def initialize_driver(self):
        driver_path = self.config.get_driver_path()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Запуск в фоновом режиме
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
