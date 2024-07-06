from decimal import Decimal
import random
from re import sub
import pytest
import allure
import time
from Fixture.environment import *
from Page.WAP.wap_home import Home
from Page.WAP.wap_profile import Profile
from Page.WAP.wap_sport import Sport
from Page.WAP.wap_thirdparty import Thirdparty
from Page.WAP.wap_order import Order_Record
from Page.CommonFunction import CommonFunction


@allure.feature("Payment Regression Test")
@pytest.mark.payment
@pytest.mark.wap
@pytest.mark.regression
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')
class TestWithdrawRegression:

    def test_setup(self, env_url, get_admin_user):
        print("TestPlatformMinePage: test_setup")
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)
        func.c2c_enable(False)

    def test_login(self, env_url, get_user):
        self.driver.get(env_url['url'])
        account, password = get_user
        home = Home(self.driver, self.screenshot_path)
        home.navigate_to_home_page()
        home.login(account, password)
        assert home.wait_for(home.User_balance).is_displayed() == True
        home.close_popup()
        assert home.checkElementExists(home.Pop_up1) == False
        assert home.checkElementExists(home.Pop_up2) == False

    def test_transaction_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_allRecord_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.navigate_to_trans_withdrawRec_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_apply_withdraw_cancel(self, env_url, get_admin_user):
        walAmount = random.randint(106, 110)
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_withdrawRec_page()
        before = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        profile_page.clickElementifExist(profile_page.CardMngBack)
        prevBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.apply_withdraw(walAmount))))
        assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        after = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        assert after == before + 1
        # prevBalance = '1,013,403.95'
        orderNo = profile_page.getElementText(profile_page.WalOrderNo)
        assert orderNo != ''
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)

        status = func.get_transaction_status(func.Transaction_Type.WITHDRAW, orderNo)
        assert status == 1
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        # profile_page.navigate_to_wallet_page()
        time.sleep(1)
        withdrawAfter = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert withdrawAfter == prevBalance - walAmount
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_withdrawRec_page()
        profile_page.click_deposit_withdraw_cancel()
        status = func.get_transaction_status(func.Transaction_Type.WITHDRAW, orderNo)
        assert status == 3
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.navigate_to_wallet_page()
        time.sleep(1)
        postBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert postBalance == prevBalance
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_apply_withdraw_auditPASS(self, env_url, get_admin_user):
        walAmount = random.randint(100, 105)
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_withdrawRec_page()
        before = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        profile_page.clickElementifExist(profile_page.CardMngBack)
        prevBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.apply_withdraw(walAmount))))
        assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        after = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        assert after == before + 1
        # prevBalance = '1,013,403.95'
        orderNo = profile_page.getElementText(profile_page.WalOrderNo)
        assert orderNo != ''
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)

        status = func.get_transaction_status(func.Transaction_Type.WITHDRAW, orderNo)
        assert status == 1
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        # profile_page.navigate_to_wallet_page()
        time.sleep(1)
        withdrawAfter = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert withdrawAfter == prevBalance - walAmount
        func.withdraw_accepted(orderNo)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.navigate_to_wallet_page()
        time.sleep(1)
        postBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert postBalance == withdrawAfter
        profile_page.clickElementifExist(profile_page.CardMngBack)
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_withdrawRec_page()
        profile_page.trans_page_filter_success()
        firstOrder = profile_page.getElementText(profile_page.WalOrderNo)
        assert orderNo == firstOrder
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_transaction_page_afterWithdraw(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_allRecord_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.navigate_to_trans_withdrawRec_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.click_trans_func_buttons()
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_logout(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.logout()
