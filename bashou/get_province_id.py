import json


def get_province_id():
    with open("province.json","r",encoding="utf-8") as f:
        dict_court = {}
        dict = json.load(f)
        for i in dict["facetFields"]["provinceId"]:
            name = i["name"]
            id = i["id"]
            dict_court[name] = id
    with open("province_court_id.json","w",encoding="utf-8") as f:
        json.dump(dict_court,f,ensure_ascii=False,indent=2)


get_province_id()