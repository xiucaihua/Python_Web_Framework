#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import  By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
from Po.LoginPage import LoginPage
from Po.BasePage import BasePage
from libs.ShareModules import InsertLog
from BaseInfoConfig import LogMessage
log=InsertLog()

class AddStudentPage(BasePage):
    u"""添加学生页"""

    username_loc = (By.NAME, "username")  # 账号
    realNmae_loc = (By.NAME, "realname")  # 昵称
    password_loc = (By.NAME, "password")  # 密码
    choseSexButton_loc = (By.XPATH, "//*[@id='form']/div/div[4]/div/label[3]/input")  # 选择性别单选按钮
    choseRole_select_loc = (By.NAME, "roleid")  # 选择角色
    start_checkbox_loc = (By.ID, "isstart")  # 选择明星
    upLoadImg_loc = (By.XPATH, "//*[@id='form']/div/div[7]/div/a/span")  # 上传图片
    upLoadLocal_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]")  # 本地上传
    browerImage_loc = (By.NAME, "imgFile")  # 浏览图片
    trueButton_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[3]/span[1]/input")  # 确认按钮
    startname_loc = (By.NAME, "startname")  # 学员类型
    studytime_loc = (By.NAME, "studytime")  # 学习时间
    studynum_loc = (By.NAME, "studynum")  # 报名课程数
    select_category_loc = (By.NAME, "orid1")  # 选择机构
    emali_loc = (By.NAME, "email")  # 邮箱
    phone_loc = (By.NAME, "phone")  # 手机
    select_provice_loc = (By.NAME, "location_p")  # 选择省份
    select_city_loc = (By.NAME, "location_c")  # 市县
    select_location_loc = (By.NAME, "location_a")  # 区域
    address_loc = (By.NAME, "address")  # 详细地址
    introduce_loc = (By.NAME, "introduce")  # 个人简介
    true_sava_loc = (By.XPATH, "//*[@id='btn_sub']/span")  # 确认保存
    txt_success_msg_loc = (By.XPATH, ".//*[@id='header']/p/span[1]/strong")  # 登录成功admin
    txt_username_error_msg_loc = (By.ID, "username_msg")  # 用户名错误
    txt_password_error_msg_loc = (By.ID, "password_msg")  # 密码错误
    sex_checkBox_man_loc = (By.XPATH, "//*[@id='form']/div/div[4]/div/label[1]/input")  # 单选男
    sex_checkBox_woman_loc = (By.XPATH, "//*[@id='form']/div/div[4]/div/label[2]/input")  # 单选女
    sex_checkBox_secret_loc = (By.XPATH, "//*[@id='form']/div/div[4]/div/label[3]/input")  # 保密

    # 输入账号
    def set_UserNmae(self, userName):
        try:
            self.dr.find_element(*self.username_loc).send_keys(userName)
            #log.info(LogMessage.findElement+userName+LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + userName + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入账号_error.png")
            print msg



    # 输入昵称
    def set_RealName(self,realName):
        try:
            self.dr.find_element(*self.realNmae_loc).send_keys(realName)
            #log.info(LogMessage.findElement + realName + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + realName + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入昵称_error.png")
            print msg


    # 输入密码信息
    def set_passWord(self,passWord):
        try:
            self.dr.find_element(*self.password_loc).send_keys(passWord)
            #log.info(LogMessage.findElement + passWord + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + passWord + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入密码_error.png")
            print msg



    # 选择性别
    def setSex(self, value="保密"):
        if value == "男":
            self.dr.find_element(*self.sex_checkBox_man_loc).click()
        elif value == "女":
            self.dr.find_element(*self.sex_checkBox_woman_loc).click()
        else:
            self.dr.find_element(*self.sex_checkBox_secret_loc).click()

    # 选择角色
    def choseRole(self, roleName):
        try:
            select = self.dr.find_element(*self.choseRole_select_loc)
            Select(select).select_by_visible_text(roleName)
            #log.info(LogMessage.findElement + roleName + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + roleName + LogMessage.Fail)
            self.get_screenshot_as_files(u"选择角色_error.png")
            print msg



    # 选中明星
    def choseStart(self):
        if self.dr.find_element(*self.start_checkbox_loc).is_selected():
            print u"角色已经被选中"
        else:
            self.dr.find_element(*self.start_checkbox_loc).click()

    # 上传图片
    def upLoadImage(self, imagePath):
        try:
            self.dr.find_element(*self.upLoadImg_loc).click()
            self.dr.find_element(*self.upLoadLocal_loc).click()
            self.dr.find_element(*self.browerImage_loc).send_keys(imagePath)
            self.dr.find_element(*self.trueButton_loc).click()
            #log.info(LogMessage.findElement + imagePath + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + imagePath + LogMessage.Fail)
            self.get_screenshot_as_files(u"上传图片_error.png")
            print msg



    # 设置学员类型
    def setStudentType(self, studentType):
        try:
            self.dr.find_element(*self.startname_loc).send_keys(studentType)
            #log.info(LogMessage.findElement + studentType + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + studentType + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置学员类型_error.png")
            print msg



    # 设置学习时间
    def setStudyTime(self, studyTime):
        try:
            self.dr.find_element(*self.studytime_loc).send_keys(studyTime)
            #log.info(LogMessage.findElement + studyTime + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + studyTime + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置学习时间_error.png")
            print msg


    # 设置报名课程数
    def setStudyNum(self, studynum):
        try:
            self.dr.find_element(*self.studynum_loc).send_keys(studynum)
            #log.info(LogMessage.findElement + studynum + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + studynum + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置报名课程数_error.png")
            print msg



    # 选择机构
    def select_category(self, category):
        try:
            self.dr.find_element(*self.select_category_loc).send_keys(category)
            #log.info(LogMessage.findElement + category + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + category + LogMessage.Fail)
            self.get_screenshot_as_files(u"选择机构_error.png")
            print msg



    # 设置邮箱
    def setEmail(self, email):
        try:
            self.dr.find_element(*self.emali_loc).send_keys(email)
            #log.info(LogMessage.findElement + email + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + email + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置邮箱_error.png")
            print msg


    # 设置手机号码
    def setPhone(self, phone):
        try:
            self.dr.find_element(*self.phone_loc).send_keys(phone)
            #log.info(LogMessage.findElement + phone + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + phone + LogMessage.Fail)
            self.get_screenshot_as_files(u"设置手机号码_error.png")
            print msg


    # 地址选择
    def selectAddre(self, provice, city, location):
        try:
            proviceSelect = self.dr.find_element(*self.select_provice_loc)
            Select(proviceSelect).select_by_visible_text(provice)
            #log.info(LogMessage.findElement + provice + LogMessage.Pass)

            citySelect = self.dr.find_element(*self.select_city_loc)
            Select(citySelect).select_by_visible_text(city)
            #log.info(LogMessage.findElement + city + LogMessage.Pass)

            selectLocation = self.dr.find_element(*self.select_location_loc)
            Select(selectLocation).select_by_visible_text(location)
            #log.info(LogMessage.findElement + location + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + provice+city+location+ LogMessage.Fail)
            self.get_screenshot_as_files(u"地址选择_error.png")
            print msg



    # 设置详细地址
    def setAddress(self, address):
        try:
            self.dr.find_element(*self.address_loc).send_keys(address)
            #log.info(LogMessage.findElement + address + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + address + LogMessage.Fail)
            self.get_screenshot_as_files(u" 设置详细地址_error.png")
            print msg


    # 设置个人简介
    def setIntroduce(self, introduce):
        try:
            self.dr.find_element(*self.introduce_loc).send_keys(introduce)
            #log.info(LogMessage.findElement + introduce + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + introduce+ LogMessage.Fail)
            self.get_screenshot_as_files(u"设置个人简介_error.png")
            print msg



    # 点击保存按钮
    def clickSaveButton(self):
        try:
            self.dr.find_element(*self.true_sava_loc).click()
            #log.info(LogMessage.findElement +self.true_sava_loc + LogMessage.Pass)
        except BaseException as msg:
            #log.error(LogMessage.findElement + self.true_sava_loc + LogMessage.Fail)
            self.get_screenshot_as_files(u"点击保存按钮_error.png")
            print msg



    # # 登录成功
    # def get_success_msg(self):
    #     r = self.dr.find_element(*self.txt_success_msg_loc).text
    #     return r