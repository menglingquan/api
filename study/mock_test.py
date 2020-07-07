import mock
import requests
import json
import unittest
url = ""
data = {

}
def post_request(url,data):
    res = requests.post(url,data).json()
    return res
class TestLogin(unittest.TestCase):
    def test_01(self):
        url = ""
        data = {

        }
        suc_test = mock.Mock(return_value=data)
        post_request = suc_test
        res = post_request
        self.assertEqual("",res())
if __name__ == '__main__':
    unittest.main()