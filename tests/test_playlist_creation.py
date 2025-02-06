import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver import WebDriverManager

class TestPlaylistCreation(unittest.TestCase):
    def setUp(self):
        self.driver_manager = WebDriverManager()
        self.driver_manager.initialize_driver()
        self.driver = self.driver_manager.get_driver()
        self.driver.get('https://rutube.ru/')

    def test_playlist_creation(self):
        # Переход в раздел "Мои плейлисты"
        self.driver.find_element(By.XPATH, "//button[@class='my-playlists']").click()

        # Создание нового плейлиста
        self.driver.find_element(By.XPATH, "//button[@class='create-playlist']").click()
        playlist_name_field = self.driver.find_element(By.ID, "playlist-name")
        playlist_name_field.send_keys("Мой новый плейлист")
        self.driver.find_element(By.XPATH, "//button[@class='save-playlist']").click()

        # Проверка успешного создания плейлиста
        playlist_title = self.driver.find_element(By.XPATH, "//div[@class='playlist-title']")
        self.assertEqual(playlist_title.text, "Мой новый плейлист")

    def tearDown(self):
        self.driver_manager.quit_driver()

if __name__ == "__main__":
    unittest.main()
