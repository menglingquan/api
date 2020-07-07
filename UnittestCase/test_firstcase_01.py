import requests
import json
import unittest
from Base.base_request import request_base
abc = '123'
url = "http://www.imooc.com"
data = {
    "username":"1111",
    "password":"22222"
}
class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print('case开始执行')
    def tearDown(self) -> None:
        print('case结束执行')
    @classmethod
    def setUpClass(cls) -> None:
        print('第一个类执行')
    @classmethod
    def tearDownClass(cls) -> None:
        print('第一个类结束')
    @unittest.skip('第一个类的第一个方法不执行')
    def test_01(self):
        print('第一条case')
        a = '123'
        self.assertEqual(a,abc)
    @unittest.skipIf(4<5,'这个case是否执行跟前面的判断是否成立有关')
    def test_02(self):
        print('第二条case')
        a = '111'
        self.assertEqual(a,abc)
    @unittest.skip('不执行')
    def test_03(self):
        print('第三条case')
        a = True
        self.assertTrue(a,msg='第三条case结果')
    def test_04(self):
        res = request_base.run_main('get',url,data)
        print(res)
if __name__ == '__main__':

    # 全部执行
    unittest.main()
    '''
    suite = unittest.TestSuite()
    tests = [TestCase01('test_01'),TestCase01('test_04')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''