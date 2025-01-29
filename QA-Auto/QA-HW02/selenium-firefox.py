from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Написать скрипт, который:
# Открывает в браузере Firefox https://itcareerhub.de/ru
# Переходит в раздел “Способы оплаты”
# Делает скриншот этой секции страницы


# Запуск браузера
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://itcareerhub.de/ru")

# Явное ожидание появления ссылки
wait = WebDriverWait(driver, 10)
payment_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты")))
payment_link.click()

# Ожидание загрузки секции и закрытие окна cookies
cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Подтвердить']")))
cookies_button.click()

# Скриншот секции "Способы оплаты"
payment_section = wait.until(EC.presence_of_element_located((By.ID, "rec717852307")))
payment_section.screenshot("./payment_types.png")

driver.quit()
