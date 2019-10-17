import MySQLdb


class DB():
    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", database="wusong", user="root",password="mysql", charset='utf8')
        self.cs1 = self.conn.cursor()

    def __enter__(self):
        return self.cs1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cs1.close()
        self.conn.close()