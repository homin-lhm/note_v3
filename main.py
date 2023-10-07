import unittest
from BeautifulReport import BeautifulReport
import os

testLoader = unittest.TestLoader()
DIR = os.path.dirname(os.path.abspath(__file__))

ENVIRON = "Online"  # 线上 Online 测试环境 Offline


def run(test_suite):
    # 定义输出的文件位置和名字
    filename = 'report.html'
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='测试报告', report_dir='./')


if __name__ == '__main__':
    suite = testLoader.discover('./testCase', 'test*.py')
    run(suite)
