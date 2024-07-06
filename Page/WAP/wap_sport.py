from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Sport(Common):

    Sport = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(3)')
    Inplay = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:first-child')
    Inplay_count = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:first-child span[class]')
    Incoming = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(2)')
    Incoming_count = (By.CSS_SELECTOR, 'nav[class^="Tabs_nav-tabs"] div:nth-child(2) span[class]')
    Today = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(3)')
    Early = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(4)')  
    Tournament = (By.CSS_SELECTOR,'div[class^="Tournament_checkBox"]')  
    Early_matches = (By.CSS_SELECTOR,'div[class^="SelectOption_content"]')
    Parlay = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(5)')
    Outright = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(6)')
    Header_arrow = (By.CSS_SELECTOR,'div[class^="SimpleHeader_arrow"]')
    Tournament_content = (By.CSS_SELECTOR,'div[class^="Tournament_content"]')
    Outright_market_subtitle = (By.CSS_SELECTOR,'div[class^="outrightMarket_subtitle"]')
    Football = (By.CSS_SELECTOR,'img[alt="Football"]')
    Basketball = (By.CSS_SELECTOR,'img[alt="Basketball"]')
    Tennis = (By.CSS_SELECTOR,'img[alt="Tennis"]')
    Baseball = (By.CSS_SELECTOR,'img[alt="Baseball"]')
    Odds = (By.CSS_SELECTOR,'div[class^="odds-btn-container"]')
    Mtch_odds = (By.CSS_SELECTOR,'#layout-scroll-content div[class^="Collapse_box"] div[class^="odds-btn-container"] div[class^="icon"]')
    Calvulator_key_2 = (By.CSS_SELECTOR, 'div[class^="Calculator_numeric-section"] div:nth-child(2)')
    Calvulator_key_3 = (By.CSS_SELECTOR, 'div[class^="Calculator_numeric-section"] div:nth-child(3)')
    Bet_confirm_text = (By.CSS_SELECTOR, 'span[class^="BettingFooter_confirmText"]')
    Bet_winable = (By.CSS_SELECTOR,'div[class^="BettingFooter_calcWinable"]')
    Bet_detail_confirm = (By.CSS_SELECTOR, 'footer a[class^="Button_wrapper"]')
    Bet_parlay_button = (By.CSS_SELECTOR,'div[class^="BettingFooter_side"] button[class^="Button_wrapper"]')
    Parlay_input_credit = (By.CSS_SELECTOR,'div[class^="Parlay_parlay"] div[class^="Parlay_parlay-item"]:last-child div[class^="Currency_input"]')
    Parlay_early_date = (By.CSS_SELECTOR,'div[class^="DateFilter_wrapper"] a:nth-child(5)')
    Bet_car_button = (By.CSS_SELECTOR,'div[class^="BettingCartButton"]')

    def navigate_to_sport_page(self):
        return self.wait_for(self.Sport).click()

    def navigate_to_inplay_page(self):
        return self.wait_for(self.Inplay).click()
    
    def get_inplay_count(self):
        return self.getElementText(self.Inplay_count)

    def navigate_to_incoming_page(self):
        return self.wait_for(self.Incoming).click()

    def navigate_to_today_page(self):
        return self.wait_for(self.Today).click()

    def navigate_to_early_page(self):
        return self.wait_for(self.Early).click()

    def navigate_to_parlay_page(self):
        return self.wait_for(self.Parlay).click()

    def navigate_to_outright_page(self):
        return self.wait_for(self.Outright).click()
    
    def bet_single(self,elm):
        if self.click_valid_odd(elm):
            self.wait_for(self.Calvulator_key_2).click()
            self.wait_for(self.Calvulator_key_3).click()
            while self.checkElementExists(self.Bet_confirm_text) :
                self.wait_for(self.Bet_confirm_text).click() 
                time.sleep(2)
        else:
            assert False, "No valid odds !"

    def click_valid_odd(self,elm):
        odds = self.finds(elm)
        for odd in odds :
            if '.' in str(odd.text):
                odd.click()
                return True
        return False

    def select_parlay(self):
        for category in [self.Football,self.Basketball,self.Tennis,self.Baseball] :
            if self.checkElementExists(category):
                self.find(category).click()
                time.sleep(1)                
                self.wait_for(self.Parlay_early_date).click()
                time.sleep(1)
                self.wait_for(self.Tournament).click()
                self.wait_for(self.Early_matches).click()
                time.sleep(1)
                self.click_valid_odd(self.Mtch_odds)
                time.sleep(1)
    
    def bet_parlay(self):
        if self.checkElementExists(self.Bet_car_button) :
            self.find(self.Bet_car_button).click()
            time.sleep(1)
            self.wait_for(self.Parlay_input_credit).click()
            self.wait_for(self.Calvulator_key_3).click()
            self.wait_for(self.Calvulator_key_3).click()
            while self.checkElementExists(self.Bet_confirm_text) :
                self.wait_for(self.Bet_confirm_text).click() 
                time.sleep(10)
        else :
            assert False, "Bet car button disappear"
        
