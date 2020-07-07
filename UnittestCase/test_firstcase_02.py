import requests
import json
import unittest
abc = '123'
class TestCase02(unittest.TestCase):
    def setUp(self) -> None:
        print('case开始执行')
    def tearDown(self) -> None:
        print('case结束执行')
    @classmethod
    def setUpClass(cls) -> None:
        print('第二个类执行')
    @classmethod
    def tearDownClass(cls) -> None:
        print('第二个类结束')

    def test_01(self):
        print('第一条case')
        a = '123'
        self.assertEqual(a,abc)
    def test_02(self):
        print('第二条case')
        a = '111'
        self.assertEqual(a,abc)
    def test_03(self):
        print('第三条case')
        a = True
        self.assertTrue(a,msg='第三条case结果')
    def test_04(self):
        print('第四条case')
        a = True
        self.assertFalse(a,msg='第四条case结果')
if __name__ == '__main__':
    '''
    //全部执行
    unittest.main()
    '''
    suite = unittest.TestSuite()
    tests = [TestCase02('test_01'),TestCase02('test_04')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)