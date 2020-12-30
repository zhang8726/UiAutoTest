# import os,sys
# sys.path.append(os.getcwd())

import unittest
from base.HTMLTestRunner import HTMLTestRunner
import time

class TestRunner:

    def runner_login(self):
        # 实例化测试套件，可以看做一个容器
        # 把部分用例挑选出来，加载到容器中执行
        suite = unittest.TestSuite()
        # 加载用例
        suite.addTests(unittest.TestLoader().discover(r'D:\workspace\selenium\ranzhi\test',pattern='login_test.py'))

        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        path = r'D:\workspace\selenium\ranzhi\report\report_login_%s.html'%timestamp
        # 创建HTML报告文件
        report = open(path,mode='wb')
        # 创建用例运行器，用于运行用例并生成报告
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi登录自动化测试报告',description='报告的详细内容描述...')

        # 运行用例
        test_runner.run(suite)

        report.close()

    def runner_adduser(self):
        # 实例化测试套件，可以看做一个容器
        # 把部分用例挑选出来，加载到容器中执行
        suite = unittest.TestSuite()
        # 加载用例

        suite.addTests(unittest.TestLoader().discover(r'D:\workspace\selenium\ranzhi\test',pattern='adduser_test.py'))

        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        path = r'D:\workspace\selenium\ranzhi\report\report_adduser_%s.html'%timestamp
        # 创建HTML报告文件
        report = open(path,mode='wb')
        # 创建用例运行器，用于运行用例并生成报告
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi添加用户自动化测试报告',description='报告的详细内容描述...')

        # 运行用例
        test_runner.run(suite)

        report.close()

    def runner_addproject(self):
        # 实例化测试套件，可以看做一个容器
        # 把部分用例挑选出来，加载到容器中执行
        suite = unittest.TestSuite()
        # 加载用例

        suite.addTests(unittest.TestLoader().discover(r'D:\workspace\selenium\ranzhi\test',pattern='addproject_test.py'))

        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        path = r'D:\workspace\selenium\ranzhi\report\report_addproject_%s.html'%timestamp
        # 创建HTML报告文件
        report = open(path,mode='wb')
        # 创建用例运行器，用于运行用例并生成报告
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi添加项目自动化测试报告',description='报告的详细内容描述...')

        # 运行用例
        test_runner.run(suite)

        report.close()


if __name__ == "__main__":
    TestRunner().runner()
