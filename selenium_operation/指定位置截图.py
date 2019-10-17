from selenium import webdriver


browser  = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_xpath('//*[@id="qrcode"]/div/div[1]').screenshot("a.jpg")
