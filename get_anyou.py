import json
import urllib
from urllib.parse import unquote

import requests
from selenium import webdriver


class AnYou():
    def __init__(self):
        self.url = "https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord+案+1+案"
        self.login_url = "https://www.itslaw.com/api/v1/users/user/login/encryption"
        self.sess = requests.session()

    def index(self):
        url = "https://www.itslaw.com/bj"
        headers = {
            "Host": "www.lawsdata.com",
            "Connection": "keep-alive",
            "Referer": "http://www.itslaw.com/obj",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        self.sess.headers.update(headers)
        resp = self.sess.get(url)
        print(resp.content)

    def get_sess_cookie(self):
        # 得到
        url = "https://www.itslaw.com/api/v1/subSites/subSite/info?subSiteCode=bj"
        headers = {
            "Host": "www.itslaw.com",
            "Referer": "https://www.itslaw.com/bj",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "If-Modified-Since":"Mon, 26 Jul 1997 05:00:00 GMT",
            "Pragma": "no-cache"
        }
        self.sess.headers.update(headers)
        resp = self.sess.get(url)

    # def login(self):
    #     data = {
    #         "isAutoLogin": "true",
    #         "password": "MjQyMjQyNDU1NA==",
    #         "userName": "13836841546"
    #     }
    #     headers = {
    #         "Host": "www.lawsdata.com",
    #         "Referer": "http://www.itslaw.com",
    #         "Origin": "http://www.itslaw.com/obj",
    #         "Upgrade-Insecure-Requests": "1",
    #         "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    #     }
    #     resp = self.sess.post(self.login_url, data=data, headers=headers)
    #     if self.check_login() == 0:
    #         cookies = requests.utils.dict_from_cookiejar(resp.cookies)
    #         cookie_str = "13836841546" + ":"
    #         for k, v in cookies.items():
    #             cookie_str += str(k) + "=" + str(v) + "; "
    #         return cookie_str

    # def check_login(self):
    #     url = "https://www.itslaw.com/api/v1/users/user/loginInfo"
    #     headers = {
    #         "Referer":"https://www.itslaw.com/bj",
    #         "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    #     }
    #     self.sess.headers.update(headers)
    #     resp = self.sess.get(url)
    #     dict = resp.json()
    #     print(dict)
    #     if dict["result"]["code"] ==0:
    #         print("登录成功")
    #         return 0
    #     else:
    #         print("未登录成")

    def get_total_anyou(self):
        # self.index()
        self.get_sess_cookie()
        url = "https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B%E6%A1%88%2B1%2B%E6%A1%88"
        headers = {
            "Host": "www.itslaw.com",
            "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT",
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E6%A1%88%2B1%2B%E6%A1%88",
            # "Cookie":"Hm_lvt_bc6f194cb44b24b9f44f1c8766c28008=1566985864; Hm_lpvt_bc6f194cb44b24b9f44f1c8766c28008=1566985864; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1566985864; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1566985864; _t=dcd84d7b-95a3-4e47-913e-1e1b866b9f4a; sessionId=f0251de9-e11e-4915-add9-c9f0bd6b7d47; subSiteCode=bj; showSubSiteTip=false"
            # "Cookie": "LXB_REFER=www.baidu.com; _t=09610437-9e5d-4b73-9a8d-e10a6f8807d0; sessionId=38f0cf6c-7051-4d98-a690-c0758b34a3e8; subSiteCode=bj; showSubSiteTip=false; _u=7edd9f89-cff0-437d-878f-553b4d853b16; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1566972954,1566975947; Hm_lvt_bc6f194cb44b24b9f44f1c8766c28008=1566972954,1566975947; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1566979161; Hm_lpvt_bc6f194cb44b24b9f44f1c8766c28008=1566979161"
        }
        self.sess.headers.update(headers)
        resp = self.sess.get(url)
        dict = resp.json()
        with open("anyou.json","w") as f:
            json.dump(dict,f,ensure_ascii=False,indent=2)

    def generate_anyou_text(self):
        with open("anyou.json","r") as f:
            dict = json.load(f)
            for category_dict in dict["data"]["searchResult"]["reasonResults"]:
                self.parse(category_dict["id"][0:2],category_dict)
                # with open(category_dict["id"][0:2]+".text","a") as f:
                #     anyou = self.parse(category_dict)
                #     f.write(anyou)

    def parse(self,name,dict):
        if "children" in dict:
            anyou_list = dict["children"]
            for dict_p in anyou_list:
                parse_dict = self.parse(name,dict_p)
                yield parse_dict
        else:
            with open(name+".text", "a") as f:
                anyou = dict["text"]
                f.write(anyou)
                return

if __name__ == '__main__':
    anyou = AnYou()
    anyou.generate_anyou_text()
    # anyou.index()
    # anyou.login()
    # url = unquote("https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B%E6%A1%88%2B1%2B%E6%A1%88")
    # print(url)
    # get_anyou()
    # dict = {"aaa":1}
    # print("aaa" in dict)