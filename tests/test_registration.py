import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver import WebDriverManager

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver_manager = WebDriverManager()
        self.driver_manager.initialize_driver()
        self.driver = self.driver_manager.get_driver()
        self.driver.get('https://rutube.ru/')

    def test_registration(self):
        # Заполнение формы регистрации
        self.driver.find_element(By.ID, "email").send_keys("testuser@example.com")
        self.driver.find_element(By.ID, "password").send_keys("password123")
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        # Проверка успешной регистрации
        success_message = self.driver.find_element(By.XPATH, "//div[@class='success-message']")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()
