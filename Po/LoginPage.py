# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Po.BasePage import BasePage
from BaseInfoConfig import LogMessage
from libs.ShareModules import InsertLog
log=InsertLog()

class LoginPage(BasePage):

    # 元素层
  #  driver.find_element_by_name('username').send_keys('testtestYS')
  #  driver.find_element_by_name('password').send_keys('12345678')

    ipt_username_loc = (By.NAME, "username1")                                                               # 登录用户名
    ipt_password_loc = (By.NAME, "password1")                                                               # 登录密码
    login_button_loc = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/form/button[1]')         # 登录按钮
    txt_success_msg_loc = (By.XPATH, "//span[@class='el-dropdown-link el-dropdown-selfdefine']")     # 登录成功显示testtestYS
    txt_username_error_msg_loc = (By.XPATH, "//p[@class='el-message__content']")                        # 用户名或密码错误

    # 输入用户名
    def set_username(self, username):
        try:
            self.dr.find_element(*self.ipt_username_loc).send_keys(username)
            log.info(u"输入用户名：" + username + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement +username + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入用户名.png")



    # 输入密码
    def set_password(self, password):
        try:
            self.dr.find_element(*self.ipt_password_loc).send_keys(password)
            log.info(u"输入密码：" + password + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement + password + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入密码.png")
            print (msg)


    # 点击登录按钮
    def click_login_button(self):
        try:
            self.dr.find_element(*self.login_button_loc).click()
            log.info("点击登录按钮成功！")
        except BaseException as msg:
            log.error("点击登录按钮失败！")
            self.get_screenshot_as_files(u"点击登录按钮.png")



    # 账号密码为空
    # def get_username_error_msg(self):
    #     WebDriverWait(self.dr, 10, 0.5).until(EC.text_to_be_present_in_element(self.txt_username_error_msg_loc, u"帐号或密码不能为空"))
    #     r = self.dr.find_element(*self.txt_username_error_msg_loc).text
    #     return r

    # 用户名或密码错误
    def get_password_error_msg(self):
        WebDriverWait(self.dr, 10, 0.5).until( EC.text_to_be_present_in_element(self.txt_password_error_msg_loc, u"用户名或密码错误"))
        r = self.dr.find_element(*self.txt_password_error_msg_loc).text
        return r

    # 登录成功
    def get_success_msg(self):
        r = self.dr.find_element(*self.txt_success_msg_loc).text
        return r

     # 登录流程
    def login(self, username,password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

if __name__ == '__main__':
    loginpage=LoginPage()
    loginpage.open_url()
    loginpage.login('testtestYS1','123456781')