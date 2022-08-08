#coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Po.BasePage import BasePage
from libs.ShareModules import InsertLog
from BaseInfoConfig import LogMessage
log=InsertLog()

class StudentListPage(BasePage):
    u"""学生列表页"""

    memberCenter_loc=(By.XPATH,"//*[@id='header']/ul/li[3]/a")                        #会员中心
    addUserButton_ifram=(By.ID,"mainframe")                                           #添加学生ifram
    addUserButton_loc=(By.XPATH,"/html/body/div[2]/h3/a[2]/span")                     #添加学生

    # 点击会员列表
    def click_memberCenterList(self):
        try:
            self.dr.find_element(*self.memberCenter_loc).click()
            #log.info(LogMessage.findElement+self.memberCenter_loc+LogMessage.Pass)
        except BaseException as msg:
            #log.info(LogMessage.findElement + self.memberCenter_loc + LogMessage.Fail)
            self.get_screenshot_as_files("会员列表_error.png")
            print msg


    # 点击添加学生
    def click_addUser_button(self):
        mainifram = self.dr.find_element(*self.addUserButton_ifram)
        self.dr.switch_to_frame(mainifram)
        self.dr.find_element(*self.addUserButton_loc).click()