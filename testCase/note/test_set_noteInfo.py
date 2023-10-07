import unittest
import requests


class NoteInfoTestPro(unittest.TestCase):
    def testCase01_major(self):
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes'.format(922061821, 0, 10)
        cookie = {
            'wps_sid': 'V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        res = requests.get(url=host + path, cookies=cookie)
        self.assertEqual(200, res.status_code, msg='状态码异常')
        # print(res.json())

    def testCase02_input_check(self):
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes'.format('', 0, 10)
        cookie = {
            'wps_sid': 'V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        res = requests.get(url=host + path, cookies=cookie)
        # print(res.status_code)
        # print(res.json())
