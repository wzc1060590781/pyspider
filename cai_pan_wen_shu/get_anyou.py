import json
import re
import urllib
from urllib.parse import unquote

import requests
from selenium import webdriver

from operate_database import OperateMysql


class AnYou():
    def __init__(self):
        self.url = "https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord+案+1+案"
        self.login_url = "https://www.itslaw.com/api/v1/users/user/login/encryption"
        self.sess = requests.session()

    def get_anyou_total_list(self):
        with open("anyou.json","r",encoding="utf-8") as f:
            # json.load(f.read())
            anyou_total_list = json.load(f)
        return anyou_total_list

    def save_reason_to_mysql(self):
        anyou_total_list = self.get_anyou_total_list()
        print(len(anyou_total_list))
        for category_dict in anyou_total_list:
            operate_mysql_2 = OperateMysql()
            reason_id = category_dict["id"]
            parent_id = category_dict["parent"]
            name = category_dict["text"]
            print(reason_id,parent_id,name)
            operate_mysql_2.save_case_reason(reason_id, parent_id, name)


    def generate_reason_text(self):
        operate_mysql = OperateMysql()
        name_id_tup = operate_mysql.query_top_level_reason()
        for tup in name_id_tup:
            with open(tup[0]+".txt","w") as f:
                f.write("")
        return name_id_tup

    def write_mysql_to_text(self):
        operate_mysql = OperateMysql()
        name_id_tup = operate_mysql.query_top_level_reason()
        print(name_id_tup)
        for tup in name_id_tup:
            operate_mysql = OperateMysql()
            name = tup[0]
            id = tup[1]
            childern_name_id_tup = operate_mysql.search_childern(id)
            print(childern_name_id_tup)
            self.parse_childern_reason(name,childern_name_id_tup)

    def parse_childern_reason(self,name,childern_name_id_tup):
        for i in range(len(childern_name_id_tup)):
            operate_mysql = OperateMysql()
            childern_name_id_tup_2 = operate_mysql.search_childern(childern_name_id_tup[i][1])
            # print(childern_name_id_tup[i][0])
            if len(childern_name_id_tup_2)==0:
                with open(name + ".txt", "a", encoding="utf8") as f:
                    f.write (childern_name_id_tup[i][0] +":"+childern_name_id_tup[i][1]+"\n")
            else:
                self.parse_childern_reason(name,childern_name_id_tup_2)



    # def generate_anyou_text(self):
    #     with open("anyou.json","r") as f:
    #         dict = json.load(f)
    #         for category_dict in dict["data"]["searchResult"]["reasonResults"]:
    #             print(category_dict["id"][0:2])
    #             # self.parse(category_dict["id"][0:2],category_dict)
    #
    #             # with open(category_dict["id"][0:2]+".text","a") as f:
    #             #     anyou = self.parse(category_dict)
    #             #     f.write(anyou)

    def parse(self, name, dict):
        if "children" in dict:
            anyou_list = dict["children"]
            for dict_p in anyou_list:
                parse_dict = self.parse(name, dict_p)
                yield parse_dict
        else:
            with open(name + ".text", "a") as f:
                anyou = dict["text"]
                f.write(anyou)
                return


if __name__ == '__main__':
    anyou = AnYou()
    # anyou.save_reason_to_mysql()
    anyou.write_mysql_to_text()
    # anyou.get_anyou_total_list()
    # anyou.write_mysql_to_text()
    # anyou.index()
    # anyou.login()
    # url = unquote("https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B%E6%A1%88%2B1%2B%E6%A1%88")
    # print(url)
    # get_anyou()
    # dict = {"aaa":1}
    # print("aaa" in dict)
