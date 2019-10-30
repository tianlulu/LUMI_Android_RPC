#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from cases.lumi_plug_mmeu01_case import European_Standard_Case as  T1
from cases.lumi_sensor_ht_v1_case import Sensor_Ht_V1_Case as T2
from cases.lumi_ctrl_ln1_aq1_case import Ctrl_Ln1_Aq1_Case as T3
from util.server import Server
import unittest,HTMLTestRunner

class All_Cases():
    def get_choose_device_from_jenkins(self):
        try:
            choose_device_list = sys.argv[1:]
            print(len(sys.argv))
            print('用户选择的参数:', choose_device_list)
            self.run_test(choose_device_list)
        except Exception as e:
            print(sys.argv)
            print(e)


    def run_test(self,device_list):
        # print('设备枚举:', device_list, type(device_list))
        total_str = device_list[0].strip("\"")
        # print('去掉引号:',total_str, type(total_str))
        choose_device_list = total_str.split('，')
        # print('逗号分隔:',choose_device_list)

        server = Server()
        server.execute_command_on_thread()
        suite = unittest.TestSuite()
        for item in range(len(choose_device_list)):
            model = choose_device_list[item].split(':')[1]
            if model == "lumi.plug.mmeu01":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
            if model == "lumi.sensor.ht.v1":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
            if model == "lumi.ctrl_ln1.aq1":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T3))
            if model == "all_case":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T3))
        filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'
        with open(filename, 'wb') as  f:
            HTMLTestRunner.HTMLTestRunner(stream=f,
                                          title='MathFunc Test Report',
                                          description='测试报告详情:').run(suite)
        server.kill_server()


if __name__ ==   '__main__':
    # list = ['"欧标插座:lumi.plug.mmeu01，米家温湿度:lumi.sensor.ht.v1，Aqara墙壁开关(零火线单键版):lumi.ctrl_ln1.aq1"']
    # print(list)
    # total_str = list[0].strip("\"")
    # print(total_str,type(total_str))
    # class_list = total_str.split('，')
    # print(class_list,type(class_list))
    # for i in range(len(class_list)):
    #     print(class_list[i])
    #     print(class_list[i].split(':')[1])

    test_cases = All_Cases()
    test_cases.get_choose_device_from_jenkins()


