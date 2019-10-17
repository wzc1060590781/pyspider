from Register.register import Register
from datebase import DB
from Login.login import Login


class CookieGenerator():
    def __init__(self, website):
        self.website = website
        self.db = DB()
        self.cookie_table_name = "cookie_{}".format(website)
        self.user_table_name = "user_{}".format(website)
        self.login = Login(self.website)

    def generate_login_cookie(self, phone_number, password):
        cookie = eval("self.login.generate_" + self.website + "_login_cookie({phone_number},{password})".format(
            phone_number=phone_number, password=password))
        return cookie

    def generate_register_cookie(self):
        register = Register(self.website)
        cookie = register.get_cookie()
        return cookie


if __name__ == '__main__':
    cg = CookieGenerator("jufa")
    cg.generate_login_cookie(111, 222)
