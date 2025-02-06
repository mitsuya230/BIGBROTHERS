import configparser

class Config:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_driver_path(self):
        return self.config['Settings']['driver_path']
    
    def get_url(self):
        return self.config['Settings']['url']
