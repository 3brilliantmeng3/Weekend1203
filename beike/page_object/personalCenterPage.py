import time


class PersonalCentPage:
    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    def __init__(self, driver):
        self.driver = driver

    def is_displayed(self):
        time.sleep(5)
        return self.title in self.driver.title