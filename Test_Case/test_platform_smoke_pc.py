import pytest
import allure,time
from Fixture.environment import *
from Page.PC.pc_home import Home
from Page.PC.pc_profile import Profile
from Page.PC.pc_sport import Sport
from Page.PC.pc_thirdparty import Thirdparty
from Page.PC.pc_order import Order_Record
from Page.PC.pc_promotion import Promotion

@allure.feature("Platform Smoke Test")
@pytest.mark.pc
@pytest.mark.usefixtures('get_screenshot_path')
@pytest.mark.usefixtures('get_pc_driver')
class TestPlatformSmoke: 

    def test_login(self,env_url,get_user):              
        self.driver.get(env_url[0])  
        account , password = get_user
        home = Home(self.driver,self.screenshot_path)
        home.navigate_to_home_page()
        home.login(account,password)
        assert home.wait_for(home.User_balance).is_displayed() == True

    def test_close_popup(self):
        home = Home(self.driver,self.screenshot_path)
        home.close_popup()
        assert home.checkElementExists(home.Pop_up1) == False 
        assert home.checkElementExists(home.Pop_up2) == False

    def test_sport_page(self):
        Sport_page = Sport(self.driver,self.screenshot_path)
        Sport_page.navigate_to_sport_page()
        time.sleep(1)
        Sport_page.navigate_to_inplay_page()
        time.sleep(1)
        Sport_page.navigate_to_incoming_page()
        time.sleep(1)
        Sport_page.navigate_to_today_page()
        time.sleep(1)
        Sport_page.navigate_to_early_page()
        time.sleep(1)
        Sport_page.navigate_to_parlay_page()
        time.sleep(1)
        Sport_page.navigate_to_outright_page()
        time.sleep(1)
        assert Sport_page.find(Sport_page.Sport).is_displayed() == True

    def test_thirdparty_page(self):
        Thirdparty_page = Thirdparty(self.driver,self.screenshot_path)
        Thirdparty_page.navigate_to_casino_page()
        time.sleep(1)
        assert Thirdparty_page.find(Thirdparty_page.Game_Entrys).is_displayed() == True

    def test_order_record_page(self):
        Order_Record_page = Order_Record(self.driver,self.screenshot_path)
        Order_Record_page.navigate_to_order_page()
        time.sleep(1)
        assert Order_Record_page.find(Order_Record_page.Filter_tabs).is_displayed() == True

    def test_promotion_page(self):
        Promotion_page = Promotion(self.driver,self.screenshot_path)
        Promotion_page.navigate_to_promotion_page()
        time.sleep(1)
        assert Promotion_page.find(Promotion_page.Categorys).is_displayed() == True

    def test_logout(self):
        profile_page = Profile(self.driver,self.screenshot_path)
        profile_page.navigate_to_profile_page()
        profile_page.logout()
        home = Home(self.driver,self.screenshot_path)
        home.navigate_to_home_page()
        time.sleep(3)
        assert home.wait_for(home.LoginBtn).is_displayed() == True
        
