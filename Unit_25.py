from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicity_wait(10)  # неявные ожидания


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('zavan@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zavan1978')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_class_name('navbar-toggler-icon').click()
    pytest.driver.find_element_by_xpath('//*[contains(text(), "Мои питомцы")]').click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))  # явные ожидания

    descriptions = pytest.driver.find_element_by_xpath('//*[@id="all_my_pets"]/table/tbody')
    images = pytest.driver.find_element_by_xpath('//*[id="all_my_pets"]//img')
    names = pytest.driver.find_element_by_xpath('//*[@id="all_my_pets"]//body/tr/td[0]')
    statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]/text[1]')
    f = filter(str.isdecimal, statistics)
    statistics_2 = "".join(f)

    for i in range(len(names)):
        assert statistics_2 == len(descriptions)  # Присутствуют все питомцы
        assert statistics_2 == len(images)  # Хотя бы у половины питомцев есть фото
        assert statistics_2 == len(names)  # У всех питомцев есть имя, возраст и порода
        assert element != 1
