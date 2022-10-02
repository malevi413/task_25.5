import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element('id', 'email').send_keys('gazov6ik@gmail.com')
    # Вводим пароль
    pytest.driver.find_element('id', 'pass').send_keys('Ard@tov13pe')
    # Нажимаем на кнопку входа в аккаунт

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )

    pytest.driver.find_element('xpath', "//button[@type='submit']").click()
    # Проверяем, что мы оказались на главной странице пользователя

    pytest.driver.implicitly_wait(10)  # seconds
    myDynamicElement = pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'


    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
