from selenium.webdriver.common.by import By
import time
from ..Common import Common

class Order_Record(Common) :

    Order = (By.CSS_SELECTOR,'div[class^="tabNavigation_icons"] div.flex-1:nth-child(4)')
    Filter_tabs = (By.CSS_SELECTOR,'div[class^="FilterTabs"]')
    Order_Count = (By.CSS_SELECTOR,'img[width="20"][height="20"][class^="w-5"]')
    Unsettle_tab = (By.CSS_SELECTOR,'div[class^="FilterTabs"] div[id="0"]')
    Settled_tab = (By.CSS_SELECTOR,'div[class^="FilterTabs"] div[id="1"]')
    Canceled_tab = (By.CSS_SELECTOR,'div[class^="FilterTabs"] div[id="3"]')
    Total_tab = (By.CSS_SELECTOR,'div[class^="FilterTabs"] div[id="2"]')
    Sport_record = (By.CSS_SELECTOR,'div[class*="items-center"] div[class*="items-center"] div[class^="px-5"]:first-child')
    Thirdparty_record = (By.CSS_SELECTOR,'div[class*="items-center"] div[class*="items-center"] div[class^="px-5"]:nth-child(2)')
    Game_Result = (By.CSS_SELECTOR,'div[class*="items-center"] div[class*="items-center"] div[class^="px-5"]:nth-child(3)')
    Cashout_button = (By.CSS_SELECTOR,'div[data-cid="cashOutButton"] button')

    def navigate_to_order_page(self):
        return self.wait_for(self.Order).click()  
    
    def count_unsettled(self) -> int:
        self.wait_for(self.Sport_record).click()
        time.sleep(1)
        self.wait_for(self.Unsettle_tab).click()
        time.sleep(1)
        return self.getElementCount(self.Order_Count)
    
    def cashout(self):
        retry_count = 0
        for i in range(10):
            if self.checkElementExists(self.Cashout_button) :
                break
            else : 
                time.sleep(10)
        while self.checkElementExists(self.Cashout_button) and retry_count <= 30 :
            self.wait_for(self.Cashout_button).click()
            retry_count+=1
            time.sleep(2)

