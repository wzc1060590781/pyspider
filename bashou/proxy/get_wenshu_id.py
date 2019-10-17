import base64
import json
import threading

from mysql_db import DB
from operate_database import OperateMysql


class GetHtmlThreading(threading.Thread):
    def __init__(self, thread_name, mysql_table):
        super(GetHtmlThreading, self).__init__()

    def Login(self):
        pass

class Page_Url():
    def __init__(self, anyou):
        self.db = DB()
        self.anyou = anyou
        self.operate = OperateMysql()

    def run(self):
        pass

    def generate_url(self):
        i = self.operate.query_i_from_case_reason(self.anyou)
        if i !=None:
            data = {"m":"advance","a":{"caseType":["3"],"reasonId":[i],"fuzzyMeasure":"0","reason":self.anyou},"sm":{"textSearch":["single"],"litigantSearch":["paragraph"]}}
            # print(data)
            # json_str = json.dumps(data,ensure_ascii=False).encode("utf-8")
            json_str = str(data)
            str_list = json_str.split(" ")
            json_str = "".join(str_list).encode("utf-8")
            return "http://www.lawsdata.com/?"+base64.b64encode(json_str).decode("utf-8")+"&s="

    def get_first_page(self):
        cookie = get_cookie()
        headers = {
            "cookie":cookie,
            "Host": "www.lawsdata.com",
            "Referer": "http://www.lawsdata.com/?q = eydtJzonYWR2YW5jZScsJ2EnOnsnY2FzZVR5cGUnOlsnMyddLCdyZWFzb25JZCc6WycwMDMwMDEwMjMnXSwnZnV6enlNZWFzdXJlJzonMCcsJ3JlYXNvbic6J+mjn+WTgeiNr+WTgeWuieWFqOihjOaUv+euoeeQhijpo5/lk4HjgIHoja/lk4EpJ30sJ3NtJzp7J3RleHRTZWFyY2gnOlsnc2luZ2xlJ10sJ2xpdGlnYW50U2VhcmNoJzpbJ3BhcmFncmFwaCddfX0=&s=",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

if __name__ == '__main__':
    gt = Page_Url("食品药品安全行政管理(食品、药品)")
    gt.generate_url()
    # json_str = "111111111".encode()
    # print(base64.b64encode(json_str))