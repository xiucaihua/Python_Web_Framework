#coding:utf-8
import unittest
from Po.LoginPage import LoginPage

class testloginCase(unittest.TestCase):
    u"""登录功能"""

    def setUp(self):
        self.obj=LoginPage()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_broser()

    def test_sucess_login_001(self):
        """正确用户密码登录"""
        self.obj.login("admin","admin")
        r=self.obj.get_success_msg()
        self.assertEqual(r,"admin")


    def test_username_emty_login_002(self):
        """用户名为空登录"""
        self.obj.login("","admin")
        r=self.obj.get_username_error_msg()
        self.assertEqual(r,u'帐号或密码不能为空')


    def test_password_emty_login_003(self):
        """ 密码为空登录"""
        self.obj.login("admin","")
        r=self.obj.get_username_error_msg()
        self.assertEqual(r,u'帐号或密码不能为空')

    def test_username_error_login_004(self):
        """ 密码错误"""
        self.obj.login("admin1","admin")
        r=self.obj.get_password_error_msg()
        self.assertEqual(r,u'密码错误')

    def test_username_error_login_005(self):
        """ 账户密码为空"""
        self.obj.login("","")
        r=self.obj.get_username_error_msg()
        self.assertEqual(r,u'帐号或密码不能为空')