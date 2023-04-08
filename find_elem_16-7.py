# Заполняем 100 полей формы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    # Перебираем элементы в массиве
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    print(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()