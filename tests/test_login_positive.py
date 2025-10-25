from selenium.webdriver.common.by import By
import time

def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message
