from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Sport(Common):

    Sport = (By.CSS_SELECTOR,'div[class="flex"] div:first-child')
    Inplay = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(2)')
    Incoming = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(3)')
    Today = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(4)')
    Early = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(5)')    
    Parlay = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(6)')
    Outright = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(7)')

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