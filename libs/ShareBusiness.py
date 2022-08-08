#coding:utf-8
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Po.LoginPage import LoginPage


# -------------------------------------------------------------------------------
# 函数/过程名称：login_B
# 函数/过程的目的：登录业务函数
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：修才华
# 创建时间：2018/05/27
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def login_B(username="admin",password="admin"):
    obj = LoginPage()
    obj.open_url()
    obj.set_username(username)
    obj.set_password(password)
    obj.click_login_button()
    return obj.dr