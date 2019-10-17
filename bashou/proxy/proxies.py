import config


def get_ab_ip():
    # 要访问的目标页面
    # targetUrl = "http://test.abuyun.com"
    # targetUrl = "http://proxy.abuyun.com/switch-ip"
    # targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = config.config["proxyUser"]
    proxyPass = config.config["proxyPass"]

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }
    return {'http':proxyMeta}

if __name__ == '__main__':
    print(get_ab_ip())