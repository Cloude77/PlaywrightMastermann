import pytest
import time
from playwright.sync_api import sync_playwright

def test_open_main_page():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=False)
        
        # Создаем новый браузерный контекст
        context = browser.new_context()

        # Открытие новой страницы
        page = context.new_page()

        # Установление таймаута ожидания по умолчанию для всех действий на странице
        page.set_default_timeout(15000)

        # Переход на главную страницу
        page.goto("https://mastermann.ru/")

        # Проверка успешной загрузки главной страницы
        assert page.title() == "Монтажные термошкафы Mastermann. Официальный сайт производителя"

        # Ожидание 5 секунд перед закрытием браузера
        page.wait_for_timeout(5000)

        # Закрытие браузера
        browser.close()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])