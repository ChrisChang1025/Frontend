import pytest
import allure
import time
from Fixture.environment import *
from Page.WAP.wap_home import Home
from Page.WAP.wap_profile import Profile
from Page.WAP.wap_sport import Sport
from Page.WAP.wap_thirdparty import Thirdparty
from Page.WAP.wap_order import Order_Record


@allure.feature("Payment Regression Test")
@pytest.mark.payment
@pytest.mark.wap
@pytest.mark.regression
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')
class TestCardMngRegression:

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

    def test_cardMng_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.navigate_to_cardmng_page()
        assert profile_page.checkElementExists(profile_page.AddCardBtn) == True
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_add_bankCard(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_cardmng_page()
        preNum = profile_page.getElementCount(profile_page.CardItem)
        profile_page.add_bankCard()
        afterNum = profile_page.getElementCount(profile_page.CardItem)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        assert afterNum == preNum + 1

    def test_delete_bankCard(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_cardmng_page()
        preNum = profile_page.getElementCount(profile_page.CardItem)
        assert preNum >= 1
        profile_page.delete_bankCard()
        afterNum = profile_page.getElementCount(profile_page.CardItem)
        profile_page.clickElementifExist(profile_page.CardMngBack)
        assert afterNum == preNum - 1

    def test_wallet_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        assert profile_page.checkElementExists(profile_page.WalletInfo) == True
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_add_wallet(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        beforeCount = profile_page.getElementCount(profile_page.CurrencyName)
        profile_page.add_wallet_currency()
        afterCount = profile_page.getElementCount(profile_page.CurrencyName)
        assert profile_page.checkElementExists(profile_page.WalletInfo) == True
        assert afterCount == beforeCount + 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_delete_wallet(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        beforeCount = profile_page.getElementCount(profile_page.CurrencyName)
        profile_page.delete_wallet_currency()
        afterCount = profile_page.getElementCount(profile_page.CurrencyName)
        assert profile_page.checkElementExists(profile_page.WalletInfo) == True
        assert afterCount == beforeCount - 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_switch_wallet(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        target = profile_page.getElementText(profile_page.SwitchCur)
        profile_page.switch_wallet_currency()
        now = profile_page.getElementText(profile_page.MyCurrency)
        assert now == target
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_cryptoWallet_page(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        profile_page.navigate_to_cryptoWallet_page()
        assert profile_page.checkElementExists(profile_page.CryptoHeader)
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_add_cryptocurrency_wallet(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        profile_page.navigate_to_cryptoWallet_page()
        before = profile_page.getElementCount(profile_page.CurItem)
        profile_page.add_cryptocurrency_wallet()
        after = profile_page.getElementCount(profile_page.CurItem)
        assert after == before + 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_delete_cryptocurrency_wallet(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_wallet_page()
        profile_page.navigate_to_cryptoWallet_page()
        before = profile_page.getElementCount(profile_page.CurItem)
        profile_page.delete_cryptocurrency_wallet()
        after = profile_page.getElementCount(profile_page.CurItem)
        assert after == before - 1
        profile_page.clickElementifExist(profile_page.CardMngBack)

    def test_logout(self):
        profile_page = Profile(self.driver, self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.logout()
