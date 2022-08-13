#coding:utf-8
import unittest
from Po.LoginPage import LoginPage
from untils.excelTools import ReadExcel
from time import sleep
from ddt import ddt, data, unpack
from untils.red_excel import redExcel
import time
from HTMLTestRunner import HTMLTestRunner
from untils.operatioJson import readJson
from untils.operatioyaml import readYaml


#@ddt
class testloginCase(unittest.TestCase):
    u"""登录功能"""

    def setUp(self):
        self.obj = LoginPage()
        self.obj.open_url()


    def tearDown(self):
        self.obj.close_broser()

    #普通数据写法
    # def test_sucess_login_001(self):
    #     """正确用户密码登录"""
    #     self.obj.login("testtestYS","12345678")
    #     r=self.obj.get_success_msg()
    #     self.assertEqual(r,"testtestYS")

    #excel数据驱动写法(正常)
    # def test_sucess_login_true(self):
    #     """正常登录"""
    #     self.obj.login(redExcel()[1][0],redExcel()[1][1])
    #     r = self.obj.get_success_msg()
    #     self.assertEqual(r,redExcel()[1][2])

    #excel数据驱动写法(正常)
    # @data(*ReadExcel().get_data("D:\\test.xlsx",0))
    # @unpack
    # def test_sucess_login_true(self,username,password,expectResults):
    #     """正常登录"""
    #     self.obj.login(username,password)
    #     r = self.obj.get_success_msg()
    #     print("预期与实际结果为：",r,expectResults)
    #     self.assertEqual(r,expectResults, msg="测试成功！")


    #excel数据驱动写法(正常)
    # @data(*ReadExcel().get_data("D:\\test.xlsx",1))
    # @unpack
    # def test_Faill_login(self,username,password,expectResults):
    #     """登录失败验证"""
    #     self.obj.login(username,password)
    #     r = self.obj.get_password_error_msg()
    #     print("预期与实际结果为：",r,expectResults)
    #     self.assertEqual(r,expectResults, msg="测试成功！")

    # 读取json数据格式写法
    # def test_loginError_001(self):
    #     """用户名或密码错误1"""
    #     self.obj.login(readJson()['loginError1']['username'],readJson()['loginError1']['password'])
    #     r=self.obj.get_password_error_msg()
    #     self.assertEqual(r,readJson()['loginError1']['result'])

    # 读取json数据格式写法
    # def test_loginError_002(self):
    #     """用户名或密码错误2"""
    #     self.obj.login(readJson()['loginError2']['username'],readJson()['loginError2']['password'])
    #     r=self.obj.get_password_error_msg()
    #     self.assertEqual(r,readJson()['loginError2']['result'])

    # 读取json数据格式写法
    # def test_loginError_003(self):
    #     """用户名或密码错误3"""
    #     self.obj.login(readJson()['loginError3']['username'],readJson()['loginError3']['password'])
    #     r=self.obj.get_password_error_msg()
    #     self.assertEqual(r,readJson()['loginError3']['result'])



    # 读取yaml数据格式写法
    def test_loginError_001(self):
        """用户名或密码错误1"""
        self.obj.login(readYaml()['loginError1']['username'],readYaml()['loginError1']['password'])
        r=self.obj.get_password_error_msg()
        self.assertEqual(r,readYaml()['loginError1']['result'])

    # 读取yaml数据格式写法
    def test_loginError_002(self):
        """用户名或密码错误2"""
        self.obj.login(readYaml()['loginError2']['username'],readYaml()['loginError2']['password'])
        r=self.obj.get_password_error_msg()
        self.assertEqual(r,readYaml()['loginError2']['result'])

    # 读取yaml数据格式写法
    def test_loginError_003(self):
        """用户名或密码错误3"""
        self.obj.login(readYaml()['loginError3']['username'],readYaml()['loginError3']['password'])
        r=self.obj.get_password_error_msg()
        self.assertEqual(r,readYaml()['loginError3']['result'])

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(testloginCase("test_Faill_login"))
#    # suite.addTest(testloginCase("test_sucess_login_true"))
#     currenttime = time.strftime('%Y-%m-%d-%H-%M-%S ')
#     fp = open("../" + currenttime + "_report" + ".html", "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='宇达MES系统登录功能 ', description='执行人：修才华', tester="修才华")
#     runner.run(suite)

