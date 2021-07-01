from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html" # or selects2.html
    browser = webdriver.Chrome()
    browser.get(link)

    n1t = browser.find_element_by_id('num1')
    n1  = int(n1t.text)
    n2t = browser.find_element_by_id('num2')
    n2  = int(n2t.text)
#    print(n1, n2)
    sr  = str(n1+n2)
#    print(sr)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(sr)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
