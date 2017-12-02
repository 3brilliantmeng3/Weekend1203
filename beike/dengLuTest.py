import unittest
from selenium import webdriver

from beike.page_object.loginPage import LoginPage
from beike.page_object.personalCenterPage import PersonalCentPage
from day5.myTestCase import MyTestCase


class DengLuTest(MyTestCase):
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.open()
        self.assertTrue(lp.is_match_title())
        lp.login("changcheng", "123654")
        pc = PersonalCentPage(self.driver)
        self.assertTrue(pc.is_displayed())

