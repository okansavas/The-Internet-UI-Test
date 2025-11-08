from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver
        self.dropdown = (By.ID, "dropdown")

    def open(self):
        self.driver.get(self.URL)

    def select_option_by_index(self, index):
        select = Select(self.driver.find_element(*self.dropdown))
        select.select_by_index(index)

    def get_selected_option_text(self):
        select = Select(self.driver.find_element(*self.dropdown))
        return select.first_selected_option.text