import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    # iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))

    # появления изображений
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))
    assert images, "Нет изображений для перетаскивания"

    source = images[0]  # первое изображение
    target = driver.find_element(By.ID, "trash")  # Корзина

    # drag_and_drop
    actions.drag_and_drop(source, target).perform()

    # Проверяем, что 1 картинка исчезла
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery > li")) < len(images))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery > li")) == len(images) - 1






