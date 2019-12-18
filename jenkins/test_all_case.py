#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from on_button_switch.case.lumi_ctrl_ln1_aq1_case import Ctrl_Ln1_Aq1_Case as T1
from on_button_switch.case.lumi_ctrl_ln1_v1_case import Ctrl_Ln1_V1_Case as T3
from on_button_switch.case.lumi_ctrl_neutral1_v1_case import Ctrl_Neutral1_V1_Case as T2
from on_button_switch.case.lumi_switch_b1lacn02_case import Switch_B1lacn02_Case as T4
from on_button_switch.case.lumi_switch_b1nacn02_case import Switch_B1nacn02_Case as T5
from util.server import Server
import unittest,HTMLTestRunner
class All_Cases():
    def run_test(self):
        server = Server()
        server.execute_command_on_thread()
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T3))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T4))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T5))
        filename = '../report//HTMLReport.html'
        with open(filename, 'wb') as  f:
            HTMLTestRunner.HTMLTestRunner(stream=f,
                                          title='MathFunc Test Report',
                                          description='测试报告详情:').run(suite)
        server.kill_server()


if __name__ ==   '__main__':
    test_cases = All_Cases()
    test_cases.run_test()


