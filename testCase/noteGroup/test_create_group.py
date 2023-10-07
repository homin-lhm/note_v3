import unittest
import requests
import time
from common.checkRes import CheckRes
from parameterized import parameterized
from copy import deepcopy


class TestPro(unittest.TestCase):
    host = 'http://note-api.wps.cn'
    cR = CheckRes()
    mustKeys = [[{'key': 'groupId', 'code': 403}], [{'key': 'groupName', 'code': 500}]]
    base = {
            'groupId': '123',
            'groupName': 'testGroup',
            'order': 0,
            'identify': {
                'app_id': '',
                'user_id': ''
            },
            'group_id': '',
            'user_num_limit': 0,
            'group_id1': '',
            'user_num_limit2': 0,
            'group_id3': '',
            'user_num_limit4': 0
        }

    def testCase01_major(self):
        """新增便签的主流程"""
        path = '/v3/notesvr/set/notegroup'
        headers = {
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd',
            'X-user-key': '922061821',
            'Content-Type': 'application/json'
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = deepcopy(self.base)
        body['group_id'] = group_id

        res = requests.post(url=self.host + path, headers=headers, json=body)
        self.assertEqual(200, res.status_code, msg='状态码异常')
        expected = {
            'responseTime': int,
            'updateTime': int
        }
        self.cR.check_output(expected=expected, actual=res.json())

        # get_path = '/v3/notesvr/get/notegroup'
        # body = {}
        # res = requests.post(url=self.host + get_path, headers=headers, json=body)
        # group_id_list = []
        # for item in res.json()['noteGroups']:
        #     group_id_list.append(item['groupId'])
        # self.assertIn(group_id, group_id_list)

    @parameterized.expand(mustKeys)
    def testCase02_input_must_key(self, item):
        """必填项校验"""
        print('testCase start')
        path = '/v3/notesvr/set/notegroup'
        headers = {
            'Cookie': 'wps_sid=V02SG3oIwfZGY3-EWrNqRBP1J1oAr6E00ab36a440036f58bfd',
            'X-user-key': '922061821',
            'Content-Type': 'application/json'
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': group_id,
            'groupName': 'testGroup',
            'order': 0

        }
        body.pop(item['key'])
        res = requests.post(url=self.host + path, headers=headers, json=body)
        self.assertEqual(item['code'], res.status_code, msg='状态码异常')
        expected = {
            'errorCode': -7,
            'errorMsg': '参数不合法！'
        }
        self.cR.check_output(expected=expected, actual=res.json())
