from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[1]/input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[2]/input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//div[@class='first_block']/div[3]/input[@placeholder='Input your email']")
    input3.send_keys("test@test.ru")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    time.sleep(3)

    # Получаем из найденного элемента get_text_page сам текст с помощью метода .text
    text_page = browser.find_element(By.CLASS_NAME, 'container').text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == text_page

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
