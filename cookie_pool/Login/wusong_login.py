import requests
import base64
from Login.generate_proxy import get_ab_ip


class WuSongLogin():
    def __init__(self):
        self.website = "wusong"
        self.url = "https://www.itslaw.com/api/v1/users/user/login/encryption"

    def post_login(self, data, headers):
        """
        发送请求方法
        :param data: post请求所需数据
        :param headers: 请求头
        :return: response对象
        """
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        proxy = get_ab_ip()
        print(proxy)
        resp = s.post(url=self.url, data=data,proxies=proxy,headers=headers)
        print(resp.json()["result"]["message"])
        return resp

    def generate_login_cookie(self, phone_number, password):
        data = self.wusong_login_data(phone_number, password)
        headers = self.wusong_get_login_headers()
        print(data)
        resp = self.post_login(data, headers)
        cookie_str = self.get_cookie_str(resp)
        return cookie_str

    def get_cookie_str(self, resp):
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
        return cookie_str

    def wusong_login_data(self, phone_number, password):
        password = base64.b64encode(password.encode())
        print(password)
        data = {
            "userName": phone_number,
            "password": password,
            "isAutoLogin": False
        }
        # print(data)
        return data

    def wusong_get_login_headers(self):
        """
        生成聚法请求头
        :return: 请求头字典
        """
        headers = {
            "Host":"www.itslaw.com",
            "Origin": "https://www.itslaw.com",
            "Referer": "https://www.itslaw.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Connection":"keep-alive"
        }
        return headers


if __name__ == '__main__':
    wusong = WuSongLogin()
    wusong.generate_login_cookie("13846629441", "8064399084")
