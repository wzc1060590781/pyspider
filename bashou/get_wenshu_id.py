import base64
from xml import etree

import requests

from operate_database import OperateMysql
from proxy.proxies import get_ab_ip


class wenshuID():
    def __init__(self,reason):
        self.url = "http://www.lawsdata.com/s/"
        self.operate_mysql = OperateMysql()
        self.reason = reason

    def form_data(self):
        i = self.operate_mysql.query_i_from_case_reason(self.reason)
        if i != None:
            data = {
                "q": {"caseType": ["2"], "reasonId": [i], "fuzzyMeasure": "0", "pageNo": 1,
                      "sortField": "referencedType", "sortOrder": "desc"},
                "subLibraryId": None
            }
        else:
            data = None
        return data

    # 生成refer的url
    def generate_refer_url(self):
        i = self.operate_mysql.query_i_from_case_reason(self.reason)
        if i != None:
            data = {"m": "advance",
                    "a": {"caseType": ["3"], "reasonId": [i], "fuzzyMeasure": "0", "reason": self.reason},
                    "sm": {"textSearch": ["single"], "litigantSearch": ["paragraph"]}}
            json_str = str(data)
            str_list = json_str.split(" ")
            json_str = "".join(str_list).encode("utf-8")
            return "http://www.lawsdata.com/?" + base64.b64encode(json_str).decode("utf-8") + "&s="
        return None

    # 生成所需的请求头
    def form_headers(self,cookie):
        refer_url =self.generate_refer_url(self.reason)
        if refer_url == None:
            print("获取案由id失败，数据库不存在该案由")
        headers = {
            "Host": "www.lawsdata.com",
            "Origin": "http://www.lawsdata.com",
            "Referer": refer_url,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": cookie
        }
        return headers

    def get_index_contnet(self,proxy,data,headers):
        resp = requests.post(self.url,data=data,headers=headers,proxies = proxy)
        count = resp.json()["numFound"]
        if count > 500:
            for province in resp["facetFields"]["provinceId"]:
                province_count = province[count]
                if province_count>500:
                    resp = requests.post("")
        else:
            return {"data":data,"url":self.url}


print("".join('// *[ @ id = "resultListDiv"] / div[2] / div / div[3] / div[3] / div / div[2] / span[2] / a'.split(" ")))
