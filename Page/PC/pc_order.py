from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Order_Record(Common) :

    Order = (By.CSS_SELECTOR,'div[class="flex"] div:nth-child(10)')
    Filter_tabs = (By.CSS_SELECTOR,'div[class^="FilterTabs"]')

    def navigate_to_order_page(self):
        return self.wait_for(self.Order).click()  