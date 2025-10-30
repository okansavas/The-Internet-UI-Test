from selenium.webdriver.common.by import By
import time


def test_checkbox(driver):

    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    if checkboxes[1].is_selected():
        checkboxes[1].click()

    time.sleep(2)
    assert checkboxes[0].is_selected()
    assert not checkboxes[1].is_selected()