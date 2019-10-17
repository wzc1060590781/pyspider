from mysql_db import DB


class OperateMysql():
    def __init__(self):
        self.db = DB()

    def save_case_reason(self, p, i, n):

        sql = "insert into case_reason (p,i,n) values('%s','%s','%s')"%(p,i,n)
        with self.db as cursor:
            cursor.execute(sql)
            cursor.execute("commit")

    def query_i_from_case_reason(self,anyou):
        sql = "select i from case_reason where n='%s'" % anyou
        with self.db as cursor:
            cursor.execute(sql)
            try:
                i = cursor.fetchone()[0]
                return i
            except Exception:
                return None


if __name__ == '__main__':
    operatemysql = OperateMysql()
    operatemysql.query_i_from_case_reason("食品药品安全行政管理(食品、药品)")