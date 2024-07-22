# tasbulatov_2may2002

## Тестирование интернет-магазина "Дикий сбор"

## ШАГИ
1. Склонировать проект https://github.com/alfredtashbulatov/tasbulatov_2may2002.git

2. Установить зависимости

4. Запустить тесты с указанием пути к директории результатов тестирования pytest pytest --alluredir allure-result

5. Сформировать отчет allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- allure

### Структура 
- api (ветка с тестами и методами api)
 - conftest.py - Файл с фикстурами 
 - user_api.py - Методы для Аpi тестов
 - test_api.py - api тесты

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure
- pip install json

### Запуск тестов 
- pytest (Запуск всех тестов )
- pytest - m api (Запуск api тестов )

