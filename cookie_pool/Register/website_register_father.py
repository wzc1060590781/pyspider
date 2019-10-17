import random
import time

from selenium import webdriver
from utils.utils_config import config, yima_project_itemid_config
from utils.yima import YiMa
from utils.yundama.Test import Code


class RegisterDatas():
    def __init__(self, website):
        self.yima = YiMa(config["Yima_username"], config["Yima_password"], yima_project_itemid_config[website])
        self.website = website
        # self.jufa_url = "https://www.jufaanli.com/"

    def get_phone_number(self):
        phone_number = self.yima.get_phone_number()
        return phone_number

    def get_sms_code(self):
        return self.yima.get_smscode()

    def recognize_code(self):
        """
        识别验证码图片
        :return: 图片验证码
        """
        code = Code()
        # print(self.website)
        img_code = code.identify_key(self.website)
        print(img_code)
        return code.identify_key(self.website)

    def parse_cookie(self, browser):
        """
        获取cookie
        :return:cookie字符串
        """
        cookie_list = browser.get_cookies()
        browser.close()
        cookie = {}
        for i in cookie_list:
            cookie[i["name"]] = i["value"]
        cookie_str = ""
        for k, v in cookie.items():
            cookie_str += str(k) + "=" + str(v) + "; "
        return cookie_str

