import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_success(driver):
    wait = WebDriverWait(driver, 20)
    actions = ActionChains(driver)

    # Переключаемся в iframe перед поиском элементов
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    paragraph = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.lead:nth-child(2)")))
    actions.move_to_element(paragraph).perform()
    expected_text = "semper posuere integer et senectus justo curabitur."
    assert expected_text in paragraph.text, f"Ожидали '{expected_text}', но получили '{paragraph.text}'"




