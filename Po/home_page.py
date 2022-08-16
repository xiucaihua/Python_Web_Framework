#coding:utf-8
from Po.BasePage import BasePage
from selenium.webdriver.common.by import By
from libs.ShareModules import InsertLog
from BaseInfoConfig import LogMessage
from selenium import webdriver
from time import sleep
log=InsertLog()

class HomePage(BasePage):
    """数字工厂首页"""
    sys_button_loc=(By.XPATH,"//button[@class='el-button el-button--primary el-button--medium']")   #进入系统按钮
    production_management_menu_loc=(By.XPATH,"(//div[@class='el-submenu__title'])[2]")                      #生产管理菜单
    workorder_management_menu_loc=(By.XPATH,"//span[contains(text(), '工单管理')]")                          #工单管理
    add_button_loc=(By.XPATH,"//button[@class='el-button fr el-button--success']")                         #新增按钮
    ipt_productName_loc=(By.XPATH,"(//input[@class='el-input__inner'])[2]")                                 #产品名称
    workorder_type_loc=(By.XPATH,"(//input[@class='el-input__inner'])[3]")                                  #工单类型下拉
    workorder_type_true_loc=(By.XPATH,"//span[contains(text(), '正常')]")                                     #工单类型-正常
    process_type_loc=(By.XPATH,"(//input[@class='el-input__inner'])[4]")                                     #工艺类型下拉选项
    stamping_process_type_loc=(By.XPATH,"//span[contains(text(), '冲压工艺')]")                               # 选择【冲压工艺】
    ipt_needs_number_loc=(By.XPATH,"(//input[@class='el-input__inner'])[5]")                                 # 清空需求数量
    ipt_stcok_loc=(By.XPATH,"(//input[@class='el-input__inner'])[6]")                                        #库存数量
    ipt_dead_storage_loc=(By.XPATH,"(//input[@class='el-input__inner'])[8]")                                 #备货数量

    ipt_username_loc = (By.NAME, "username")  # 登录用户名
    ipt_password_loc = (By.NAME, "password")

    def set_username(self,username):
        try:
            self.dr.find_element(*self.ipt_username_loc).send_keys(username)
            log.info(u"输入用户名：" + username + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement +username + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入用户名.png")


    def click_system_button(self):
        """点击进入到系统"""
        self.dr.find_element(*self.sys_button_loc).click()
        log.info(u"点击进入系统按钮："  + LogMessage.Pass)

    def click_production_management_menu(self):
        """点击生产管理"""
        windows = self.dr.window_handles
        self.dr.switch_to_window(windows[1])
        self.dr.find_element(*self.production_management_menu_loc).click()
        log.info(u"点击生产管理菜单："  + LogMessage.Pass)

    def click_workorder_management_menu(self):
        """点击工单管理"""
        self.dr.find_element(*self.workorder_management_menu_loc).click()
        log.info(u"点击工单管理菜单："  + LogMessage.Pass)

    def click_add_button(self):
        """点击新增按钮"""
        self.dr.find_element(*self.add_button_loc).click()
        log.info(u"点击新增按钮：" + LogMessage.Pass)

    def input_productName(self,productName):
        """输入产品名称"""
        self.dr.find_element(*self.ipt_productName_loc).send_keys(productName)
        log.info(u"输入产品名称："  + LogMessage.Pass)

    def select_workorder_type(self):
        """选择工单类型"""
        self.dr.find_element(*self.workorder_type_loc).click()
        log.info(u"点击工单类型输入框："  + LogMessage.Pass)
        sleep(3)
        self.dr.find_element(*self.workorder_type_true_loc).click()
        log.info(u"选择正常："  + LogMessage.Pass)

    def select_process_type(self):
        """选择工艺类型"""
        self.dr.find_element(*self.process_type_loc).click()
        log.info(u"点击工艺类型输入框：" + LogMessage.Pass)
        sleep(3)
        self.dr.find_element(*self.stamping_process_type_loc).click()
        log.info(u"选择正常冲压工艺："  + LogMessage.Pass)

    def input_needs_number(self,needs_number):
        """输入需求数量"""
        self.dr.find_element(*self.ipt_needs_number_loc).send_keys(needs_number)
        log.info(u"输入库存数量："  + LogMessage.Pass)

    def input_stcok_number(self,stcok_number):
        """输入库存数量"""
        self.dr.find_element(*self.ipt_stcok_loc).send_keys(stcok_number)
        log.info(u"输入库存数量："  + LogMessage.Pass)

    def input_ead_storage_number(self,storageNumber):
        """输入备货数量"""
        self.dr.find_element(*self.ipt_dead_storage_loc).send_keys(storageNumber)
        log.info(u"输入备货数量：" + LogMessage.Pass)