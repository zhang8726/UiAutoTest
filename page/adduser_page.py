import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage

class AddUser(LoginPage):

    def switch_to(self):
        driver = self.driver
        # 添加成员
        driver.click('x //*[@id="s-menu-superadmin"]/button')
        # 切换到frame中
        driver.switch_to_frame('id iframe-superadmin')
        driver.click('x //*[@id="shortcutBox"]/div/div[1]/div/a')
        driver.wait(2)

    def add_user(self,username,realname,email): 
        driver = self.driver         
        driver.input('id account',username)
        driver.input('id realname',realname)
        driver.click('id '+['genderm','genderf'][random.randint(0,1)])
        driver.select_by_index('id dept',random.randint(1,6))
        driver.select_by_index('id role',random.randint(1,16))
        driver.input('id password1','123456')
        driver.input('id password2','123456')
        driver.input('id email',email)
        driver.click('id submit')
        driver.wait(1)

    def get_realname(self,selector):
            driver = self.driver
            # 跳转到最后一页
            driver.input('id _pageID','100')
            driver.click('id goto')
            driver.wait(2)
            # 断言
            accounts = driver.locator_elements(selector)
            account = accounts[-1]
            return account.text

    def add_user_again(self):       
        # 添加下一个成员 
        self.driver.click('x /html/body/div/div/div/div[1]/div/div[2]/a[1]')



if __name__ == "__main__":
    AddUser().add_user()

