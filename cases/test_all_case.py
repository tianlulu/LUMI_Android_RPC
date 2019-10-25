#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from cases.lumi_plug_mmeu01_case import European_Standard_Case as  T1
from cases.lumi_sensor_ht_v1_case import Sensor_Ht_V1_Case as T2
from util.server import Server
import unittest,HTMLTestRunner

class All_Cases():
    def run_test(self):
        server = Server()
        server.execute_command_on_thread()
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
        filename = '../report//HTMLReport.html'
        with open(filename, 'wb') as  f:
            HTMLTestRunner.HTMLTestRunner(stream=f,
                                          title='MathFunc Test Report',
                                          description='测试报告详情:').run(suite)
        server.kill_server()


if __name__ ==   '__main__':
    test_cases = All_Cases()
    test_cases.run_test()


