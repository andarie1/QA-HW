import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--window-size=1920,1080")
#    # options.add_argument("--headless")  фоновый режим
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
#     driver.get("http://uitestingplayground.com/textinput")
#     yield driver
#     driver.quit()
#
# def test_button(driver):
#     set_new_button_str = driver.find_element(By.ID, "newButtonName")
#     button = driver.find_element(By.ID, "updatingButton")
#     set_new_button_str.send_keys("ITCH")
#     button.click()
#     assert button.text == "ITCH"

# #########################################################################################
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
   # options.add_argument("--headless")  фоновый режим
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()

def test_img_box(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))
    third_img = wait.until(EC.presence_of_element_located((By.ID, "award")))
    assert third_img.is_displayed(), "Изображение не отображается!"

    img_src = third_img.get_attribute("src")
    assert "award.png" in img_src, f"Неправильный src: {img_src}"



