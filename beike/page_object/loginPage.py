from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    url = "http://localhost/index.php?m=user&c=public&a=login"
    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    username_input_loc = (By.ID, "username")
    password_input_loc = (By.ID, "password")
    login_button_loc = (By.CLASS_NAME, "login_btn")

    def find_element(self, loc):
        try:
            return self.driver.find_element(*loc)
        except:
            print("{0}页面没有找到{0}的元素".format(self.title, loc))

    def send_keys(self, loc, keys):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(keys)

    def click(self, loc):
        self.find_element(loc).click()

    def is_match_title(self):
        return "用户登录" in self.driver.title

    def input_username(self, keys):
        self.send_keys(self.username_input_loc, keys)

    def input_password(self, keys):
        self.send_keys(self.password_input_loc, keys)

    def click_login_button(self):
        self.click(self.login_button_loc)

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
        

