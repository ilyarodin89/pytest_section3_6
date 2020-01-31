# -*- coding: utf-8 -*-

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_basket(browser):
    #открываем ссылку в браузере
    browser.get(link)

    time.sleep(30)
    
    #используя явное ожидание, ждем появление кнопки на странице на случай долгой загрузки страницы
    button_add_basket = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 
        "button.btn.btn-lg.btn-primary.btn-add-to-basket")))

    #метод presence_of_element_located в переменную сохраняет сам элемент DOM, поэтому в проверке is not None
    assert button_add_basket is not None, "КНОПКА 'ДОБАВИТЬ В КОРЗИНУ' НА СТРАНИЦЕ НЕ НАЙДЕНА"


