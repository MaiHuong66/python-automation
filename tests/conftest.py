import os
import pytest
from selenium import webdriver
from pytest_html import extras

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    d = webdriver.Chrome(options=options)
    if os.getenv("HEADLESS", "false").lower() != "true":
        d.maximize_window()
    d.implicitly_wait(5)
    yield d
    d.quit()
@pytest.fixture(scope="session")
def valid_user():
    user = os.getenv("LOGIN_USER")
    pwd = os.getenv("LOGIN_PASS")
    if not user or not pwd:
        pytest.fail("Thiếu biến môi trường LOGIN_USER / LOGIN_PASS")
    return user, pwd
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")

            report.extras = getattr(report, "extras", []) + [
                extras.png(driver.get_screenshot_as_base64())
            ]