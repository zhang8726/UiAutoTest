'''
单元测试unittest
'''
import unittest

# 必须继承TestCase类
class Test01(unittest.TestCase):

    @classmethod   # 注解
    def setUpClass(self):
        print('*******这是setUpClass方法*******')

    @classmethod
    def tearDownClass(self):
        print('*******这是tearDownClass方法*******')

    # 继承自父类TestCase的方法，名字不能乱写
    # setUp方法会自动在每一个测试用例前执行
    def setUp(self):
        print('*******这是setUp方法*******')

    # tearDown方法会自动在每一个测试用例后执行
    def tearDown(self):
        print('*******这是tearDown方法*******')
        

    # 自定义测试用例
    # 自定义用例方法名必须以test***开头
    # 按照ASCII码表中的字符顺序为优先级别来执行
    def test2(self):
        print('*******这是test2方法-测试用例*******')

    def testabc(self):
        print('*******abc方法*******')

    def testAbc(self):
        print('*******Abc方法*******')

    def test1(self):
        print('*******这是test1方法-测试用例*******')
        
if __name__ == "__main__":
    # Test01().test1()
    unittest.main()