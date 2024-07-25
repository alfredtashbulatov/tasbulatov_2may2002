import pytest
import allure
from selenium import webdriver
from user_api import Api
from main_page import Main_Page as MP


@allure.title("Фикстура URL для API-тестов")
@pytest.fixture(scope="session")
def api():
    return Api("https://www.sibdar-spb.ru")

@allure.title("Фикстура для Браузера для Ui-тестов")
@pytest.fixture
def driver():
    with allure.step("Записать в переменную {browser},\
                     браузер 'Microsoft Edge'"):
        browser = webdriver.Edge()
    with allure.step("Задать ожидание браузера"):
        browser.implicitly_wait(6)
    with allure.step("Задать размеры окна браузера"):
        browser.set_window_size(800, 1100)
    with allure.step("Задать расположение браузера"):
        browser.set_window_position(800,10)

    with allure.step("Записать в переменную {driver1},\
                     браузер 'Microsoft Edge'"):
        driver1 = webdriver.Edge()
    with allure.step("Открыть в браузере каленьдарь"):
        driver1.get("https://www.bing.com/search?q=%D0%BA%D0%B0%D0%BB%D0%B5%D0%BD%D0%B4%D0%B0%D1%80%D1%8C&filters=ufn%3a%22%D0%9A%D0%B0%D0%BB%D0%B5%D0%BD%D0%B4%D0%B0%D1%80%D1%8C%22+sid%3a%22316631a4-ccc4-75f1-60c6-759a07349cb3%22&asbe=SC&form=WNSGPH&qs=MB&cvid=2a3738cc83f7484d9c3338043ccd4ec5&pq=rfktyml&cc=RU&setlang=ru-RU&nclid=A6E5F7AF8A42AD540AC0CFA130BB0DC5&ts=1721855881221&wsso=Moderate")
    with allure.step("Задать размеры окна браузера"):
        driver1.set_window_size(800, 1100)
    with allure.step("Задать расположение браузера"):
        driver1.set_window_position(10,10)

    with allure.step("Вернуть браузер"):
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
