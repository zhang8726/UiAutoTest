from parameterized import parameterized
import unittest
from page.login_page import LoginPage
from page.addproject_page import AddProject
from base.util import BoxDriver,GetExcel,GetLogger

class AddProject:

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.logger = GetLogger(r'D:\workspace\selenium\ranzhi\report\ranzhi_addproject.log')
        addproject = AddProject(self.driver)
        addproject.login()
        self.logger.info('登录完毕！')
        addproject.switch_to()
        self.addproject = addproject

    def setUp(self):
        self.addproject.add_project_start()
        self.logger.info('添加任务开始！')

    def tearDown(slef):
        self.logger.info('添加任务结束！')

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.logger.info('执行完毕！')

    @parameterized.expand(GetExcel().get(r'D:\workspace\selenium\ranzhi\config\data.xlsx','addproject_success'))   
    def test_project(self,name):
        '''添加项目用例'''
        addproject = self.addproject
        # 添加项目
        addproject.add_project(name)
        # 断言 
        dataname = addproject.get_dataname('x //*[@id="dashboard"]/div[1]/div/div[1]')
        self.assertEqual(dataname,name,'添加项目用例失败')
        self.logger.info('断言完毕！')


if __name__ == "__main__":
    AddProject().add_project()