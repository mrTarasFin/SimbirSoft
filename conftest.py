import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from settings import settings, WebDriverSettings


CHROME_BROWSER_NAME = 'Chrome'
FIREFOX_BROWSER_NAME = 'Firefox'
EDGE_BROWSER_NAME = 'Edge'

test_browsers = [CHROME_BROWSER_NAME, FIREFOX_BROWSER_NAME, EDGE_BROWSER_NAME]

browser_options = {
    CHROME_BROWSER_NAME: ChromeOptions,
    FIREFOX_BROWSER_NAME: FirefoxOptions,
    EDGE_BROWSER_NAME: EdgeOptions,
}


def get_options(browser: str) -> Options:
    options = browser_options[browser]()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--no-sandbox")
    options.set_capability('--platform', 'Linux')
    options.add_argument('--headless')
    return options


def get_driver(browser_name: str) -> WebDriverSettings:
    '''
    Создаем драйвер для выбранного браузера с сервера selenium
    :param browser_name: название браузера
    '''

    webdr = None
    try:
        webdr = WebDriverSettings(command_executer=settings.webdriver_host,
                                  options=get_options(browser_name),
                                  )
        webdr.browser_name = browser_name
    except WebDriverException as ex:
        pytest.exit(f'ERROR: {ex}')
    return webdr


@pytest.fixture()
def browser(request):
    '''Функция инициализирует работу WebDriver основные настройки для тестирования'''
    driver_service = Service(ChromeDriverManager().install())
    webdrv = webdriver.Chrome(service=driver_service)
    # webdrv = get_driver(request)
    request.addfinalizer(lambda *args: webdrv.quit())
    webdrv.maximize_window()
    return webdrv
