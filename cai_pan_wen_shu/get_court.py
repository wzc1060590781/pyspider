# import selenium
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class Court():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = "http://wenshu.court.gov.cn/"
        # self.url = "http://www.baidu.com"


    def __(self):
        self.browser.get(self.url)

    # def serarch_caipanwenshu(self):
    #     self.browser.find_element_by_xpath('//*[@id="kw"]').send_keys("中国裁判文书网")
    #     # self.browser.find_element_by_xpath()

    def get_province_doom(self):
        province_list = self.browser.find_elements_by_xpath('//*[@id="idx_map_content"]/*')
        for province in province_list[19:]:
            print("正在写入："+province.text)
            province.click()
            with open(province.text + ".txt", "a", encoding="utf-8") as f:
                li_list = self.browser.find_elements_by_xpath('//*[@id="_view_1541490383000"]/div/ul/*')
                # li_list = self.browser.find_elements_by_xpath('//*[@id="_view_1541491038000"]/div/div/ul/*')
                for i in li_list:
                    time.sleep(0.5)
                    f.write(i.text+"\n")
                    ActionChains(self.browser).move_to_element(i).perform()
                    childern_doom_list = self.browser.find_elements_by_xpath('//*[@id="_view_1541491038000"]/div/div/ul/li[position()>1]')
                    # childern_doom_list = self.browser.find_elements_by_xpath('//*[@id="_view_1541490383000"]/div/ul/li[position()>1]')
                    for i in childern_doom_list:
                        # time.sleep(0.5)n
                        f.write(i.text+"\n")
                print("第"+str(province_list.index(province))+ "个完成")
                print(province.text+"完成")



        # print(len(province_list))
        # print(len(province_list))

    def parse_court(self):
        province_list = os.listdir("./法院")
        for province in province_list:
            remove_list = []
            with open(province,"r",encoding="utf-8") as f:
                str_list = f.readlines()
                for str in str_list:
                    if len(str) == 0:
                        remove_list.append(str)
                for i in remove_list:
                    str_list.pop(i)
if __name__ == '__main__':
    court = Court()
    # court.parse_court()
    court.__()
    court.get_province_doom()
    # court.get_province_doom()
