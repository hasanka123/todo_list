from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TodoPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def navigate_to_page(self):
        self.browser.get(self.url)

    def add_todo(self, todo_text):
        self.navigate_to_page()
        todo_input = self.browser.find_element(By.CLASS_NAME, "new-todo")
        todo_input.send_keys(todo_text)
        todo_input.send_keys(Keys.ENTER)