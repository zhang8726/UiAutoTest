import unittest
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetLogger
from parameterized import parameterized

class LoginTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.page = LoginPage(self.driver)
        self.logger = GetLogger(r'D:\workspace\selenium\ranzhi\report\ranzhi_login.log')
        self.logger.info('打开浏览器，输入网址完毕！')
    @classmethod
    def tearDownClass(self):
        self.driver.close()

    # 用例参数化
    @parameterized.expand(GetExcel().get(r'D:\workspace\selenium\ranzhi\config\data.xlsx','login_success'))
    def test_login_success(self,uname,upwd,realname1):
        try:
            '''登录成功功能测试用例'''
            page = self.page

            page.login(uname,upwd)
            self.logger.info('登录完毕！')

            # 断言
            realname2 = page.get_info('x //*[@id="mainNavbar"]/div/ul[1]/li/a')
            self.assertEqual(realname1,realname2,'登录成功测试用例失败')
            self.logger.info('断言成功！')
            # page.logout()
        except:
            raise NameError('登录成功功能测试用例失败')
        finally:
            page.logout()   
            self.logger.info('退出成功！')
            

    @parameterized.expand(GetExcel().get(r'D:\workspace\selenium\ranzhi\config\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd,realname):
        try:
            '''登录失败功能测试用例'''
            page = self.page
            page.login(uname,upwd)
            self.logger.info('登录完成！')
            # 断言
            text = page.get_info('x /html/body/div[2]/div/div/div[2]/button')
            self.assertEqual(text,'确认','登录失败测试用例失败')
            self.logger.info('断言成功！')
        except:
            raise NameError('登录失败功能测试用例失败')
        finally:
            page.confirm()
            self.logger.info('点击确认按钮！')

if __name__ == "__main__":
    unittest.main()