#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from cases.lumi_plug_mmeu01_case import European_Standard_Case as  T1
from cases.lumi_sensor_ht_v1_case import Sensor_Ht_V1_Case as T2
from cases.lumi_ctrl_ln1_aq1_case import Ctrl_Ln1_Aq1_Case as T3
from cases.lumi_ctrl_neutral1_v1_case import Ctrl_Neutral1_V1_Case as T4
from util.server import Server
import unittest,HTMLTestRunner
from util.freedom_name import My_Custom_Name

'''
1、找房间
2、找设备
3、运行该设备用例 
'''
class All_Cases():
    def get_choose_device_from_jenkins(self):
        try:
            choose_info = sys.argv[1:]
            # print('参数个数', len(choose_info))
            print('用户选择的参数:', choose_info)
            return choose_info
        except Exception as e:
            print(sys.argv)
            print(e)

    def deal_device_info(self):
        # choose_list_info = self.get_choose_device_from_jenkins()
        # choose_list_info = ['222', '222', 'lumi.european.standard', 'jjj', 'kk', 'kkk', 'kkk', '888', '999', '00000',
        #                '', '','ddd','eee','lumi.sensor.ht.v1']
        # [ 'Sweet', 'Sweet-米家温湿度', 'lumi.sensor.ht.v1','Sweet', 'Sweet-欧标插座', 'lumi.european.standard','','','']
        choose_list_info = self.get_choose_device_from_jenkins()
        # print('用户选择的设备:',choose_list_info)
        temp_list = []
        for item in self.split_list(choose_list_info, 3):
            # print('item:',item)
            if('' not in item):
                temp_list.append(item)
            # else:
                # print('设备的信息不完整')
        print('处理后用户的设备', temp_list)
        return temp_list

    def run_test(self):
        server = Server()
        server.execute_command_on_thread()
        suite = unittest.TestSuite()
        my_custom_name = My_Custom_Name()
        device_list = self.deal_device_info()

        for device_info in range(len(device_list)):
            print('device_info:',device_list[device_info])
            room_name = device_list[device_info][0]
            device_name = device_list[device_info][1]
            model = device_list[device_info][2]
            print('room_name:',room_name,type(room_name))
            print('device_name:',device_name,type(device_name))
            print('model:',model,type(model))

            if model == "lumi.plug.mmeu01":
                print('lumi.european.standard')
                my_custom_name.set_european_standard_room_name(room_name)
                my_custom_name.set_european_standard_device_name(device_name)
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T1))
            if model == "lumi.sensor.ht.v1":
                print('lumi.sensor.ht.v1')
                my_custom_name.set_sensor_ht_v1_room_name(room_name)
                my_custom_name.set_sensor_ht_v1_device_name(device_name)
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T2))
            if model == "lumi.ctrl_ln1.aq1":
                print('lumi.ctrl_ln1.aq1')
                my_custom_name.set_ctrl_ln1_aq1_room_name(room_name)
                my_custom_name.set_ctrl_ln1_aq1_device_name(device_name)
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T3))
            if model == "lumi.ctrl_neutral1.v1":
                print('lumi.ctrl_neutral1.v1')
                my_custom_name.set_ctrl_neutral_v1_room_name(room_name)
                my_custom_name.set_ctrl_neutral_v1_device_name(device_name)
                suite.addTests(unittest.TestLoader().loadTestsFromTestCase(T4))
        filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'
        with open(filename, 'wb') as  f:
            HTMLTestRunner.HTMLTestRunner(stream=f,
                                          title='MathFunc Test Report',
                                          description='测试报告详情:').run(suite)
        server.kill_server()

    def split_list(self,listTemp, n):
        for i in range(0, len(listTemp), n):
            yield listTemp[i:i + n]

if __name__ ==   '__main__':
    test_cases = All_Cases()
    test_cases.run_test()



