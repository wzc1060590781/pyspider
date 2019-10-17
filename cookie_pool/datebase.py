# import MySQLdb
#
# MySql_HOST = '192.168.14.23'
# # MySql_PORT = 6379
# MySql_UERSNAME = "root"
# MySql_PASSWORD = "root123"
# DB_NAME = "cookie_pool"
# class DB(object):
#     def __init__(self):
#         # 1. 连接数据
#         # 创建Connection连接
#         self.conn = MySQLdb.connect(host=MySql_HOST, database=DB_NAME, user=MySql_UERSNAME,password=MySql_PASSWORD, charset='utf8')
#         self.cs1 = self.conn.cursor()
#
#     def __enter__(self):
#         return self.cs1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cs1.close()
#         self.conn.close()

if __name__ == '__main__':
    # print(1)
    # db = DB()
    # with db as cursor:
    #     sql_str = "show tables"
    #     cursor.execute(sql_str)
    #     print(cursor.fetchall())
    import sys

    print(sys.executable)