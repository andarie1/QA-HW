from time import sleep

import pytest
from selenium import webdriver
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
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_display_logo(driver):
    """ICH-logo"""
    ich_logo = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221710153310155 > a > img')
    sleep(5)
    assert ich_logo.is_displayed(), "Логотип ITCareerHub не найден или не отображается!"


def test_program_logo(driver):
    """Ссылка “Программы”"""
    logo_program = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221709552454448 > a')
    assert logo_program.is_displayed(), "Элемент не найден или не отображается."


def test_payment(driver):
    """Ссылка “Способы оплаты”"""
    payment_element = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221709552445907 > a')
    assert payment_element.is_displayed(), "Элемент не найден или не отображается."


def test_news(driver):
    """Ссылка “Новости”"""
    news_element = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221709552475577 > a')
    assert news_element.is_displayed(), "Элемент не найден или не отображается."


def test_about_us(driver):
    """Ссылка “О нас”"""
    about_us = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221709552503050 > a')
    assert about_us.is_displayed(), "Элемент не найден или не отображается."


def test_reviews(driver):
    """Ссылка “Отзывы”"""
    reviews_element = driver.find_element(By.CSS_SELECTOR, '#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221709552523895 > a')
    assert reviews_element.is_displayed(), "Элемент не найден или не отображается."

def test_de_language(driver):
    """DE_LANGUAGE_CHECK"""
    driver.get("https://itcareerhub.de")
    de_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'de')]"))
    )
    assert de_icon.is_displayed(), "Иконка смены языка на немецкий не найдена!"


def test_ru_language(driver):
    """RU_LANGUAGE_CHECK"""
    ru_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/ru')]"))
    )
    assert ru_icon.is_displayed(), "Иконка смены языка на русский не найдена!"


def test_telephone_icon_extended(driver):
    """ Проверка клика по иконке телефона и отображения сообщения о неудачном звонке """
    telephone_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="molecule-171015335126584580"]/div[2]/a/img'))
    )
    assert telephone_icon.is_displayed(), "Иконка телефона не найдена!"
    telephone_icon.click()

    failed_call_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rec767956167"]/div/div/div[4]/div'))
    )
    assert failed_call_msg.is_displayed(), "Текст о неудачном звонке не отображается!"



