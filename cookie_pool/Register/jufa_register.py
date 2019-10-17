import random
import time

from selenium import webdriver

from Register.website_register_father import RegisterDatas


class jufa_Register(RegisterDatas):
    def __init__(self, website):
        super().__init__(website)
        self.url = "https://www.jufaanli.com/"

    @classmethod
    def jufa_generate_password(self):
        password = str(random.randint(1000000, 9999999999))
        return password

    def jufa_init_browser(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        return browser

    def jufa_get_code_image(self, browser):
        """
        获取验证码图片
        :param phone_number: 用于存放验证码图片命名用手机号
        :return: None
        """
        browser.find_element_by_xpath('//*[@id="imgFrame"]').screenshot('jufa.jpg')

    def jufa_get_register_cookie(self):
        password = self.jufa_generate_password()
        phone_number = self.get_phone_number()
        browser = self.jufa_init_browser()
        browser.find_element_by_xpath('//*[@id="regObj"]/span').click()
        # 输入手机号
        browser.find_element_by_xpath('//*[@id="regPhoneOrEmailObj"]').send_keys(phone_number)
        # 输入密码
        browser.find_element_by_xpath('//*[@id="regPwdObj"]').send_keys(password)
        # 获取聚法的验证码图片
        self.jufa_get_code_image(browser)
        code = self.recognize_code()
        print(code)
        while True:
            # 输入图片验证码
            browser.find_element_by_xpath('//*[@id="inputCode"]').send_keys(code)
            # 点击获取短信验证码按钮
            browser.find_element_by_xpath('//*[@id="getVerifyObj"]').click()
            time.sleep(2)
            # 获取短信验证码
            if browser.find_element_by_xpath('//*[@id="getVerifyObj"]').text == "获取验证码":
                self.jufa_get_code_image(browser)
                code = self.recognize_code()
            else:
                break
        result_code = self.yima.get_smscode()
        # 输入短信验证码
        browser.find_element_by_xpath('//*[@id="verifyPhoneObj"]').send_keys(result_code)
        time.sleep(1.5)
        # 点击登录
        browser.find_element_by_xpath('//*[@id="subRegister"]').click()
        time.sleep(0.3)
        cookie_str = self.parse_cookie(browser)
        dict = {}
        dict["phone_number"] = phone_number
        dict["password"] = password
        dict["cookie"] = cookie_str
        return dict
