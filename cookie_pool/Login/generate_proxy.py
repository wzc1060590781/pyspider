from config import PROXY_USER_NAME, PROXY_USER_PASS


def get_ab_ip():
    proxy_host = "http-dyn.abuyun.com"
    proxy_port = "9020"

    proxy_user =PROXY_USER_NAME
    proxy_pass = PROXY_USER_PASS

    proxy_meta="http://%(user)s:%(pass)s@%(host)s%(port)s"%{
        "host":proxy_host,
        "port":proxy_port,
        "user":proxy_user,
        "pass":proxy_pass,
    }
    return {"http":proxy_meta}