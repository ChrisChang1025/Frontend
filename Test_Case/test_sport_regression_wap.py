from decimal import Decimal
import random
from re import sub
import pytest
import allure
import time
from Fixture.environment import *
from Page.WAP.wap_sport import Sport
from Page.WAP.wap_order import Order_Record
from Page.WAP.wap_home import Home
from Page.CommonFunction import CommonFunction


@allure.feature("Sport Regression Test")
@pytest.mark.sport
@pytest.mark.wap
@pytest.mark.regression
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_wap_driver')
class TestCardMngRegression:

    def test_setup(self, env_url, get_admin_user):
        func = CommonFunction(env_url)
        ad_user, ad_pw, secret_key = get_admin_user
        func.login_admin(ad_user, ad_pw, secret_key)
        func.get_sport_settings()
        func.set_sport_cashout_status('on')

    def test_login(self, env_url, get_user):
        self.driver.get(env_url['url'])
        account, password = get_user
        home = Home(self.driver, self.screenshot_path)
        home.navigate_to_home_page()
        time.sleep(3)
        assert home.getElementCount(home.Match_cards) == 8, "Home page match cards is not 8"
        home.login(account, password)
        assert home.wait_for(home.User_balance).is_displayed() == True
        home.close_popup()
        assert home.checkElementExists(home.Pop_up1) == False
        assert home.checkElementExists(home.Pop_up2) == False

    def test_early_bet(self):
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        before_count = Order_page.count_unsettled()

        Sport_page = Sport(self.driver,self.screenshot_path)
        Sport_page.navigate_to_sport_page()    
        Sport_page.navigate_to_early_page()     
        time.sleep(1)
        bet_count=0
        for category in [Sport_page.Football,Sport_page.Basketball,Sport_page.Tennis,Sport_page.Baseball] :
            if Sport_page.checkElementExists(category):
                Sport_page.wait_for(category).click()
                Sport_page.wait_for(Sport_page.Tournament).click()
                Sport_page.wait_for(Sport_page.Early_matches).click()
                time.sleep(2)
                Sport_page.bet_single(Sport_page.Mtch_odds)
                assert Sport_page.checkElementExists(Sport_page.Bet_detail_confirm), f"Bet failed without bet deatil"
                Sport_page.find(Sport_page.Bet_detail_confirm).click()
                bet_count+=1
        
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        after_count = Order_page.count_unsettled()

        assert after_count == before_count+bet_count , f"before = {before_count} & bet = {bet_count}, after = {after_count}"

        Order_page.cashout()
        cashout_count = Order_page.count_unsettled()
        assert cashout_count < after_count , f"Cashout failed !"

    def test_outright_bet(self):
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        before_count = Order_page.count_unsettled()

        Sport_page = Sport(self.driver,self.screenshot_path)
        Sport_page.navigate_to_sport_page()    
        Sport_page.navigate_to_outright_page()   
        time.sleep(1)
        bet_count=0
        for category in [Sport_page.Football,Sport_page.Basketball,Sport_page.Tennis,Sport_page.Baseball] :
            if Sport_page.checkElementExists(category):
                Sport_page.wait_for(category).click()
                Sport_page.wait_for(Sport_page.Header_arrow).click()
                time.sleep(1)
                Sport_page.wait_for(Sport_page.Tournament_content).click()
                time.sleep(1)
                if Sport_page.checkElementExists(Sport_page.Odds) == False:
                    Sport_page.wait_for(Sport_page.Outright_market_subtitle).click()
                time.sleep(1)
                Sport_page.bet_single(Sport_page.Odds)
                assert Sport_page.checkElementExists(Sport_page.Bet_detail_confirm), f"Bet failed without bet deatil"
                Sport_page.find(Sport_page.Bet_detail_confirm).click()
                bet_count+=1
        
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        after_count = Order_page.count_unsettled()

        assert after_count == before_count+bet_count , f"before = {before_count} & bet = {bet_count}, after = {after_count}"

    def test_parlay_bet(self):
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        before_count = Order_page.count_unsettled()

        Sport_page = Sport(self.driver,self.screenshot_path)
        Sport_page.navigate_to_sport_page()    
        Sport_page.navigate_to_parlay_page() 
        time.sleep(1)
        Sport_page.select_parlay()
        Sport_page.bet_parlay()
        assert Sport_page.checkElementExists(Sport_page.Bet_detail_confirm), f"Bet parlay failed without bet deatil"
        Sport_page.find(Sport_page.Bet_detail_confirm).click()

        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        after_count = Order_page.count_unsettled()

        assert after_count > before_count , f"before = {before_count} , after = {after_count}"

    def test_inplay_bet(self):
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        before_count = Order_page.count_unsettled()

        Sport_page = Sport(self.driver,self.screenshot_path)
        Sport_page.navigate_to_sport_page() 
        Sport_page.navigate_to_inplay_page()
        time.sleep(1)
        match_count = Sport_page.get_inplay_count()
        if int(match_count) == 0 :
            pytest.skip("No inplay match")
        Sport_page.bet_single(Sport_page.Mtch_odds)
        assert Sport_page.checkElementExists(Sport_page.Bet_detail_confirm), f"Bet failed without bet deatil"
        Sport_page.find(Sport_page.Bet_detail_confirm).click()
        Order_page = Order_Record(self.driver,self.screenshot_path)
        Order_page.navigate_to_order_page()
        after_count = Order_page.count_unsettled()

        assert after_count > before_count , f"before = {before_count}, after = {after_count}"

        Order_page.cashout()
        cashout_count = Order_page.count_unsettled()
        assert cashout_count < after_count , f"Cashout failed !"



        
        