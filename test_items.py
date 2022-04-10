from selenium.webdriver.common.by import By


def test_conftests(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(5)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    finally:
        print('...Test case end.')
