import json

import MySQLdb
import requests
import selenium
from selenium import webdriver

from config import config
from operate_database import OperateMysql
from proxy.proxies import get_ab_ip


class CaseReason():
    def __init__(self):
        self.url = "http://www.lawsdata.com/js/data/reason.json"
        self.headers = {
            "Host": "www.lawsdata.com",
            "Origin": "http: // www.lawsdata.com",
            "Referer":"http://www.lawsdata.com/?q=eyJtIjoiYWR2YW5jZSIsImEiOnsidGV4dHMiOlt7InR5cGUiOiJhbGwiLCJzdWJUeXBlIjoiIiwidmFsdWUiOiLmoYgifV0sImNhc2VUeXBlIjpbIjIiXSwiZnV6enlNZWFzdXJlIjowfSwic20iOnsidGV4dFNlYXJjaCI6WyJzaW5nbGUiXSwibGl0aWdhbnRTZWFyY2giOlsicGFyYWdyYXBoIl19fQ==&s=",
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome /70.0.3538.110 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.outer_reason = config["outer_reason"]
        self.operate_mysql = OperateMysql()
        # self.conn = MySQLdb.connect(host="127.0.0.1", database="bashou", user="root", password="mysql", charset='utf8')
        # self.cs1 = self.conn.cursor()

    def save_case_reason(self, p_, i_, n_):
        sql = "insert into case_reason_2 (p,i,n) values ('{0}','{1}','{2}')".format(p_,i_,n_)
        try:
            with self.operate_mysql as cursor:
                cursor.execute(sql)
                cursor.execute("commit")
        except Exception:
            print("重复数据:(%s,%s,%s)"%(p_,i_,n_))
            cursor.execute("rollback")

    def get_case_reason(self):
        resp = requests.get(self.url,headers=self.headers)
        # print(len(tuple(resp.json())))
        for dict in resp.json():
            p_ = dict["p"]
            i_ = dict["i"]
            n_ = dict["n"]
            self.save_case_reason(p_,i_,n_)
        print("插入完毕")

    def write_mysql_into_text(self):
        sql = "select distinct(i) from case_reason as cr where cr.i not in (select distinct(case_reason.p) from case_reason)"
        with self.operate_mysql as cursor:
            cursor.execute(sql)
            name_list = cursor.fetchall()
        print(len(tuple(name_list)))
        # for name_tupple in name_list:
        #     with open("案由.text","a",encoding="utf8") as f:
        #         f.write(name_tupple[0]+"\n")

    def write_mysql_into_anyou(self):
        sql_1 = "select distinct(n),i from case_reason where p='-1'"
        self.cs1.execute(sql_1)
        name_list = self.cs1.fetchall()
        for anyou_tupple in name_list:
            name = anyou_tupple[0]
            anyou_i = anyou_tupple[1]
        # name = "赔偿案由"
        # anyou_i = "004"
            sql_2 = "select distinct(i) from case_reason where p='%s'" % anyou_i
            with self.operate_mysql as cursor:
                cursor.execute(sql_2)
                all_i = cursor.fetchall()
            list_t = []
            for i in all_i:
                list_t.append(i[0])
            self.iiii(list_t,name)


    def iiii(self,list_t,name):
        print("这是list的长度："+str(len(list_t)))
        for i in range(len(list_t)):
            print("这是i:"+str(i))
            # sql_3 = "select count(*) from case_reason where p='%s'" % list_t[i]
            self.cs1.execute("select count(*) from case_reason where p='%s'" % list_t[i])
            count = self.cs1.fetchone()[0]
            if count == 0:
                with open(name + ".text", "a",encoding="utf8") as f:
                    sql_4 = "select n from case_reason where i='%s'" % list_t[i]
                    self.cs1.execute(sql_4)
                    n = self.cs1.fetchone()[0]
                    f.write(n + "\n")
            else:
                self.cs1.execute("select i from case_reason where p='%s'" % list_t[i])
                all_i = self.cs1.fetchall()
                list_t2 = []
                for i in all_i:
                    list_t2.append(i[0])
                self.iiii(list_t2,name)


if __name__ == '__main__':
    cr = CaseReason()
    # cr.get_case_reason()
    # cr.write_mysql_into_anyou()
    cr.write_mysql_into_text()
    # i = 1
    # print(str(i))