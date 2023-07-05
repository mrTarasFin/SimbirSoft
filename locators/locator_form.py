from selenium.webdriver.common.by import By


class PageLocators:
    """В данном классе определены основные локаторы для поиска объектов на странице согласно задания"""

    LOCATOR_BUTTON_LOGIN = (By.XPATH, '/html/body/div/div/div[2]/div/form/button')
    LOCATOR_HARRY_POTTER = (By.XPATH, '//*[@id="userSelect"]/option[3]')
    LOCATOR_FIELD_USER = (By.XPATH, '//*[@id="userSelect"]')
    LOCATOR_LOGIN = (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]')
    LOCATOR_TRANSACTION = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]')
    LOCATOR_DEPOSIT = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]')
    LOCATOR_WITHDRAWL = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[3]')
    LOCATOR_INPUT_FIELD = (By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    LOCATOR_BUTTON_PLUS = (By.XPATH, '//*[text() = "Deposit"]')
    LOCATOR_BUTTON_MINUS = (By.XPATH, '//*[text() = "Withdraw"]')
    LOCATOR_BALANCE = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]')
    LOCATOR_TABLE_TRANSACTION = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/table/tbody')
