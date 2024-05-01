import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from todo_page import TodoPage

@pytest.fixture(scope="function")
def todo_page(browser, url):
    return TodoPage(browser, url)

def test_add_todo(todo_page):
    todo_page.add_todo("Example Todo")
    assert WebDriverWait(todo_page.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Example Todo']"))
    )