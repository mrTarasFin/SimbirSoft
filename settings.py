from selenium.webdriver.remote.webdriver import WebDriver as WD


class Settings:
    webdriver_host = 'http://localhost:4444/wd/hub'


class WebDriverSettings(WD):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


settings = Settings()
