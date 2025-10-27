from selenium.webdriver.common.by import By
import time


def test_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for box in checkboxes:
        if not box.is_selected():
            box.click()
    time.sleep(1)
    assert all(box.is_selected() for box in checkboxes)