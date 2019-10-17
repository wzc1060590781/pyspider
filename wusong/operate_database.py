from mysql_db import DB


class OperateMysql():
    def __init__(self):
        self.db = DB()

    def save_case_reason(self, reason_id, parent_id, name):
        sql = "insert into case_reason (reason_id,parent_id,name) values('%s','%s','%s')"%(reason_id,parent_id,name)
        with self.db as cursor:
            try:
                cursor.execute(sql)
                cursor.execute("commit")
            except Exception:
                cursor.execute("rollback")

    def search_reason_id_by_name(self,name):
        sql = "select reason_id from case_reason where name='%s'" % name
        with self.db as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]

    def query_i_from_case_reason(self,anyou):
        sql = "select i from case_reason where n='%s'" % anyou
        with self.db as cursor:
            cursor.execute(sql)
            try:
                i = cursor.fetchone()[0]
                return i
            except Exception:
                return None

    def query_top_level_reason(self):
        sql_1 = "select distinct(name),reason_id from case_reason where parent_id='TopLevel'"
        with self.db as cursor:
            cursor.execute(sql_1)
            name_id_tup = cursor.fetchall()
            return name_id_tup

    def search_childern(self,parent_id):
        print(type(parent_id))
        print("parent_id : "+parent_id)
        sql_1 = "select distinct(name),reason_id from case_reason where parent_id='%s'"% parent_id
        with self.db as cursor:
            cursor.execute(sql_1)
            name_id_tup = cursor.fetchall()
            return name_id_tup


if __name__ == '__main__':
    operatemysql = OperateMysql()
    name_id_tup = operatemysql.search_childern("88888")
    print(name_id_tup)