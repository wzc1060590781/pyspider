import requests

from proxy.proxies import get_ab_ip


class Login():
    def __init__(self):
        self.url = "http://www.lawsdata.com/login"
        self.proxy = get_ab_ip()

    def login(self,mobile,password):
        data = {
            "mobile": mobile,
            "password": password,
            "rememberMe": "false"
        }
        headers = {
            "Host": "www.lawsdata.com",
            "Referer": "http://www.lawsdata.com",
            "Origin": "http://www.lawsdata.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        resp = requests.post(self.url,data=data,headers=headers)
        resp_dict = resp.json()
        if resp_dict["returnState"]== "OK":
            cookies = requests.utils.dict_from_cookiejar(resp.cookies)
            cookie_str = mobile + ":"
            for k, v in cookies.items():
                cookie_str += str(k) + "=" + str(v) + "; "
            return cookie_str

    def get_cookie(self,mobile,resp):
        cookies = requests.utils.dict_from_cookiejar(resp.cookies)
        cookie_str = mobile + ":"
        for k, v in cookies.items():
            cookie_str += str(k) + "=" + str(v) + "; "
        return cookie_str




if __name__ == '__main__':
    lg = Login()
    # lg.login("13269774451","44509542")
    lg.download()
    # lg.open_text()