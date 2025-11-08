from pages.dropdown_page import DropdownPage

def test_select_dropdown_option(driver):
    page = DropdownPage(driver)
    page.open()

    page.select_option_by_index(1)
    assert page.get_selected_option_text() == "Option 1"

    page.select_option_by_index(2)
    assert page.get_selected_option_text() == "Option 2"