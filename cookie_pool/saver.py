import datetime
import random

from datebase import DB


class Savor():
    def __init__(self, type, website):
        self.db = DB()
        self.type = type
        self.website = website
        self.table_name = "{type}_{website}".format(type=self.type, website=self.website)

    def insert_into_user_table(self, phone_number, password):
        """
        向表中添加数据
        :param phone_number: 手机号
        :param password: 密码
        :return: 提示字符串
        """
        if self.type != "user":
            return "type有误，无法向user表中插入cookie"
        with self.db as cursor:
            try:
                sql_insert = "insert into {0}(phone_number,password) values(%s,%s);".format(
                    self.table_name)
                cursor.execute(sql_insert, (phone_number, password))
                cursor.execute("commit")
            except Exception:
                cursor.execute("rollback")
                return "插入失败"

    def insert_into_cookie_table(self, phone_number, cookie):
        print("cookie")
        if self.type != "cookie":
            return
        sql_query = "select into {0}(phone_number,cookie) values(%s,%s);".format(
            self.table_name)
        # date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(date_time)
        with self.db as cursor:
            try:
                sql_insert = "insert into {0}(phone_number,cookie) values(%s,%s);".format(
                    self.table_name)
                print(sql_insert)
                cursor.execute(sql_insert, (phone_number, cookie))
                cursor.execute("commit")
                print("成功")
            except Exception:
                print("插入失败")
                cursor.execute("rollback")

    def get_all(self, phone_number):
        if self.type == "user":
            sql_query = "select password from {} where phone_number=%s".format(self.table_name)
        elif self.type == "cookie":
            sql_query = "select cookie from {} where phone_number=%s".format(self.table_name)
        else:
            print("输入的type有误")
            return
        with self.db as cursor:
            try:
                cursor.execute(sql_query, (phone_number))
            except Exception:
                cursor.execute("rollback")

    def delete(self, phone_number):
        if self.type == "user":
            sql_delete = "delete from {} where phone_number=%s".format(self.table_name)
        elif self.type == "cookie":
            sql_delete = "delete from {} where phone_number=%s".format(self.table_name)
        else:
            print("输入的type有误")
            return
        with self.db as cursor:
            try:
                cursor.execute(sql_delete, (phone_number))
            except Exception:
                cursor.execute("rollback")

    def random(self):
        table_name = "cookie_" + self.website
        sql_getall = "select cookie from {}".format(table_name)
        cookie_tupple = tuple()
        with self.db as cursor:
            try:
                cursor.execute(sql_getall)
                cookie_tupple = cursor.fetchall()
                print(cookie_tupple)
            except Exception:
                print("查询数据库错误")
            if len(cookie_tupple) == 0:
                return
            cookie_list = [tupple_[0] for tupple_ in cookie_tupple]
            cookie = random.choice(cookie_list)
            return cookie

    def get_phone_numbers(self):
        if self.type == "user":
            sql_getall = "select phone_number from {}".format(self.table_name)
        elif self.type == "cookie":
            sql_getall = "select cookie from {}".format(self.table_name)
        else:
            print("输入的type有误")
            return
        with self.db as cursor:
            try:
                cursor.execute(sql_getall)
                return
            except Exception:
                print("查询数据库错误")

    def get_one_value(self, phone_number):
        sql_getall = "select phone_number from {}".format(self.table_name)
        with self.db as cursor:
            try:
                cursor.execute(sql_getall)
            except Exception:
                print("查询数据库错误")

    def count(self):
        sql_getall = "select count(*) from {}".format(self.table_name)
        with self.db as cursor:
            try:
                cursor.execute(sql_getall)
                return cursor.fetchone()[0]
            except Exception:
                print("查询数据库错误")


if __name__ == '__main__':
    sv = Savor("cookie", "jufa")
    # sv.insert_into_cookie_table("88888888","8888888888")
    # print(sv.random())
    print(sv.count())
