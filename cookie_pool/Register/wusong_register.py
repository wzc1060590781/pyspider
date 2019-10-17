import random
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Register.website_register_father import RegisterDatas
from selenium.webdriver.support import expected_conditions as EC


class wusong_Register(RegisterDatas):
    def __init__(self, website):
        super().__init__(website)
        self.url = "https://www.itslaw.com/bj"

    @classmethod
    def wusong_generate_password(self):
        password = str(random.randint(100000, 9999999999))
        return password

    def jufa_init_browser(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        return browser


    def wusong_get_register_cookie(self):
        password = self.wusong_generate_password()
        phone_number = self.get_phone_number()
        print(password)
        print(phone_number)
        browser = self.jufa_init_browser()
        # WebDriverWait(browser, 20, 0.5).until(EC.element_to_be_clickable((By.ID, 'username')))
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="wel-bg-style"]/div[1]/div/img[2]').click()
        browser.find_element_by_xpath('//*[@id="wel-bg-style"]/div[1]/header/div[4]/div/section/span[2]').click()
        WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'username')))
        # 输入手机号

        browser.find_element_by_xpath('//*[@id="username"]').send_keys(phone_number)
        # 输入密码
        time.sleep(2)
        WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'password')))

        browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        time.sleep(10)
        # 点击获取短信验证码按钮
        # WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, '')))
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="TencentCaptcha"]').click()
        # # time.sleep(2)
        result_code = self.yima.get_smscode()
        print(result_code)
        time.sleep(10)

        cookie_str = self.parse_cookie(browser)
        with open("phone_cookie.txt","a") as f:
            f.write(phone_number+":"+cookie_str+"\n")
        with open("phone_password.txt", "a") as f:
            f.write(phone_number + ":" + password + "\n")
        # # # 输入短信验证码
        # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="verifyPhoneObj"]').send_keys(result_code)
        # time.sleep(1.5)
        # # # # 点击登录
        # # time.sleep(2)
        # browser.find_element_by_xpath('//*[@id="ls-global"]/div[4]/div/div/div/div/div/div[1]/form/div[2]/button').click()
        # # # time.sleep(0.3)
        # cookie_str = self.parse_cookie(browser)
        # dict = {}
        # dict["phone_number"] = phone_number
        # dict["password"] = password
        # dict["cookie"] = cookie_str
        # return dict
if __name__ == '__main__':
    # for i in range(5):
    wusong = wusong_Register("wusong")
        # wusong.wusong_get_register_cookie()
    print(wusong.wusong_generate_password())