import requests

from requests.utils import unquote

from Login.generate_proxy import get_ab_ip

url = "https://www.itslaw.com/api/v1/caseFiles?startIndex=20&countPerPage=20&sortType=1&conditions=searchWord%2B文书%2B1%2B文书"
refer = "https://www.itslaw.com/"
proxy = get_ab_ip()
headers = {
    "origin": "https://www.itslaw.com",
    "Referer": refer,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Cookie":"sessionId=68c29c6b-a91f-4f26-97e5-5e996d14503c;"
}

resp = requests.session().get(url,proxies=proxy,headers= headers)
# print(resp)
print(resp.json())

# print(url)

