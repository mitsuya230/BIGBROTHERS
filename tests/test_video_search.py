import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver import WebDriverManager

class TestVideoSearch(unittest.TestCase):
    def setUp(self):
        self.driver_manager = WebDriverManager()
        self.driver_manager.initialize_driver()
        self.driver = self.driver_manager.get_driver()
        self.driver.get('https://rutube.ru/')

    def test_video_search(self):
        # Поиск видео по запросу
        search_box = self.driver.find_element(By.ID, "search-input")
        search_box.send_keys("тестовое видео")
        search_button = self.driver.find_element(By.XPATH, "//button[@class='search-button']")
        search_button.click()

        # Проверка наличия результатов поиска
        results = self.driver.find_elements(By.XPATH, "//div[@class='video-item']")
        self.assertGreater(len(results), 0, "Нет результатов поиска")

    def tearDown(self):
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()
