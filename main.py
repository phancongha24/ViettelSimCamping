import re
import time

from selenium import webdriver

import requests
from bs4 import BeautifulSoup
# driver = webdriver.PhantomJS("D:\Python\driver\phantomjs.exe",service_args=['--ignore-ssl-errors=true'])
# driver.get('http://shop.viettel.vn')
# xBlockRequest = driver.find_element_by_name("x_block_request").get_attribute("value")
# driver.close()
from ViettelSimCamping import ViettelSimCamping

data={
    'vt_signin[_csrf_token]': '3bce835a9881c6cfe6246b8cc37b7015',
    'vt_signin[phone]': '0929315514',
    'vt_signin[password]': 'Hoanghaigod12@@',
    'object_value': ''
}
ViettelSimCamping()
exit(1)
headers= {
    "x-vtshop-header" : xBlockRequest
  }
# while True:
#     soup = BeautifulSoup(request.get('https://shop.viettel.vn/ajax/tim-kiem-sim?is_commitment=1&number=&_='+str(int(time.time())),headers=headers).text,"xml")
#     listNumber=soup.findAll("td",{"class":"col-number"})
#     for number in listNumber:
#         phoneNumber = number.findChildren()[0].text
#         print(phoneNumber)
#

