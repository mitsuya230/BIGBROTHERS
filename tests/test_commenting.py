import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver import WebDriverManager

class TestCommenting(unittest.TestCase):
    def setUp(self):
        self.driver_manager = WebDriverManager()
        self.driver_manager.initialize_driver()
        self.driver = self.driver_manager.get_driver()
        self.driver.get('https://rutube.ru/')

    def test_commenting(self):
        # Переход к видео
        self.driver.find_element(By.XPATH, "//a[@href='/video/123']").click()

        # Оставление комментария
        comment_box = self.driver.find_element(By.ID, "comment-input")
        comment_box.send_keys("Это тестовый комментарий.")
        submit_button = self.driver.find_element(By.XPATH, "//button[@class='submit-comment']")
        submit_button.click()

        # Проверка, что комментарий был добавлен
        comment_text = self.driver.find_element(By.XPATH, "//div[@class='comment-text']")
        self.assertTrue(comment_text.is_displayed())

    def tearDown(self):
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()
