# coding:utf-8
from selenium import webdriver
from time import sleep
from  selenium.webdriver.support.select import Select
from BaseInfoConfig import BaseInfoCofig
from BaseInfoConfig import BasePathConfig
from BaseInfoConfig import LogMessage
import time
import os
from libs.ShareModules import InsertLog
log=InsertLog()

class BasePage():

    def __init__(self, driver=''):
        b = driver
        if b == '':
            self.dr = self.create_browser()
            log.info("创建浏览器对象成功!")
        else:
            self.dr = b
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

    #创建浏览器
    def create_browser(self, b='g'):
        if b == 'g':
            d = webdriver.Chrome(BasePathConfig.ChomedriverPath)
            log.info("创建谷歌浏览器对象成功!")
        elif b == 'f':
            d = webdriver.Firefox()
            log.info("创建火狐浏览器对象成功!")
        return d

    #打开访问地址
    def open_url(self, url=BasePathConfig.baseUrl):
        try:
            self.dr.get(url)
            log.info("打开"+url+LogMessage.Pass)
        except BaseException as msg:
            print (msg)




    #关闭浏览器
    def close_broser(self):
        try:
            if self.dr!=None:
                self.dr.quit()
                log.info("关闭浏览器对象成功！")
        except BaseException as msg:
            print (msg)




    """
    功能描述：截图功能
    创建者：修才华
    创建时间：2018/06/06
    """
    def get_screenshot_as_files(self, imageNmae, imagePath=BasePathConfig.imagePath):
        try:
            self.dr.get_screenshot_as_file(imagePath+imageNmae)
            log.info("截图方法调用---成功！")
        except BaseException as msg:
            log.error("截图方法调用--失败！")
            print (msg)


     #返回操作
    def goBack(self):
        self.dr.back()
        log.info("返回成功！")


    #刷新操作
    def Refresh(self):
        self.dr.refresh()
        log.info("刷新操作成功！")

    # 前进操作
    def forWard(self):
        self.dr.forward()
        log.info("前进操作成功！")


    #隐式等待
    def new_implicitly_wait(self,time_to_wait):
        self.dr.implicitly_wait(time_to_wait)

    #sleep等待
    def new_Sleep(self,time):
        try:
            sleep(time)
        except Exception as msg:
            print (msg)

    # 获取当前的URL
    def ger_current_url(self):
        return self.dr.current_url
        log.info("获取到当前"+dr.current_url+LogMessage.Pass)

    #滚动条到底部
    def goUnderPage(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.dr.execute_script(js)
        log.info("滚动条拖动到底部！")

    # 执行js拖拽，拖拽到顶部
    def goTopPage(self):
        js = "window.scrollTo(0,0)"
        self.dr.execute_script(js)
        log.info("滚动条拖动到顶部！")