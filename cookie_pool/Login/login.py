import requests

from Login.form_login_datas import LoginDatas
from saver import Savor
from utils.proxy.generate_proxy import get_ab_ip


class Login():
    def __init__(self, website):
        self.jufa_url = "https://www.jufaanli.com/home/User/login"
        self.login_datas = LoginDatas()
        self.website = website

    def post_login(self, data, headers):
        """
        发送请求方法
        :param data: post请求所需数据
        :param headers: 请求头
        :return: response对象
        """
        proxy = get_ab_ip()
        resp = requests.post(url=self.jufa_url, data=data, headers=headers, proxies=proxy)
        return resp

    def get_cookie_str(self, phone_number, resp):
        """
        获取cookie方法
        :param phone_number: 手机号
        :param resp: response对象
        :return: cookie字符串
        """
        cookies = requests.utils.dict_from_cookiejar(resp.cookies)
        cookie_str = ""
        for k, v in cookies.items():
            cookie_str += str(k) + "=" + str(v) + "; "
        # print(cookie_str)
        return cookie_str

    def generate_login_cookie(self, phone_number, password):
        func = getattr(self.login_datas,self.website+"_login_data")
        data = func(phone_number,password)
        # data = eval("self.login_datas." + self.website + "_login_data({phone_number}, {password})".format(
        #     phone_number=phone_number, password=password))
        headers = self.login_datas.jufa_get_login_headers()
        resp = self.post_login(data, headers)
        cookie_str = self.get_cookie_str(phone_number, resp)
        self.save_cookie_password(phone_number, cookie_str)
        print(cookie_str)
        # return cookie_str

    def save_cookie_password(self, phone_number, cookie, ):
        type = "cookie"
        sv = Savor(type, self.website)
        sv.insert_into_cookie_table(phone_number, cookie)


if __name__ == '__main__':
    login = Login("wusong")
    # login.generate_login_cookie("15214586246", "2770980686")
    func = getattr(login.login_datas, login.website + "_login_data")
    data = func("15214586246", "2770980686")