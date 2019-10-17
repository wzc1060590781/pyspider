from PIL import Image
from selenium import webdriver
import pytesseract

browser = webdriver.Chrome()
browser.get("http://my.cnki.net/elibregister/commonRegister.aspx#")
browser.find_element_by_xpath('//*[@id="checkcode"]').screenshot("a.png")
img = Image.open("a.png")
# img.show()
img = img.convert("L")
img.show()
threshold = 150
table = []
for i in range(256):
    if i <threshold:
        table.append(0)
    #
    else:
        print(1)
        table.append(1)
#
img = img.point(table,"1")
img.show()
# print(2)
print(pytesseract.image_to_string(img))