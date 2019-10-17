from Register.jufa_register import jufa_Register
from saver import Savor
from Register.wusong_register import wusong_Register

class Register():
    def __init__(self,website):
        self.website = website
        # eval('from Register.'+website+'_register import '+website+'_Register')
        self.website_register = eval(website + '_Register("' + website + '")')


    def get_cookie(self):
        cookie_user_password_dict = eval("self.website_register."+self.website+"_get_register_cookie()")
        phone_number = cookie_user_password_dict["phone_number"]
        cookie = cookie_user_password_dict["cookie"]
        password = cookie_user_password_dict["password"]
        self.save_cookie(phone_number,cookie)
        with open("phone_cookie.txt","a") as f:
            f.write(phone_number+":"+cookie+"\n")
        self.save_user(phone_number,password)
        with open("phone_password.txt", "a") as f:
            f.write(phone_number + ":" + password + "\n")


    def save_cookie(self,phone_number,cookie):
        type = "cookie"
        sv = Savor(type, self.website)
        sv.insert_into_cookie_table(phone_number, cookie)

    def save_user(self,phone_number,password):
        type = "user"
        sv = Savor(type, self.website)
        sv.insert_into_user_table(phone_number, password)


if __name__ == '__main__':
    website = "wusong"
    register = Register("wusong")
    register.get_cookie()