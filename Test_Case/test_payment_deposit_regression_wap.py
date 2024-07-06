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
class TestDepositRegression:

    def test_setup(self, env_url, get_admin_user):
        print("TestPlatformMinePage: test_setup")
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)
        func.c2c_enable(False)
        # print(func.get_transaction_status(func.Transaction_Type.DEPOSIT, '202311140a84c5a5148c'))

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
        profile_page.navigate_to_trans_depositRec_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_applyDeposit_cancel(self, env_url, get_admin_user):
        depAmount = random.randint(100, 500)
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_depositRec_page()
        before = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        profile_page.clickElementifExist(profile_page.CardMngBack)
        prevBalance = profile_page.apply_deposit(depAmount)
        assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        after = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        assert after == before + 1
        orderNo = profile_page.getElementText(profile_page.DepOrderNo)
        assert orderNo != ''
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)

        status = func.get_transaction_status(func.Transaction_Type.DEPOSIT, orderNo)
        assert status == 0
        profile_page.click_deposit_withdraw_cancel()
        status = func.get_transaction_status(func.Transaction_Type.DEPOSIT, orderNo)
        assert status == 3
        profile_page.clickElementifExist(profile_page.CardMngBack)
        # profile_page.navigate_to_wallet_page()
        time.sleep(1)
        postBalance = profile_page.getElementText(profile_page.WalletBalance)
        assert postBalance == prevBalance
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_applyDeposit_auditPASS(self, env_url, get_admin_user):
        depAmount = random.randint(800, 1000)
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_depositRec_page()
        before = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        profile_page.clickElementifExist(profile_page.CardMngBack)
        prevBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.apply_deposit(depAmount))))
        assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        after = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        assert after == before + 1
        orderNo = profile_page.getElementText(profile_page.DepOrderNo)
        assert orderNo != ''

        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        print(ad_user)
        func.login_admin(ad_user, ad_pw, secret_key)
        # prevBalance = 1013603.95

        status = func.get_transaction_status(func.Transaction_Type.DEPOSIT, orderNo)
        assert status == 0
        profile_page.clickElementifExist(profile_page.CardMngBack)
        # profile_page.navigate_to_wallet_page()
        time.sleep(1)
        auditBefore = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert prevBalance == auditBefore

        func.deposit_audit(orderNo, func.Deposit_Status.CONFIRMED)
        status = func.get_transaction_status(func.Transaction_Type.DEPOSIT, orderNo)
        assert status == 2
        postBalance = float(Decimal(sub(r'[^\d.]', '', profile_page.getElementText(profile_page.WalletBalance))))
        assert postBalance == prevBalance + depAmount
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_transaction_page_afterDeposit(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_trans_page()
        profile_page.navigate_to_trans_allRecord_page()
        num = [int(s) for s in (profile_page.getElementText(profile_page.RecordNum)).split() if s.isdigit()][0]
        if num > 0:
            assert profile_page.checkElementExists(profile_page.HasDataItem) == True
        else:
            assert profile_page.checkElementExists(profile_page.NodataItem) == True
        profile_page.navigate_to_trans_depositRec_page()
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
