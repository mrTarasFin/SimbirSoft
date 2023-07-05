import datetime
from selenium.webdriver.common.keys import Keys
import time
from page.BaseApp import BasePage
from locators.locator_form import PageLocators as locators


class FormPage(BasePage):

    def click_plus(self):
        self.find_element(locators.LOCATOR_BUTTON_PLUS).click()

    def click_minus(self):
        self.find_element(locators.LOCATOR_BUTTON_MINUS).click()

    def input_field(self):
        '''Функция отрабатывает поле ввода на странице'''
        self.find_element(locators.LOCATOR_INPUT_FIELD).click()
        return self.find_element(locators.LOCATOR_INPUT_FIELD)

    def enter_digit(self, digit):
        '''Функция вводит количество в поле ввода'''
        self.input_field().send_keys(digit)
        time.sleep(2)

    def login(self):
        self.find_element(locators.LOCATOR_LOGIN).click()

    def login_user(self):
        self.find_element(locators.LOCATOR_BUTTON_LOGIN).click()

    def find_user(self):
        self.find_element(locators.LOCATOR_FIELD_USER).click()
        self.find_element(locators.LOCATOR_HARRY_POTTER).click()
        self.find_element(locators.LOCATOR_FIELD_USER).click()

    def fibonacci(self, num: int) -> int:
        if num in (1, 2):
            return 1
        return self.fibonacci(num-1) + self.fibonacci(num-2)

    def button_deposit(self):
        self.find_element(locators.LOCATOR_DEPOSIT).click()
        num = datetime.datetime.now().day + 1
        self.enter_digit(self.fibonacci(num))

    def button_withdrawl(self):
        self.find_element(locators.LOCATOR_WITHDRAWL).click()
        time.sleep(5)
        self.enter_digit(self.check_balance())

    def check_balance(self):
        balance = self.find_element(locators.LOCATOR_BALANCE).text
        if int(balance) != 0:
            return int(balance)
        else:
            return 0

    @staticmethod
    def save_file(list_trans: list) -> None:
        try:
            with open("report.csv", 'a') as file:
                for el in list_trans:
                    file.write(el)
        except IOError as ex:
            print(f'При записи файла произошла ошибка {ex}')

    def button_transaction(self):
        self.find_element(locators.LOCATOR_TRANSACTION).click()
        value = self.find_elements(locators.LOCATOR_TABLE_TRANSACTION)
        list_trans = []
        for item in value:
            list_trans.append(item.text)
        return list_trans
