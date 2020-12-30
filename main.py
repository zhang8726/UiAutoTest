from runner.test_runner import TestRunner


class Main:

    def start(self):
        TestRunner().runner_login()
        # TestRunner().runner_adduser()
        # TestRunner().runner_addproject()




if __name__ == "__main__":
    '''整个自动化测试代码入口'''
    Main().start()
     