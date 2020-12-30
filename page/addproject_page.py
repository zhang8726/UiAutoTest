import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage

class AddProject(BasePage):

    def switch_to(self):
        # 添加项目
        driver.click('x //*[@id="s-menu-3"]/button')

        # 切换到frame中
        driver.switch_to_frame('id iframe-3')

    def add_project_start(self):
        # 添加区块
        driver.click('x //*[@id="dashboard"]/div[2]/a')
        driver.select_by_index('x //*[@id="blocks"]',1)

    def add_project(self,name):
        # 区块名称
        driver.input('id title',name)
        # 外观
        # 宽度
        driver.select_by_index('id grid',random.randint(0,5))
        # 颜色
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]'%random.randint(1,6))
        # 类型
        driver.click('x //*[@id="paramstype_chosen"]/a')
        driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%random.randint(1,5))
        # 数量
        driver.locator_element('id params[num]').clear()
        driver.input('id params[num]',random.randint(10,20))
        # 排序
        driver.click('x //*[@id="paramsorderBy_chosen"]/a')
        driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%random.randint(1,6))
        # 任务状态 
        driver.click('x //*[@id="paramsstatus_chosen"]/ul')
        driver.click('x //*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%random.randint(1,6))
        # 保存
        driver.click('id submit')
        driver.wait(3)

    def get_dataname(self,selector):
        # 断言 
        data_names = driver.locator_elements(selector)
        data_name = data_names[-1].get_attribute('data-name')
        return data_name

            
            
if __name__ == "__main__":
    AddProject().add_project()