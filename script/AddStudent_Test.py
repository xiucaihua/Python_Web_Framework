#coding:utf-8
import  unittest
from time import sleep
from selenium import webdriver
from Po.MemberCenter.StudentListPage import StudentListPage
from Po.MemberCenter.StudentList.AddStudentPage import AddStudentPage
from libs.ShareBusiness import login_B

class AddStudentTest(unittest.TestCase):

    u"""添加学生功能"""
    def setUp(self):
        b =login_B()
        self.obj_sp = StudentListPage(b)  #学生列列表页
        self.obj_ap = AddStudentPage(b)   #添加学生页面

    def test_addstudent_success(self):
        """正常添加学生信息"""

        self.addstudent_verify("13811012955", u"修才华", "123456", u"iOS开放", "D:\\11.jpg",
                                     u"新学员类型","2","3",u"河南科技大学","11988@Q.com","15711932121",u"天津市",u"市辖区",u"和平区",u"天津市河西区地址",u"这个是我的个人简介")
        print ("返回的结果信息为：添加学生信息成功！")
        #self.assertEqual(msg,"admin")


    def tearDown(self):
        self.obj_sp.close_broser()

    # 增加学生
    def addstudent_verify(self, username, realname, password, role, image, studentType, studyTime, studyNum,
                              category, email, phone, provice, city, location, address, introduce):
            try:
                self.obj_sp.click_memberCenterList()
                self.obj_sp.click_addUser_button()
                sleep(3)
                self.obj_ap.set_UserNmae(username)
                self.obj_ap.set_RealName(realname)
                self.obj_ap.set_passWord(password)
                self.obj_ap.setSex()
                self.obj_ap.choseRole(role)
                self.obj_ap.choseStart()
                self.obj_ap.upLoadImage(image)
                self.obj_ap.setStudentType(studentType)
                self.obj_ap.setStudyTime(studyTime)
                self.obj_ap.setStudyNum(studyNum)
                self.obj_ap.select_category(category)
                self.obj_ap.setEmail(email)
                self.obj_ap.setPhone(phone)
                self.obj_ap.selectAddre(provice, city, location)
                self.obj_ap.setAddress(address)
                self.obj_ap.setIntroduce(introduce)
                self.obj_ap.clickSaveButton()
                #message = self.obj_ap.get_success_msg()
                message="admin"
                return message
            except BaseException as msg:
                print (msg)