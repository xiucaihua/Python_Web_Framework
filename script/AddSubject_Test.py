#coding:utf-8
import unittest
from time import sleep
from selenium import webdriver
from libs.ShareBusiness import login_B
from Po.Community.SubjectManger import SubjectManger


class AddSubject(unittest.TestCase):
    u"""主题管理"""

    def setUp(self):
        b = login_B()
        self.object = SubjectManger(b)

    def tearDown(self):
        self.object.close_broser()


    def test_success_addSubject(self):
        """正常添加主题"""
        self.addSubject_verify("mainframe",u"项目管理2",u"新的标题",u"新的活动类型",u"这个是我新增加的描述","D:\\11.jpg",2)
        #print "返回的结果信息为：",result
        #self.assertEqual(result,"admin")
        print ("成功！")



    def addSubject_verify(self,ifram,Plant,title,activeType,description,imagePath,order):
        """正常添加主题"""
        self.object.clickCommunity()
        self.object.clickSubJectManger()
        sleep(3)
        self.object.switchIfram(ifram)
        self.object.addSubject()
        self.object.selectFidPlant(Plant)
        self.object.set_title(title)
        self.object.set_activeType(activeType)
        self.object.set_description(description)
        self.object.uploadImage(imagePath)
        self.object.order(order)
        self.object.goUnderPage()
        self.object.trueAdd()