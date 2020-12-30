from parameterized import parameterized
from page.login_page import LoginPage
from page.adduser_page import AddUser
from base.util import BoxDriver,GetExcel,GetLogger
import unittest

class AddUserTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.logger = GetLogger(r'D:\workspace\selenium\ranzhi\report\ranzhi_adduser.log')
        addUser = AddUser(self.driver)
        addUser.login()
        self.logger.info('登录完毕！')
        addUser.switch_to()
        self.addUser = addUser

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.logger.info('执行完毕！')

    def tearDown(self):
        self.addUser.add_user_again()
        self.logger.info('添加下一个用户！')

    

    @parameterized.expand(GetExcel().get(r'D:\workspace\selenium\ranzhi\config\data.xlsx','adduser_success'))
    def test_adduser_seccess(self,username,realname,email):
        '''添加用户成功用例'''
        addUser = self.addUser
        addUser.add_user(username,realname,email)
        self.logger.info('添加用户完毕！')
        realname_get = addUser.get_realname('x /html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        self.assertEqual(realname_get,realname,'添加用户成功用例失败')
        self.logger.info('断言完毕！')



if __name__ == "__main__":
    unittest.main()