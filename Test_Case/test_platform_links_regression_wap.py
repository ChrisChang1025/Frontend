from datetime import datetime
import random
import string
import pytest
import allure
from allure import attachment_type
import time
from Fixture.environment import *
from Page.WAP.wap_home import Home
from Page.WAP.wap_profile import Profile
from Page.WAP.wap_sport import Sport
from Page.WAP.wap_thirdparty import Thirdparty
from Page.WAP.wap_order import Order_Record
from Page.CommonFunction import CommonFunction


@allure.feature("Platform links Regression Test")
@pytest.mark.platform
@pytest.mark.wap
@pytest.mark.regression
@pytest.mark.logo
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')
class TestLinksRegression:

    def test_login(self, env_url, get_user):
        self.driver.get(env_url['url'])
        account, password = get_user
        home = Home(self.driver, self.screenshot_path)
        home.navigate_to_home_page()
        home.screenshot(f"{self.screenshot_path}noLogin_Index.png")
        home.login(account, password)
        assert home.wait_for(home.User_balance).is_displayed() == True
        home.close_popup()
        assert home.checkElementExists(home.Pop_up1) == False
        assert home.checkElementExists(home.Pop_up2) == False

    def test_bottom_tabs(self):
        home = Home(self.driver, self.screenshot_path)
        home.login_click_buttom_tabs()
        home.navigate_to_home_page()

    def test_sideBar_pages(self):
        home = Home(self.driver, self.screenshot_path)
        home.click_sideBar_navLinks()

    def test_profile_pages(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.click_MyPage_navLinks()

    def test_profile_footer_links(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.click_profile_footer_links()

    def test_logout(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.logout()