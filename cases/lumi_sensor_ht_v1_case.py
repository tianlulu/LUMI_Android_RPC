#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import HTMLTestRunner
import unittest
from util.server import Server
from util.write_user_command import WriteUserCommand
from util.operation_json import OperationJson
from handle.lumi_sensor_ht_v1_handle import Sensor_Ht_V1_Handle
from dos.dos_cmd import DosCmd
from base.base_driver import DriverUtil
import time

class Sensor_Ht_V1_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始Sensor_Ht_V1_Case')
        global operation_json
        operation_json = OperationJson()
        cls.sensor_ht_v1_handle = Sensor_Ht_V1_Handle()

    def setUp(self):
        print('setUp')

    def test_case1(self):
        '''找到米家温湿度设备'''
        global device_exists
        device_exists = self.sensor_ht_v1_handle.get_room_sensor_ht_v1_element()
        self.assertTrue(device_exists, '滑动到底部仍然没有找到设备')

    def test_case2(self):
        '''进入温湿度首页(get_device_prop_exp)'''
        self.assertTrue(device_exists, '该设备不在房间内')

        global is_no_network
        is_no_network = self.sensor_ht_v1_handle.get_fail_toast('请求失败，请检查网络')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')

        # 判断设备是否离线状态
        global is_offline
        is_offline = self.sensor_ht_v1_handle.is_offline_element()
        self.assertFalse(is_offline,'设备已离线，请重新连接设备')

        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'get_device_prop_exp')
        param_list = data['params'][0]

        self.assertTrue(param_list[1] == 'temperature','请求参数错误：预期参数：temperature 实际参数：' + param_list[1])
        self.assertTrue(param_list[2] == 'humidity','请求参数错误：预期参数：humidity 实际参数：' + param_list[2])
        for value in param_list:
            print('params中带有' + value + '参数')


    def test_case3(self):
        '''返回首页吧：滑动到顶部'''
        '''
        if is_offline():
            1、点击关闭按钮
            2、点击返回首页   
        '''
        if device_exists == False:
            print('设备不在房间内')
            self.assertTrue(self.sensor_ht_v1_handle.click_universal_back_element(), '返回到房间列表的箭头按钮不存在')
            self.assertTrue(self.sensor_ht_v1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")
            return

        if is_no_network:
            self.expected_conditions()
            return

        if is_offline:
            print('设备离线状态')
            self.assertTrue(self.sensor_ht_v1_handle.click_offline_close(), '离线框右上角关闭按钮不存在')
            self.expected_conditions()
            return

        self.expected_conditions()

    def expected_conditions(self):
        self.assertTrue(self.sensor_ht_v1_handle.click_use_back_element(), '返回到房间里面的箭头按钮不存在')
        self.assertTrue(self.sensor_ht_v1_handle.click_universal_back_element(), '返回到房间列表的箭头按钮不存在')
        self.assertTrue(self.sensor_ht_v1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

# appium_init初始化
def appium_init():
    server = Server()
    server.execute_command_on_thread()

# 通过yaml中的个数获取运行的进程个数()
def get_count():
    write_file =WriteUserCommand()
    return write_file.get_yaml_file_lines()

def get_suite():
    # 定义一个测试容器
    suite = unittest.TestSuite()
    suite.addTest(Sensor_Ht_V1_Case('test_case1'))
    suite.addTest(Sensor_Ht_V1_Case('test_case2'))
    suite.addTest(Sensor_Ht_V1_Case('test_case3'))
    # unittest.TextTestRunner().run(suite)
    # 定义个报告存放的路径，支持相对路径
    # filename = '../report/tesecase'+str(i)+'_report'+'.html'
    filename = '../report/HTMLReport.html'
    # filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'

    file_result = open(filename, 'wb')
    # 定义测试报告
    HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                  title='米家温湿度测试报告',
                                  description='测试报告详情:').run(suite)
    file_result.close()


if __name__ == '__main__':
    server = Server()
    server.execute_command_on_thread()
    # appium_init()
    get_suite()
    server.kill_server()


