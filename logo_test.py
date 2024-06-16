from playwright.sync_api import sync_playwright

def test_logo_on_various_devices():
    devices = [
        {"name": "Desktop 1920x1080", "viewport": {"width": 1920, "height": 1080}},
        {"name": "Desktop 1366x768",  "viewport": {"width": 1366, "height": 768}},
        {"name": "iPhone 12",         "viewport": {"width": 390,  "height": 844},  "user_agent": "Mozilla/5.0 (iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},
        {"name": "Samsung Galaxy S21","viewport": {"width": 360,  "height": 800},  "user_agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36"}
        # Добавьте другие устройства и разрешения по необходимости
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)     


        # Эмуляция.
        for device in devices:
            context = browser.new_context(
                viewport=device["viewport"],  # Задает размеры экрана (ширину и высоту), эмулируя разрешение экрана устройства.
                user_agent=device.get("user_agent", "")  # Задает пользовательский агент браузера, который определяет, как сайт видит браузер и устройство.
            )

            page = context.new_page() # Открытие новой страницы в контексте браузера.
            page.goto("https://mastermann.ru")
            logo = page.query_selector('img[src="/catalog/view/theme/default/image/logo-w.svg"]')
            assert logo is not None, f"Логотип не найден на устройстве {device['name']}" # Проверка, что alt текст установлен и равен "Логотип". Если текст отличается, выдается сообщение об ошибке для конкретного устройства.

            alt_text = logo.get_attribute("alt")
            assert alt_text == "Логотип", f"Альт-текст для логотипа не установлен на устройстве {device['name']}"

            context.close()
        
        browser.close()

test_logo_on_various_devices()