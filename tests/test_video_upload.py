import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver import WebDriverManager

class TestVideoUpload(unittest.TestCase):
    def setUp(self):
        self.driver_manager = WebDriverManager()
        self.driver_manager.initialize_driver()
        self.driver = self.driver_manager.get_driver()
        self.driver.get('https://rutube.ru/')

    def test_video_upload(self):
        # Переход к форме загрузки видео
        upload_button = self.driver.find_element(By.XPATH, "//button[@class='upload-button']")
        upload_button.click()

        # Заполнение формы загрузки видео
        file_input = self.driver.find_element(By.ID, "file-upload-input")
        file_input.send_keys("/path/to/test-video.mp4")
        self.driver.find_element(By.XPATH, "//button[@class='submit-upload']").click()

        # Проверка успешной загрузки
        success_message = self.driver.find_element(By.XPATH, "//div[@class='upload-success']")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()
