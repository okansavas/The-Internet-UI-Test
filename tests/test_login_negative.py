from selenium.webdriver.common.by import By
import time

def test_login_failure(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("fehler")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
