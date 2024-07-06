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


@allure.feature("Register Regression Test")
@pytest.mark.register
@pytest.mark.wap
@pytest.mark.regression
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')
class TestRegisterRegression:

    regUsername = 'at' + datetime.now().strftime('%H%M%S%f')[0:8] + ''.join(random.choices(string.
                                                                                           ascii_lowercase + string.digits, k=3))
    regPassword = 'test1234'

    def test_setup(self, env_url, get_admin_user):
        self.driver.get(env_url['url'])
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)
        func.get_all_sms_settings()
        func.set_tiger_sms_status('off')
        func.get_all_sms_settings()

    # def test_login(self, env_url):
    #     home = Home(self.driver, self.screenshot_path)
    #     home.navigate_to_home_page()
    #     home.login(self.regUsername, self.regPassword)
    #     assert home.wait_for(home.User_balance).is_displayed() == True
    #     home.close_popup()
    #     assert home.checkElementExists(home.Pop_up1) == False
    #     assert home.checkElementExists(home.Pop_up2) == False

    def test_home_tabs_pages(self):
        home = Home(self.driver, self.screenshot_path)
        home.noLogin_click_buttom_tabs()
        allure.attach(self.driver.get_screenshot_as_png(), name='Home page screenshot', attachment_type=attachment_type.PNG)  # screenshot add into allure report
        home.clickElementifExist(home.Index)

    def test_register_account(self):
        home = Home(self.driver, self.screenshot_path)
        home.register(self.regUsername, self.regPassword)
        print(self.regUsername)
        home.close_popup()
        assert home.checkElementExists(home.Pop_up1) == False
        assert home.checkElementExists(home.Pop_up2) == False

    def test_profile_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        time.sleep(1)
        getName = profile_page.getElementText(profile_page.Username)
        assert getName == self.regUsername

    def test_personalInfo_page_before(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_personalInfo_page()
        username = profile_page.getElementText(profile_page.BannerAcc)
        assert username == self.regUsername
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_complete_personalData(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_personalInfo_page()
        profile_page.complete_personal_data()
        noCompCount = profile_page.getElementCount(profile_page.NoCompItem)
        assert noCompCount == 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_complete_withdrawPwd(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_personalInfo_page()
        profile_page.complete_withdraw_password()
        noCompCount = profile_page.getElementCount(profile_page.NoCompItem)
        assert noCompCount == 0
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_complete_security_phoneNumber(self, env_url):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_personalInfo_page()
        profile_page.set_phoneNumber_getSMSCode()
        if profile_page.checkElementExists(profile_page.SMSCode_Textbox):
            func = CommonFunction(env_url)
            optCode = func.get_sms_code(self.regUsername)
            profile_page.set_phoneNumber_inputSMS(optCode)
            profile_page.clickElementifExist(profile_page.SetPhoneNo)
            assert profile_page.checkElementExists(profile_page.PhoneNumber_Textbox) == False
            profile_page.clickElementifExist(profile_page.CardMngBack)
            profile_page.clickElementifExist(profile_page.CardMngBack)
        else:
            errorCode = profile_page.getElementText(profile_page.PrompErrorText)
            profile_page.clickElementifExist(profile_page.SuccessOk)
            profile_page.clickElementifExist(profile_page.CardMngBack)
            profile_page.clickElementifExist(profile_page.CardMngBack)
            profile_page.clickElementifExist(profile_page.CardMngBack)
            assert False, f"Get SMS fail error code : {errorCode}"

    def test_eventGift_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_eventGift_page()
        assert profile_page.getElementCount(profile_page.EventGiftBanner) > 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_personalInfo_page_after(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_personalInfo_page()
        username = profile_page.getElementText(profile_page.BannerAcc)
        assert username == self.regUsername
        noCompCount = profile_page.getElementCount(profile_page.NoCompItem)
        assert noCompCount == 0
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_logout(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.logout()
