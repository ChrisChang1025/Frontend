from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Promotion(Common) :

    Promotion = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(11)')
    Categorys = (By.CSS_SELECTOR,'div[class^="self-center"]')

    def navigate_to_promotion_page(self):
        return self.wait_for(self.Promotion).click()  