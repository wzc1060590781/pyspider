import requests

from proxy.proxies import get_ab_ip


def download(self,id,cookie,name):
    proxy = get_ab_ip()
    headers = {
        "Host": "www.lawsdata.com",
        "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Cookie": cookie
    }
    resp = requests.get("http://www.lawsdata.com/u/download/word?id="+id, headers=headers,proxies = proxy)
    with open(name+".docx", "wb") as f:
        f.write(resp.content)