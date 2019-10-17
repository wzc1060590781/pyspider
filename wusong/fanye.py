import json
import time
from urllib.parse import unquote

import requests
from selenium import webdriver


class FanYe():
    def __init__(self,anyou):
        self.content_url ="https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord+"+anyou+"+1+"+anyou
        self.login_url = "https://www.itslaw.com/api/v1/users/user/login/encryption"
        self.sess = requests.session()



    def index(self):
        """
        访问首页，添加cookie
        :return:
        """
        url = "https://www.itslaw.com/bj"
        headers = {
            "Host": "www.lawsdata.com",
            "Connection": "keep-alive",
            "Referer": "http://www.itslaw.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        self.sess.headers.update(headers)
        resp = self.sess.get(url)

    def login(self):

        data = {
                "isAutoLogin": "true",
                "password": "MjQyMjQyNDU1NA==",
                "userName": "13836841546"
            }
        data = json.dumps(data)
        headers = {
            "Host": "www.lawsdata.com",
            "Referer": "http://www.itslaw.com",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "http://www.itslaw.com/obj",
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

        ck_dict = requests.utils.dict_from_cookiejar(self.sess.cookies)
        ck_dict["subSiteCode"] = "obj"
        ck_dict["showSubSiteTip"] = "false"
        self.sess.headers.update(headers)
        resp = self.sess.post(self.login_url, data=data, cookies=ck_dict)
        print(ck_dict)
        print(resp.status_code)

    def get_sess_cookie(self):
        # 得到
        url = "https://www.itslaw.com/api/v1/subSites/subSite/info?subSiteCode=bj"
        headers = {
            "Host": "www.itslaw.com",
            "Referer": "https://www.itslaw.com/bj",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT",
            "Pragma": "no-cache"
        }
        self.sess.headers.update(headers)
        resp = self.sess.get(url)

    def fan(self):
        pass


if __name__ == '__main__':
    fanye = FanYe("生产、销售伪劣产品罪")
    fanye.index()
    fanye.get_sess_cookie()
    fanye.login()
    # print(unquote(
        # "https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E7%94%9F%E4%BA%A7%E3%80%81%E9%94%80%E5%94%AE%E4%BC%AA%E5%8A%A3%E4%BA%A7%E5%93%81%E7%BD%AA%2B1%2B%E7%94%9F%E4%BA%A7%E3%80%81%E9%94%80%E5%94%AE%E4%BC%AA%E5%8A%A3%E4%BA%A7%E5%93%81%E7%BD%AA"))
