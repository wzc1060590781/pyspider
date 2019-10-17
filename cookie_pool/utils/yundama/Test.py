# -*- coding: cp936 -*-

import sys
import os
from urllib.request import urlretrieve
from ctypes import *

class Code():

    def __init__(self):
        self.YDMApi = windll.LoadLibrary('yundamaAPI-x64')
        self.appId = 7452  # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
        self.appKey = b'6a1b9884fbf80b37bab5173f70733402'  # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
        # print('软件ＩＤ：%d\r\n软件密钥：%s' % (self.appId, self.appKey))
        self.username = b'645064301'
        self.password = b'qwert12358'
        # self.code_name = code_name
        if self.username == b'test':
            exit('\r\n>>>请先设置用户名密码')


    ####################### 一键识别函数 YDM_EasyDecodeByPath #######################
    def identify_key(self,website):
        # print('\r\n>>>正在一键识别...')
        # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
        codetype = 1004

        # 分配30个字节存放识别结果
        result = c_char_p(b"                              ")

        # 识别超时时间 单位：秒
        timeout = 60

        # 验证码文件路径
        filename = "{}.jpg".format(website).encode()
        print(filename)

        # 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
        captchaId = self.YDMApi.YDM_EasyDecodeByPath(self.username, self.password, self.appId, self.appKey, filename, codetype, timeout, result)

        # print("一键识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
        print(result.value.decode("utf-8"))
        return result.value.decode("utf-8")

    def identify_ordinary(self):

        ################################################################################
        ########################## 普通识别函数 YDM_DecodeByPath #########################


        # print('\r\n>>>正在登陆...')

        # 第一步：初始化云打码，只需调用一次即可
        self.YDMApi.YDM_SetAppInfo(self.appId, self.appKey)

        # 第二步：登陆云打码账号，只需调用一次即可
        uid = self.YDMApi.YDM_Login(self.username, self.password)

        if uid > 0:

            # print('>>>正在获取余额...')

            # 查询账号余额，按需要调用
            balance = self.YDMApi.YDM_GetBalance(self.username, self.password)

            # print('登陆成功，用户名：%s，剩余题分：%d' % (self.username, balance))

            # print('\r\n>>>正在普通识别...')

            # 第三步：开始识别

            # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
            codetype = 1004

            # 分配30个字节存放识别结果
            result = c_char_p(b"                              ")

            # 验证码文件路径
            filename = b'code.png'

            # 普通识别函数，需先调用 YDM_SetAppInfo 和 YDM_Login 初始化
            captchaId = self.YDMApi.YDM_DecodeByPath(filename, codetype, result)

            # print("普通识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
            return result.value.decode("utf-8")
        else:
            # print('登陆失败，错误代码：%d' % uid)
            return "识别失败！"

        ################################################################################

        # print('\r\n>>>错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html')
        #
        # input('\r\n测试完成，按回车键结束...')


if __name__ == '__main__':
    c = Code()
#     # filename = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "/register_code_image/13438197166.png")
    website = "1"
    str = "{}.jpg".format(website)
    print(str.encode())
    # print(str("1"))