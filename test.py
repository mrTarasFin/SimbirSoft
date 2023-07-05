import time
import allure
import pytest
from page.page_form import FormPage


@allure.epic('End-to-end test suit')
@allure.feature('Selenium')
@allure.story('Test selenium grid is alive')
@pytest.mark.test_one
def test_one_part(browser):
    site = FormPage(browser)
    site.open_site()
    site.login()
    site.find_user()
    site.login_user()
    site.button_deposit()
    site.click_plus()
    assert site.check_balance() != 0, 'Баланс не пополнен'
    site.button_withdrawl()
    site.click_minus()
    assert site.check_balance() == 0, 'Баланс не обнулен'
    site.save_file(site.button_transaction())


    time.sleep(5)
