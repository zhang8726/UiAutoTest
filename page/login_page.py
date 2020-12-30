from base.util import BoxDriver,BasePage,GetYaml

class LoginPage(BasePage):

    config = GetYaml().get(r'D:\workspace\selenium\ranzhi\config\config.yaml')

    def login(self,uname='admin',upwd='123456'):
        '''登录操作流程'''
        driver = self.driver

        # 登录
        driver.input(self.config['LoginPage']['ACCOUNT'],uname)
        driver.input(self.config['LoginPage']['PASSWORD'],upwd)
        driver.click(self.config['LoginPage']['SUBMIT'])

        driver.wait(2)

    def logout(self):
        self.driver.click('p 签退')

    def confirm(self):
        self.driver.click('x /html/body/div[2]/div/div/div[2]/button')
    
    def get_info(self,selector): 
        info = self.driver.locator_element(selector)
        return info.text


if __name__ == "__main__":
    LoginPage(BoxDriver()).login()
