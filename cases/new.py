#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from cases.lumi_european_standard_case import European_Standard_Case as  T1
from cases.lumi_sensor_ht_v1_case import Sensor_Ht_V1_Case as T2
from util.server import Server
import unittest,HTMLTestRunner

class All_Cases():
    def get_choose_device_from_jenkins(self):
        choose_device_list = sys.argv[1:]
        print(len(sys.argv))
        # ['"lumi.sensor.ht.v1，lumi.sensor.ht.v1"']
        choose_device_list = choose_device_list
        print('用户选择的参数:',choose_device_list)
        self.run_test(choose_device_list)

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
            if choose_device_list[item] == "lumi.european.standard":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
            if choose_device_list[item] == "lumi.sensor.ht.v1":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
            if choose_device_list[item] == "all_case":
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
        filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'
        with open(filename, 'wb') as  f:
            HTMLTestRunner.HTMLTestRunner(stream=f,
                                          title='MathFunc Test Report',
                                          description='测试报告详情:').run(suite)
        server.kill_server()

if __name__ ==   '__main__':
    # list= ['"lumi_sensor_ht_v1_case"']
    # list = ['"lumi.sensor.ht.v1，lumi.sensor.ht.v1"']
    # print(list)
    # total_str = list[0].strip("\"")
    # print(total_str,type(total_str))
    # class_list = total_str.split('，')
        # for i in range(len(class_list)):
        #     print(class_list[i]）
    test_cases = All_Cases()
    test_cases.get_choose_device_from_jenkins()


