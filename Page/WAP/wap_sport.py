from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Sport(Common):

    Sport = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(3)')
    Inplay = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:first-child')
    Incoming = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(2)')
    Today = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(3)')
    Early = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(4)')    
    Parlay = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(5)')
    Outright = (By.CSS_SELECTOR,'nav[class^="Tabs_nav-tabs"] div:nth-child(6)')

    def navigate_to_sport_page(self):
        return self.wait_for(self.Sport).click()

    def navigate_to_inplay_page(self):
        return self.wait_for(self.Inplay).click()

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