import sys, datetime, traceback, time, requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as Actions


class Common:

    def __init__(self, browser, screenshot_path):
        self._browser = browser
        self._screenshot_path = screenshot_path
        self._wait = WebDriverWait(self._browser, 30)
        self.admin_token = None

    def wait_for(self,locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def find(self,locator):
        return self._browser.find_element(*locator)
    
    def finds(self,locator) -> list:
        return self._browser.find_elements(*locator)

    def getElementText(self, _elm):
        elms = self._browser.find_elements(*_elm)
        print(elms)
        if len(elms) > 0:
            for elm in elms:
                if elm.is_displayed():
                    print(f'====={elm.text}')
                    return elm.text
            return ''
        else:
            return ''
        
    
    def screenshot(self, path):
        return self._browser.save_screenshot(path)

    def getElementCount(self, _elm, _frame=False):
            """ 檢查頁面物件是否存在且返回數量\n
                Args: \n
                    _page : [必要參數] 執行操作的頁面名稱
                    _elm : [必要參數] 操作的物件名稱
                    _frame : [選填參數] 物件是否在iframe中，預設為「不是」
                Return: \n
                    0 / 該物件數量
            """
            elms = self._browser.find_elements(*_elm)
            print(elms)
            if len(elms) > 0:
                return len(elms)
            else:
                return 0

    def checkElementExists(self, _elm, _frame=False):
            """ 檢查頁面物件是否存在 \n
                Args: \n
                    _page : [必要參數] 執行操作的頁面名稱
                    _elm : [必要參數] 操作的物件名稱
                    _frame : [選填參數] 物件是否在iframe中，預設為「不是」
                Return: \n
                    True / False
            """
            elms = self._browser.find_elements(*_elm)
            print(elms)
            if len(elms) > 0:
                for elm in elms:
                    if elm.is_displayed():
                        return True
                return False
            else:
                return False

    def clickElementifExist(self, _elm, _frame=False):
            """ 如果有找到頁面物件，就點擊頁面物件 \n
                Args: \n
                    _page : [必要參數] 執行操作的頁面名稱
                    _elm : [必要參數] 操作的物件名稱
                    _frame : [選填參數] 物件是否在iframe中，預設為「不是」
                Return: \n
                    None
            """
            try:
                _count = 0
                elms = []
                while len(elms) == 0:
                    elms = self._browser.find_elements(*_elm)
                    if _count > 5:
                        break
                    else:
                        _count += 1
                    time.sleep(1)

                if (len(elms) != 0):
                    if elms[0].is_displayed():
                        elms[0].click()
                    else:
                        print(elms[0], "頁面上不可見")
            except:
                self.__errorHandling(_elm)

    def __errorHandling(self, _elm):
            """ 錯誤時的處理 \n
                Args: \n
                    _page : [必要參數] 執行操作的頁面名稱
                    _elm : [必要參數] 操作的物件名稱
                Return: \n
                    None
            """

            self._browser.save_screenshot(f"{self._screenshot_path}Error_{datetime.datetime.now():%Y%m%d_%H%M%S}.png")
            formatted_lines = traceback.format_exc().splitlines()
            for s in formatted_lines[:-1]:
                print(s)
            raise sys.exc_info()[1]

    def drag_and_drop(self, elm, x,y):
        action = Actions(self._browser)
        element = self.find(elm)
        action.drag_and_drop_by_offset(element,x,y).perform()

    