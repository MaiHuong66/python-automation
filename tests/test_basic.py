from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_password_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("abcxyz")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    assert "Your password is invalid!" in msg.text

def test_login_username_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("abcxyz")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    assert "Your username is invalid!" in msg.text

def test_login_empty_username(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    assert "Your username is invalid!" in msg.text

def test_tick_first_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    first = checkboxes[0]
    assert not first.is_selected()    
    first.click()
    assert first.is_selected()       

def test_tick_second_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    second = checkboxes[1]
    assert second.is_selected()    
    second.click()
    assert not second.is_selected()

def test_select_option_2(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.text == "Option 2"

def test_dynamic_loading(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    result = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert result.text == "Hello World!"