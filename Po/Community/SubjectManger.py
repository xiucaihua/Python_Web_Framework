#coding:utf-8
from time import sleep
from Po.BasePage import BasePage
from selenium.webdriver.common.by import By
from Po.LoginPage import LoginPage
from libs.ShareBusiness import login_B
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libs.ShareModules import InsertLog
from BaseInfoConfig import LogMessage
log=InsertLog()

class SubjectManger(BasePage):

    #主题管理对象层
    community_loc=(By.XPATH,"//*[@id='header']/ul/li[1]/a")                                       #社区
    subjectManger_loc=(By.LINK_TEXT,u"主题管理")                                                  #主题管理
    mainfram_loc=(By.NAME,"mainframe")                                                              #iframe
    addSubject_loc=(By.CSS_SELECTOR,"a.btn-general:nth-child(1)")                                 #添加
    selectfidplant_loc=(By.ID,"fidplant")                                                         #选择板块
    title_loc=(By.ID,"title")                                                                     #标题
    activeType_loc=(By.NAME,"data[descr]")                                                        #活动类型
    description_loc=(By.NAME,"data[sketch]")                                                      #简述
    uploadImageButton_loc=(By.XPATH,"//*[@id='form']/div/div[7]/div/a/span")                      #上传图片
    localUpload_loc=(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div/div[1]/ul/li[2]")              #本地上传
    imgFile_loc=(By.NAME,"imgFile")                                                               #浏览
    trueButton_loc=(By.XPATH,"//input[@class='ke-button-common ke-button' and @value='确定']")    #确定
    dataLmorder_loc=(By.ID,"data[lmorder]")                                                       #排序
    trueAddButton_loc=(By.CSS_SELECTOR,".btn-area .btn-general span")                             #确认添加



    #点击社区菜单
    def clickCommunity(self):
        try:
            self.dr.find_element(*self.community_loc).click()
            self.get_screenshot_as_files(u"社区菜单.png")
            log.info(LogMessage.findElement + "社区菜单" + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement +"社区菜单" + LogMessage.Fail)
            self.get_screenshot_as_files(u"社区菜单_error.png")
            print msg

    #主题管理
    def clickSubJectManger(self):
        try:
            self.dr.find_element(*self.subjectManger_loc).click()
            log.info(LogMessage.findElement+"主题管理"+LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement + "主题管理" + LogMessage.Fail)
            self.get_screenshot_as_files(u"主题管理_error.png")
            print msg


    # 切换到列表的ifram
    def switchIfram(self,ifram):
        try:
            self.dr.find_element(*self.mainfram_loc)
            self.dr.switch_to_frame(ifram)
            log.infor(LogMessage.findElement + "切换到列表的ifram" + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement + "切换到列表的ifram" + LogMessage.Fail)
            self.get_screenshot_as_files(u"切换列表ifram_error.png")
            print msg



    #点击添加主题按钮
    def addSubject(self):
        try:
            # WebDriverWait(self.dr, 10, 0.5).until(EC.text_to_be_present_in_element(self.addSubject_loc))
            self.dr.find_element(*self.addSubject_loc).click()
            log.infor(LogMessage.findElement + "添加主题按钮" + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement + "添加主题按钮" + LogMessage.Fail)
            self.get_screenshot_as_files(u"添加主题按钮_error.png")
            print msg


    #选择板块
    def selectFidPlant(self,selectText):
        try:
            select = self.dr.find_element(*self.selectfidplant_loc)
            Select(select).select_by_visible_text(selectText)
            log.info("选择板块"+selectText+LogMessage.Pass)
        except BaseException as msg:
            #log.error("选择板块" + selectText + LogMessage.Fail)
            self.get_screenshot_as_files(u"选择板块_error.png")
            print msg


    #标题
    def set_title(self,titleName):
        try:
            self.dr.find_element(*self.title_loc).send_keys(titleName)
            log.info(u"输入标题：" + titleName + LogMessage.Pass)
        except BaseException as msg:
            #log.error(u"输入标题：" + titleName + LogMessage.Fail)
            self.get_screenshot_as_files(u"标题_error.png")
            print msg



    #活动类型
    def set_activeType(self,activeTypeName):
        try:
            self.dr.find_element(*self.activeType_loc).send_keys(activeTypeName)
            #log.info("输入活动类型：" + activeTypeName + LogMessage.Pass)
        except BaseException as msg:
            #log.error("输入活动类型：" + activeTypeName+ LogMessage.Fail)
            self.get_screenshot_as_files(u"活动类型_error.png")
            print msg




    #设置简述
    def set_description(self,description):
        try:
            self.dr.find_element(*self.description_loc).send_keys(description)
            #log.info("设置简述：" + description + LogMessage.Pass)
        except BaseException as msg:
            #log.error("设置简述：" + description + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置简述_error.png")
            print msg



    #上传图片
    def uploadImage(self,imagePath):
        try:
            self.dr.find_element(*self.uploadImageButton_loc).click()
            self.dr.find_element(*self.localUpload_loc).click()
            self.dr.find_element(*self.imgFile_loc).send_keys(imagePath)
            self.dr.find_element(*self.trueButton_loc).click()
            #log.info("上传图片：" + imagePath + LogMessage.Pass)
        except BaseException as msg:
            #log.error("上传图片：" + imagePath + LogMessage.Fail)
            self.get_screenshot_as_files(u"上传图片_error.png")
            print msg


    #排序
    def order(self,orderNumber):
        try:
            self.dr.find_element(*self.dataLmorder_loc).send_keys(orderNumber)
            #log.info(u"设置排序：" + orderNumber + LogMessage.Pass)
        except BaseException as msg:
            #log.info(u"设置排序：" + orderNumber + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置排序_error.png")
            print msg


    #确认添加
    def trueAdd(self):
        try:
            self.dr.find_element(*self.trueAddButton_loc).click()
            #log.info(u"点击确认添加按钮"  + LogMessage.Pass)
        except BaseException as msg:
            #log.info(u"点击确认添加按钮：" + LogMessage.Fail)
            self.get_screenshot_as_files(u"确认添加_error.png")
            print msg