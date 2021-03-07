import re

import requests
class ViettelSimCamping:
    baseUrl = "http://shop.viettel.vn/"
    def __init__(self):
        self.request = requests.Session()
        self.request.cookies['D1N'] = re.search("D1N=(.*?);window", self.request.get(ViettelSimCamping.baseUrl).text).group(
            1).replace('"+"', "")
        self.init()
    def init(self):
        request =self.request.get(ViettelSimCamping.baseUrl)
        matches = re.findall('x_block_request" value="(.*?)"|csrf_token" value="(.*?)"', request.text)
        self.xBlockRequest = matches.pop()[0]
        self.csrfToken = matches.pop()[0]
  #       data={
  #           'vt_signin[_csrf_token]': self.csrfToken,
  #           'vt_signin[phone]': '0929315514',
  #           'vt_signin[password]': 'Hoanghaigodd12@@',
  #           'object_value': ''
  #       }
  #       headers={
  #   "accept": "*/*",
  #   "accept-language": "en-US,en;q=0.9",
  #   "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  #   "sec-fetch-dest": "empty",
  #   "sec-fetch-mode": "cors",
  #   "sec-fetch-site": "same-origin",
  #   "x-requested-with": "XMLHttpRequest"
  # }
  #       print(self.request.post(ViettelSimCamping.baseUrl+"ajax/dang-nhap",data=data,headers=headers).text)

