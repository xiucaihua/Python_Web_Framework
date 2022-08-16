#coding:utf-8
import  unittest
from time import sleep
from selenium import webdriver
from Po.LoginPage import LoginPage
from Po.home_page import HomePage
from libs.ShareBusiness import login_B
from time import sleep

class HomePageTest(unittest.TestCase):

    u"""创建工单"""
    def setUp(self):
        b =login_B()
        self.obj_hp = HomePage(b)  #系统home页面
        sleep(5)
        self.obj_hp.click_system_button()
        sleep(5)
        self.obj_hp.click_production_management_menu()
        sleep(5)
        self.obj_hp.click_workorder_management_menu()
        sleep(5)
        self.obj_hp.click_add_button()
        sleep(5)
        self.obj_hp.input_productName("UBS")
        self.obj_hp.select_workorder_type()
        sleep(2)
        self.obj_hp.select_process_type()
        self.obj_hp.input_needs_number(10)
        self.obj_hp.input_stcok_number(2)
        self.obj_hp.input_ead_storage_number(2)
        sleep(10)




    def test_success_addSubject(self):
        """创建工单"""
        pass
        #self.addWorkOrder("USB",10,2,2)

    # def tearDown(self):
    #     self.obj_hp.close_broser()

    def addWorkOrder(self,productName,needs_number,stcok_number,storageNumber):
        """新建工单"""
        try:
            self.obj_hp.click_system_button()
            sleep(3)
            self.obj_hp.click_production_management_menu()
            sleep(3)
            self.obj_hp.click_workorder_management_menu()
            sleep(3)
            self.obj_hp.click_add_button()
            sleep(3)
            self.obj_hp.input_productName(productName)
            self.obj_hp.select_workorder_type()
            self.obj_hp.select_process_type()
            self.obj_hp.input_needs_number(needs_number)
            self.obj_hp.input_stcok_number(stcok_number)
            self.obj_hp.input_ead_storage_number(storageNumber)
        except BaseException as msg:
            print(msg)