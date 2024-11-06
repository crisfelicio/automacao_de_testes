import random
import pathlib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"file:////{file_path}/sample-exercise.html")

    generate_button = driver.find_element(by=By.NAME, value="generate")
    generate_button.click()

    time.sleep(4)

    code = driver.find_element(by=By.ID, value="my-value")
    code_text = code.text

    text_box = driver.find_element(by=By.ID, value="input")
    text_box.clear()
    text_box.send_keys(code_text)

    driver.find_element(by=By.NAME, value="button").click()
    alert = driver.switch_to.alert
    alert.accept()
    result = driver.find_element(by=By.ID, value="result").text

    assert result == f"It workls! {code_text}!"

    time.sleep(3)

    
    driver.quit()
