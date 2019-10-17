class LoginDatas():
    def __init__(self):
        pass

    def jufa_get_login_data(self, phone_number, password):
        """
        生成聚法post请求所需data
        :param phone_number:
        :param password:
        :return:
        """
        data = {
            "user": phone_number,
            "password": password,
            "is_remember": "1"
        }
        print(2)
        return data

    def jufa_get_login_headers(self):
        """
        生成聚法请求头
        :return: 请求头字典
        """
        headers ={
                "origin": "https://www.jufaanli.com",
                "referer": "https://www.jufaanli.com/",
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
        return headers

    def wusong_login_data(self, phone_number, password):
        data = {
            "userName": phone_number,
            "password": password,
            "isAutoLogin": False
        }
        return data

    def wusong_get_login_headers(self):
        """
        生成聚法请求头
        :return: 请求头字典
        """
        headers ={
                "origin": "https://www.itslaw.com",
                "referer": "https://www.itslaw.com/bj",
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            }
        return headers