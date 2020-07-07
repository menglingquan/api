#封装请求
import requests
import json
from Util.handle_json import get_value
from Util.handle_ini import get_ini
class BaseRequest:
    def send_post(self,url,data):
        '''
        发送post请求
        '''
        res = requests.post(url=url,data=data).text
        return res
    def send_get(self,url,data):
        '''
        发送get请求
        '''
        res = requests.get(url=url,params=data).text
        return res
    def run_main(self,method,url,data):
        return get_value(url)
        base_url = get_ini.get_value('host')
        if 'http' not in url:
            url = base_url + url

        if method == "get":
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        try:
            res = json.loads(res)
        except:
            print('这是个text呀')
        return res
request_base = BaseRequest()
if __name__ == '__main__':
    request_base = BaseRequest()
    request_base.run_main('get','login/','{"n":"1","b":"2"}')