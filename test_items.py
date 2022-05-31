import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "http://google.com"

def test_in_different_languages(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "Нет кнопки add-to-basket"
    #страница товара на сайте содержит кнопку добавления в корзину
    # В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. Есть assert.
    #pytest --language=fr -s test_items.py