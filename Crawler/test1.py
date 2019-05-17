
from selenium import webdriver
import time

class Test(object):
    def __init__(self):
        self.brower = webdriver.Firefox()
        self.url = 'https://kyfw.12306.cn/otn/regist/init'
        self.data  = {"userName": ["++++++","teamboy2019","teamboy2020","teamboy2021","teamboy2022","teamboy20222","teamboy20223","teamboy23022"],
                      "passWord" : ["Teamboy2019_", "11111", "passWord2", "passWord2", "passWord2", "passWord2", "passWord2", "passWord2"],
                       "confirmPassWord" : ["Teamboy2019_", "11111", "passWord21", "passWord2", "passWord2", "passWord2", "passWord2", "passWord2"],
                      "r-txt" : ["姚柯寒","姚柯寒","姚柯寒","","姚柯寒","姚柯寒","姚柯寒","姚柯寒"],
                      "cardCode" :["330124199601191812","330124199601191812","330124199601191812","330124199601191812","330124192","330124199601191812","330124199601191812","330124199601191812"],
                      "email" : ["Teamboy@gmail.com","Teamboy@gmail.com","Teamboy@gmail.com","Teamboy@gmail.com","Teamboy@gmail.com","Teambo","Teamboy@gmail.com","Teamboy@gmail.com"],
                      "mobileNo":["17826800685","17826800685","17826800685","17826800685","17826800685","17826800685","178268","17826800685"]



             }

    def test(self):

        # self.brower.get(self.url)
        for item in range(8):
            self.brower.get(self.url)
            self.brower.find_element_by_id('userName').clear()
            self.brower.find_element_by_id('userName').send_keys(self.data['userName'][item])
            self.brower.find_element_by_id("passWord").clear()
            self.brower.find_element_by_id('passWord').send_keys(self.data['passWord'][item])
            self.brower.find_element_by_id('confirmPassWord').clear()
            self.brower.find_element_by_id('confirmPassWord').send_keys(self.data['confirmPassWord'][item])
            self.brower.find_element_by_xpath(".//*[@name='loginUserDTO.name']").clear()
            # self.brower.find_elements_by_class_name('r-txt')[0].send_keys("姚柯寒")
            self.brower.find_element_by_xpath(".//*[@name='loginUserDTO.name']").send_keys(self.data['r-txt'][item])
            self.brower.find_element_by_id('cardCode').clear()
            self.brower.find_element_by_id('cardCode').send_keys(self.data['cardCode'][item])
            self.brower.find_element_by_id('email').clear()
            self.brower.find_element_by_id('email').send_keys(self.data['email'][item])
            self.brower.find_element_by_id('mobileNo').clear()
            self.brower.find_element_by_id('mobileNo').send_keys(self.data['mobileNo'][item])
            self.brower.find_element_by_id('checkAgree').click()
            self.brower.find_element_by_id('nextBtn').click()
            time.sleep(3)


if __name__ == '__main__':
    test =  Test()
    test.test()