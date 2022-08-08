# coding:utf-8
import os,time,HTMLTestRunner
import unittest
from script.AddStudent_Test import AddStudentTest
from script.Login_Test import testloginCase
from script.AddSubject_Test import AddSubject
from libs.ShareModules import SendEmail,GetNewReport


class MainTest():
    """执行测试类里面指定case"""
    if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(testloginCase("test_sucess_login_001"))
        suite.addTest(testloginCase("test_username_emty_login_002"))
        suite.addTest(testloginCase("test_password_emty_login_003"))
        suite.addTest(testloginCase("test_username_error_login_004"))
        suite.addTest(testloginCase("test_username_error_login_005"))
        suite.addTest(AddStudentTest("test_addstudent_success"))
        suite.addTest(AddSubject("test_success_addSubject"))


        currenttime = time.strftime('%Y-%m-%d-%H-%M-%S ')
        fp = open("C:\\Users\\Andrew\\PycharmProjects\\FramWork\\report\\" + currenttime+"_report"+ ".html", "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录增加学生自动化测试报告 ', description='执行人：修才华',tester="修才华")
        runner.run(suite)
        #f = GetNewReport()
        #SendEmail('pythondldysl01@163.com', 'wxqcl258258',"651552390@QQ.com","smtp.163.com", f, 25)
        fp.close()

        # 第三种方式执行
        # case_path = os.path.join(os.getcwd(), "C:\\Users\\Andrew\\PycharmProjects\\Day2\\Day6\\")
        # runner = unittest.TextTestRunner(verbosity=2)
        # discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

        #  now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        #  fp = open("C:\\Users\\Andrew\\PycharmProjects\\Day2\\report\\" + now + ".html", "wb")
        # # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试 ', description="系统自动化测试报告")
        #  runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test ', description="test")
        #  runner.run(discover)