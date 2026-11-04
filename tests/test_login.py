from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    msg = login_page.get_message()
    assert "You logged into a secure area!" in msg

def test_login_password_failure(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "abcxyz")
    msg = login_page.get_message()
    assert "Your password is invalid!" in msg 

def test_login_username_failure(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("abcxyz", "SuperSecretPassword!")
    msg = login_page.get_message()
    assert "Your username is invalid!" in msg

def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "SuperSecretPassword!")
    msg = login_page.get_message()
    assert "Your username is invalid!" in msg

def test_login_empty_pasword(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "")
    msg = login_page.get_message()
    assert "Your password is invalid!!!" in msg

