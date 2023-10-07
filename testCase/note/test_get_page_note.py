import unittest
import requests
from common.checkRes import CheckRes
from common.yamlOperator import YamlOperator


class GetPageNote(unittest.TestCase):  # 基于接口定义类名
    cR = CheckRes()
    envConfig = YamlOperator().env_config()
    getNotePageConfig = YamlOperator().api_data_config('getPageNote')
    host = envConfig['host']
    sid1 = envConfig['sid1']
    userId1 = envConfig['userId1']
    key = envConfig['key'].encode('utf-8')
    iv = envConfig['iv'].encode('utf-8')
    mustKeys = getNotePageConfig['mustKeys']
    '''类属性提取了环境变量、接口请求数据变量，并实现数据驱动'''

    def setUp(self):  # 初始化   1.造数据  2.登录  3.清空数据
        print('setUp')

    def tearDown(self) -> None:  # 后置清数据  断开链接close方法
        print('tearDown')

    def testCase01_major(self):
        """
        1.方法名：testCase01_noteId_num_0  方法名前缀需要满足装饰器的通配符和unittest的通配符
        2.注释：用例描述  用例名
        3.基于step日志输出方式  定义步骤描述
        4.请求数据的框架 处理
        5.断言 对齐文档、校验状态码、校验数据源

        :return:
        """
        path = '/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes'.format(self.userId1, 0, 10)
        cookie = {
            'wps_sid': self.sid1
        }
        res = requests.get(url=self.host + path, cookies=cookie)
        actual = {'responseTime': 0, 'webNotes': [
            {'noteId': '541b304e2e027d0f306082d71a85ee9d', 'createTime': 1687589107415, 'star': 0, 'remindTime': 0,
             'remindType': 0, 'infoVersion': 1, 'infoUpdateTime': 1687589107415, 'groupId': None,
             'title': '75u8dlZyTLqWCm/b2PLNlg==',
             'summary': 'nt3Dle5eb6GKl8Pyqhy5iipBwM8uLHuhwUR6wl3Vz20eTfZzKyBzJoI7X81jH/'
                        'M5GOOypvmAnUGca+GXnfz3A2ALsFb09vElESI7N5ZTsNZ8InObDa9wj00oMMlVGRqTE1oSMNLq7kCPV+rqvWS+rA==',
             'thumbnail': None, 'contentVersion': 21, 'contentUpdateTime': 1690553813588}]}

        expected = {
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': '541b304e2e027d0f306082d71a85ee9d',
                    'createTime': int,
                    'star': 0,
                    'remindTime': int,
                    'remindType': 0,
                    'infoVersion': int,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': str,
                    'summary': str,
                    'thumbnail': None,
                    'contentVersion': int,
                    'contentUpdateTime': int
                }
            ]
        }

        self.cR.check_output(expected, actual)

    def testCase02_input_check(self):
        host = 'http://note-api.wps.cn'
        path = '/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes'.format('', 0, 10)
        cookie = {
            'wps_sid': 'V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd'
        }
        res = requests.get(url=host + path, cookies=cookie)
        # print(res.status_code)
        # print(res.json())

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
