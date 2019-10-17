# 防止中文报错
import time
import urllib
from http import cookiejar
from PIL import Image

import pytesseract


# image = Image.open("")
# .image_to_text(image)
# CaptchaUrl = "http://202.115.80.153/CheckCode.aspx"
# PostUrl = "http://202.115.80.153/default2.aspx"
class Register():
    def __init__(self):
        self.zhiwang_image_url = "http://my.cnki.net/elibregister/CheckCode.aspx?"
        self.zhiwang_getsmscode_url = "http://my.cnki.net/elibregister/Server.aspx?"
        self.check_image_code_url = "http://my.cnki.net/elibregister/Server.aspx?"
        # self.register_url = "https://www.jufaanli.com/home/User/regist"
        # self.get_sms_code_url = "https://www.jufaanli.com/home/User/sendMgsVerifyCode"
        # self.get_image_code_url ="https://www.jufaanli.com/home/Server/identitycode"

    # 验证码地址和post地址
    def get_image(self):
        cookie = cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        self.opener = urllib.request.build_opener(handler)
        # 将cookies绑定到一个opener cookie由cookielib自动管理
        username = '12345678910'
        # password = 'password123'
        # 用户名和密码
        picture = self.opener.open(self.zhiwang_image_url).read()
        # # 用openr访问验证码地址,获取cookie
        local = open('image.png', 'wb')
        local.write(picture)
        local.close()

    def get_code(self):
        self.get_image()
        img = Image.open("image.png")
        # img.show()
        img = img.convert("L")
        img.show()
        threshold = 150
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            #
            else:
                # print(1)
                table.append(1)
        #
        img = img.point(table, "1")
        img.show()
        # print(2)
        str = pytesseract.image_to_string(img)
        # str_list = str.split(" ")
        # str = "".join(str_list)
        return str

    def get_smscode(self):
        while True:
            image_code = self.get_code()
            print(image_code)
            headers = {
                "Host": "my.cnki.net",
                "Origin": "http: // my.cnki.net",
                "Referer": "http://my.cnki.net/elibregister/commonRegister.aspx",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
            }
            mobile = "13522224444"

            url = self.get_sms_url(mobile, image_code)
            # print(url)
            print(url)
            request = urllib.request.Request(url,data=None,headers=headers)
            resp = self.opener.open(request)
            # print(resp.getcode())
            resp_str = resp.read().decode()
            print(resp_str)
            if resp_str == "1":
                print("发送验证码成功")
                break
            time.sleep(1)
    # def check_image_code(self):
    #     while True:
    #         code = self.get_code()
    #         print(code)
    #         url = self.get_check_image_code_url(code)
    #         headers = {
    #             "Host": "my.cnki.net",
    #             "Referer": "http://my.cnki.net/elibregister/commonRegister.aspx",
    #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    #             "X-Requested-With": "XMLHttpRequest"
    #         }
    #         request = urllib.request.Request(url, data=None, headers=headers)
    #         resp = self.opener.open(request)
    #         print(resp.read())
    #         if resp.read().decode() !=-3:
    #             print("验证通过")
    #             break
    #         time.sleep(2)


    # def get_check_image_code_url(self,code):
    #     data = {
    #         "imageCode": code,
    #         "checkFlag": "1",
    #         "operatetype": "7"
    #     }
    #     check_image_code_url = self.check_image_code_url + urllib.parse.urlencode(data)
    #     return check_image_code_url

    def get_sms_url(self, mobile, image_code):
        # temp = int(time.time())
        post_data = {
            "checkflag": "1",
            # "temp": temp,
            "operatetype": "7",
            "imageCode": image_code,
        }
        zhiwang_getsmscode_url = self.zhiwang_getsmscode_url + urllib.parse.urlencode(post_data)
        return zhiwang_getsmscode_url

    def register(self):
        pass


if __name__ == '__main__':
    re = Register()
    # re.check_image_code()
    re.get_smscode()
    # re.get_image()
    # code = re.get_code()
    # print(code)
    # post_data = {
    #     "mobile": "13522222222",
    #     "temp": "1566720445267",
    #     "operatetype": "2",
    #     "imageCode": 1111,
    # }
    # data = urllib.parse.urlencode(post_data)
    # print(data)
