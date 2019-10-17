import json
import re
import time


import requests
class YiMa():
    def __init__(self,username,password,project_num):
        self.url ="http://api.fxhyd.cn/UserInterface.aspx?action=login&username={0}&password={1}"
        self.get_phone_number_url = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token={0}&itemid={1}&timestamp=TIMESTAMP&isp={2}"
        self.get_smscode_url = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token={0}&itemid={1}&mobile={2}&timestamp=TIMESTAMP"
        self.username = username
        self.password = password
        self.project_num = project_num
        self.token = None
        self.phone_number = None

    def get_response(self):
        resp = requests.get(self.url.format(self.username,self.password))
        return resp.content.decode()

    def get_token(self):
        resp = self.get_response()
        if resp.startswith("success"):
            self.token = resp.split("|")[1]

    def get_phone_number(self):
        if self.token == None:
            self.get_token()
        get_phone_number_url = self.get_phone_number_url.format(self.token,self.project_num,"1")
        resp = requests.get(get_phone_number_url).content.decode()
        if resp.startswith("success"):
            self.phone_number = resp.split("|")[1]
        else:
            print("报错")
        return self.phone_number

    def get_smscode(self):
        if self.phone_number==None:
            phone_number = self.get_phone_number()
        get_smscode_url = self.get_smscode_url.format(self.token,self.project_num,self.phone_number)
        begin_time = time.time()
        while True:
            time.sleep(5)
            resp = requests.get(get_smscode_url)
            sms_code_str = resp.content.decode()
            print(sms_code_str)
            # try:
            #     sms_code = int(sms_code_str)
            # except Exception:
            #     continue
            if sms_code_str.startswith("success"):
                break
            end_time = time.time()
            if end_time-begin_time>60:
                return "failed"
        sms_code = re.match(r".*?(\d+).*", sms_code_str).group(1)
        print(sms_code)
        return sms_code



if __name__ == '__main__':
    yima = YiMa("huanghong695","wenshu123","7485")
    yima.get_phone_number()
    # yima.get_smscode()
    print(yima.phone_number)