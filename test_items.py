from selenium.webdriver.common.by import By


def test_found_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(5)
    try:
        assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket') is not None
    finally:
        print('...Test case end.')
