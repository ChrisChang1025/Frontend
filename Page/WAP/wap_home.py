from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from ..Common import Common


class Home(Common):
    Body = (By.CSS_SELECTOR, 'body[class]')
    Index = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(1)')
    Game = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(2)')
    Inplay = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(3)')
    Records = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(4)')
    My = (By.CSS_SELECTOR, 'div[class^="tabNavigation_icons"] div.flex-1:nth-child(5)')
    IndexBalls = (By.CSS_SELECTOR, 'div[class="slick-track"]')
    IndexAnchors = (By.CSS_SELECTOR, 'div[id="sports"] div[class="slick-list"] div[class="slick-track"] div[data-index="0"]')
    AnchorPage = (By.CSS_SELECTOR, 'div[data-cid="AnchorHome"]')
    AnchorBackIndex = (By.CSS_SELECTOR, 'div[data-cid="BottomNavigation"] div.flex button:nth-child(1)')
    GameCarousel = (By.CSS_SELECTOR, 'div[class^="mobile_main"] div.w-full:nth-child(1)')
    InplayMenu = (By.CSS_SELECTOR, 'div[data-cid="MobileMenu"]')
    InplayAnchors = (By.CSS_SELECTOR, 'div[id="sports"] div[class^="MobileMenu_ball-type"]:nth-child(1)')
    RecordsBackIdx = (By.CSS_SELECTOR, 'div[class^="pb-3 text"] div[class="flex items-center"] span')
    RecordsPage = (By.CSS_SELECTOR, 'div[data-cid="betRecordEntrance"]')
    RecordsOfSport = (By.CSS_SELECTOR, 'div[data-cid="betRecordEntrance"] div.bg-white div.flex div:nth-child(1) div.px-5:nth-child(1)')
    SportRecordPage = (By.CSS_SELECTOR, 'div[data-cid="BetRecord-Sports"]')
    RecordsOf3rdGame = (By.CSS_SELECTOR, 'div[data-cid="betRecordEntrance"] div.bg-white div.flex div:nth-child(1) div.px-5:nth-child(2)')
    ThirdGamePage = (By.CSS_SELECTOR, 'div[data-cid="BetRecord-ThirdGames"]')
    RecordsOfGame = (By.CSS_SELECTOR, 'div[data-cid="betRecordEntrance"] div.bg-white div.flex div:nth-child(1) div.px-5:nth-child(3)')
    GamePageTitle = (By.CSS_SELECTOR, 'div[class^="TopHeader_title"]')
    BackToIndex = (By.CSS_SELECTOR, 'div[class^="TopHeader_top"] div:nth-child(1) svg')
    MypersonInfo = (By.CSS_SELECTOR, 'div[class^="personInfo_main"]')
    LoginBtn = (By.CSS_SELECTOR, 'button[class^="UnLogin_loginBtn"]')
    RegisterBtn = (By.CSS_SELECTOR, 'button[class^="UnLogin_registerBtn"]')
    Cancel_ezpwd = (By.CSS_SELECTOR, 'div[data-cid="CoreModal__Footer"] button:nth-child(2)')
    Pop_up1 = (By.CSS_SELECTOR, '#pop_close_dark')
    Pop_up2 = (By.CSS_SELECTOR, 'path[fill="ivory"]')
    User_balance = (By.CSS_SELECTOR, 'div[class^="UserDetail_money"]')
    Loginpage_loginBtn1 = (By.CSS_SELECTOR, 'div[style="opacity: 1;"] button[type="button"]')
    # sideBar
    HeadIcon = (By.CSS_SELECTOR, 'div[data-cid="UserDetail"] div div.bg-primary')
    BalanceBtn = (By.CSS_SELECTOR, 'div[data-cid="UserBalance"] div[class^="userBalance_sideBarBalanceInfo"] div.flex')
    BalancSideBar = (By.CSS_SELECTOR, 'div[class^="userBalance_sideBarWalletList"]')
    SideBarElm = (By.CSS_SELECTOR, 'aside[data-cid="Sidebar"]')
    CouponSumm = (By.CSS_SELECTOR, 'div[class^="slick-track"] div button')
    CouponPage = (By.CSS_SELECTOR, 'div[data-cid="CouponCenter"]')
    CouponBtn = (By.CSS_SELECTOR, 'div[data-cid="CouponCenter"] div:nth-child(2)  div.tw-layout-center:nth-child(1)')
    VoucherBtn = (By.CSS_SELECTOR, 'div[data-cid="CouponCenter"] div:nth-child(2)  div.tw-layout-center:nth-child(2)')
    HeaderBack = (By.CSS_SELECTOR, 'div[id="pageHeader"] button')
    NavWallet = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(1) span')
    WalletPage = (By.CSS_SELECTOR, 'div[data-cid="WalletView"]')
    NavCoupon = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(2) span')
    NavTimezone = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(3) span')
    TimezonePage = (By.CSS_SELECTOR, 'div[data-cid="TimezoneBlocks"]')
    NavAppDownload = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(4) span')
    AppDownloadBtn = (By.CSS_SELECTOR, 'div[data-cid="DownloadApp_Footer"] button')
    NavPlayRules = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(5) span')
    PlayRulesPage = (By.CSS_SELECTOR, 'div[data-cid="GamePlan"]')
    NavCustService = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(6) span')
    WelcomeTitle = (By.CSS_SELECTOR, 'div[class^="VdPersonInfo_info"] div:nth-child(1)')
    NavTransaction = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(7) span')
    TransTitle = (By.CSS_SELECTOR, 'div[id="pageHeader"] div[class^="pageHeader_center"]:nth-child(2)')
    NavBetRecord = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(8) span')
    NavGameSearch = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(9) span')
    NavAnchors = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(10) span')
    NavMyFavorite = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(12) span')
    FavoriteElm = (By.CSS_SELECTOR, 'div[class^="FavoriteHeader"]')
    FavoriteClose = (By.CSS_SELECTOR, 'div[class^="FavoriteHeader_close"] svg')
    NavEventGifts = (By.CSS_SELECTOR, 'ul[class^="navLinks_navLinks"] li:nth-child(13) span')
    EventBanner = (By.CSS_SELECTOR, 'div[class="flex h-[50px]"] div.h-full')

    # register
    Account_textbox = (By.XPATH, '//input[@name="username"]')
    Password_textbox = (By.XPATH, '//input[@type="password"]')
    Loginpage_loginBtn2 = (By.CSS_SELECTOR, 'button[type="submit"]')
    Confirm_Password_textbox = (By.XPATH, '//input[@name="confirmPassword"]')
    Register_button = (By.XPATH, "//button[1]")
    Canvas_frame = (By.CSS_SELECTOR, "canvas[class^='JigsawPuzzleValidation_canvas']")
    Drag_slider = (By.CSS_SELECTOR, "div[class^='JigsawPuzzleValidation_slider_']")
    Match_cards = (By.CSS_SELECTOR, 'div[class^="UnitCard_box"]')

    def navigate_to_home_page(self):
        self.wait_for(self.Index).click()
        # self.wait_for((By.CSS_SELECTOR,'body[class]')).send_keys(Keys.PAGE_DOWN)
        # time.sleep(1)

    def login(self, _username, _password):
        self.wait_for(self.LoginBtn).click()  # 登入按鈕
        self.wait_for(self.Loginpage_loginBtn1).click()  # 登入        
        self.wait_for(self.Account_textbox).send_keys(_username)  # 輸入帳號
        self.wait_for(self.Password_textbox).send_keys(_password)  # 輸入密碼
        self.screenshot(f"{self._screenshot_path}LoginPage.png")
        self.wait_for(self.Loginpage_loginBtn2).click()
        time.sleep(3)

    def register(self, _username, _password):
        self.wait_for(self.RegisterBtn).click()  # 註冊按鈕        
        self.wait_for(self.Account_textbox).send_keys(_username)  # 輸入帳號
        self.wait_for(self.Password_textbox).send_keys(_password)  # 輸入密碼
        self.wait_for(self.Confirm_Password_textbox).send_keys(_password)  # 確認密碼
        self.screenshot(f"{self._screenshot_path}RegisterPage.png")
        self.wait_for(self.Register_button).click()
        time.sleep(2)
        frame = self.find(self.Canvas_frame)
        style = frame.get_attribute("style")
        print(style)
        print(style[style.index('left:')+5:style.index('px')])
        self.drag_and_drop(self.Drag_slider, int(style[style.index('left:')+5:style.index('px')]), 3)
        time.sleep(3)

    def close_popup(self):
        self.clickElementifExist(self.Cancel_ezpwd)
        time.sleep(2)
        while self.checkElementExists(self.Pop_up1) or self.checkElementExists(self.Pop_up2):
            if self.checkElementExists(self.Pop_up1):
                self.find(self.Pop_up1).click()
            else:
                self.find(self.Pop_up2).click()
            time.sleep(2)

    def noLogin_click_buttom_tabs(self):
        self.wait_for(self.Index).click()
        self.wait_for(self.IndexBalls)
        assert self.checkElementExists(self.IndexBalls) == True
        self.wait_for(self.Game).click()
        self.wait_for(self.GameCarousel)
        assert self.checkElementExists(self.GameCarousel) == True
        self.wait_for(self.Inplay).click()
        self.wait_for(self.InplayMenu)
        assert self.checkElementExists(self.InplayMenu) == True
        self.wait_for(self.Records).click()
        time.sleep(1)
        assert self.checkElementExists(self.RecordsBackIdx) == True
        self.wait_for(self.RecordsBackIdx).click()
        self.wait_for(self.My).click()
        time.sleep(1)
        assert self.checkElementExists(self.MypersonInfo) == True

    def login_click_buttom_tabs(self):
        self.wait_for(self.Index).click()
        assert self.checkElementExists(self.IndexBalls) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}Index.png")
        self.wait_for(self.IndexAnchors).click()
        self.wait_for(self.AnchorPage)
        assert self.checkElementExists(self.AnchorPage) == True
        self.wait_for(self.AnchorBackIndex).click()
        self.wait_for(self.Game).click()
        self.wait_for(self.GameCarousel)
        assert self.checkElementExists(self.GameCarousel) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}Game.png")
        self.wait_for(self.Inplay).click()
        self.wait_for(self.InplayMenu)
        assert self.checkElementExists(self.InplayMenu) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}Inplay.png")
        self.wait_for(self.InplayAnchors).click()
        self.wait_for(self.AnchorPage)
        assert self.checkElementExists(self.AnchorPage) == True
        self.wait_for(self.AnchorBackIndex).click()
        self.wait_for(self.Records).click()
        self.wait_for(self.RecordsOfSport).click()
        self.wait_for(self.SportRecordPage)
        assert self.checkElementExists(self.SportRecordPage) == True
        self.wait_for(self.RecordsOf3rdGame).click()
        self.wait_for(self.ThirdGamePage)
        assert self.checkElementExists(self.ThirdGamePage)
        btnTitle = self.getElementText(self.RecordsOfGame)
        self.wait_for(self.RecordsOfGame).click()
        self.wait_for(self.GamePageTitle)
        pageTitle = self.getElementText(self.GamePageTitle)
        assert btnTitle == pageTitle
        self.wait_for(self.BackToIndex).click()
        self.wait_for(self.My).click()
        self.wait_for(self.MypersonInfo)
        assert self.checkElementExists(self.MypersonInfo) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}My.png")

    def click_sideBar_navLinks(self):
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.SideBarElm)
        assert self.checkElementExists(self.SideBarElm) == True
        self.wait_for(self.BalanceBtn).click()
        self.wait_for(self.BalancSideBar)
        assert self.checkElementExists(self.BalancSideBar) == True
        self.wait_for(self.BalanceBtn).click()
        self.wait_for(self.CouponSumm).click()
        self.wait_for(self.CouponPage)
        assert self.checkElementExists(self.CouponPage) == True
        self.wait_for(self.CouponBtn).click()
        self.wait_for(self.VoucherBtn).click()
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavWallet).click()
        self.wait_for(self.WalletPage)
        assert self.checkElementExists(self.WalletPage) == True
        self.wait_for(self.Index).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavCoupon).click()
        self.wait_for(self.CouponPage)
        assert self.checkElementExists(self.CouponPage) == True
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavTimezone).click()
        self.wait_for(self.TimezonePage)
        assert self.checkElementExists(self.TimezonePage) == True
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavAppDownload).click()
        self.wait_for(self.AppDownloadBtn)
        assert self.checkElementExists(self.AppDownloadBtn) == True
        time.sleep(1)
        self.screenshot(f"{self._screenshot_path}AppDownload.png")
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavPlayRules).click()
        self.wait_for(self.PlayRulesPage)
        assert self.checkElementExists(self.PlayRulesPage) == True
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavCustService).click()
        self.wait_for(self.WelcomeTitle)
        assert self.checkElementExists(self.WelcomeTitle) == True
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavTransaction)
        transText = self.getElementText(self.NavTransaction)
        self.wait_for(self.NavTransaction).click()
        self.wait_for(self.TransTitle)
        transPage = self.getElementText(self.TransTitle)
        assert transText == transPage
        self.wait_for(self.HeaderBack).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavBetRecord).click()
        self.wait_for(self.RecordsOfSport)
        assert self.checkElementExists(self.RecordsOfSport) == True
        self.wait_for(self.Index).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavGameSearch)
        fullname = self.getElementText(self.NavGameSearch)
        self.wait_for(self.NavGameSearch).click()
        self.wait_for(self.GamePageTitle)
        title = self.getElementText(self.GamePageTitle)
        assert title in fullname
        self.wait_for(self.BackToIndex).click()
        self.wait_for(self.HeadIcon).click()
        self.wait_for(self.NavAnchors).click()
        self.wait_for(self.AnchorPage)
        assert self.checkElementExists(self.AnchorPage) == True
        self.wait_for(self.AnchorBackIndex).click()
        self.wait_for(self.HeadIcon).click()
        time.sleep(1)
        self.wait_for(self.NavMyFavorite).click()
        self.wait_for(self.FavoriteElm)
        assert self.checkElementExists(self.FavoriteElm) == True
        self.wait_for(self.FavoriteClose).click()
        self.wait_for(self.HeadIcon).click()
        time.sleep(1)
        self.wait_for(self.NavEventGifts).click()
        self.wait_for(self.EventBanner)
        assert self.getElementCount(self.EventBanner) > 1
        self.wait_for(self.HeaderBack).click()
        time.sleep(1)
