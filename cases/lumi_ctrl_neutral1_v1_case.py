#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import unittest
from util.operation_json import OperationJson
from util.server import Server
import HTMLTestRunner
from handle.lumi_ctrl_neutral1_v1_handle import Ctrl_Neutral1_V1_Handle

'''
Aqara墙壁开关(单火线单键版)测试用例
'''
class Ctrl_Neutral1_V1_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('开始Ctrl_Neutral1_V1_Case')
        cls.ctrl_neutral1_v1_handle = Ctrl_Neutral1_V1_Handle()
        cls.operation_json = OperationJson()

    def setUp(self) -> None:
        print('setUp')

    def test_case1(self):
        '''找出Aqara墙壁开关(零火线单键版)'''
        global room_exists
        room_exists = self.ctrl_neutral1_v1_handle.click_room_element()
        self.assertTrue(room_exists,'滑动到底部仍然没有找到房间')

        global device_exists
        device_exists = self.ctrl_neutral1_v1_handle.click_device_element()
        self.assertTrue(device_exists, '滑动到底部仍然没有找到设备')

    def test_case2(self):
        '''进入首页(get_device_prop_exp)'''
        self.assertTrue(room_exists,'房间不存在')
        self.assertTrue(device_exists, '设备不存在')

        global is_no_network
        is_no_network = self.ctrl_neutral1_v1_handle.get_fail_toast('请求失败，请检查网络')
        self.assertFalse(is_no_network,'无网络状态，请联网后重试')

        # 判断设备是否离线状态
        global is_offline
        is_offline = self.ctrl_neutral1_v1_handle.is_offline_element()
        self.assertFalse(is_offline,'设备已离线，请重新连接设备')

        data = self.operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'get_device_prop_exp')
        param_list = data['params'][0]

        self.assertTrue(param_list[1] == 'channel_0','请求参数错误：预期参数：channel_0 实际参数：' + param_list[1])
        self.assertTrue(param_list[2] == 'load_power','请求参数错误：预期参数：load_power 实际参数：' + param_list[2])
        for value in param_list:
            print('params中带有' + value + '参数')


    def test_case3(self):
        '''打开/关闭开关（toggle_ctrl_neutral)'''
        self.assertTrue(room_exists, '房间不存在')
        self.assertTrue(device_exists, '设备不存在')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        gray_rgba = (216, 216, 216, 255)
        rgba = self.ctrl_neutral1_v1_handle.get_light_bulb_element_rgba()
        print('得到的灯泡颜色为:',rgba)
        self.assertTrue(self.ctrl_neutral1_v1_handle.click_on_off_light_element(), '找不到开关按钮')
        if rgba == gray_rgba:
            self.set_toggle_plug_on()
        else:
            self.set_toggle_plug_off()


    def set_toggle_plug_on(self):
        '''打开开关'''
        print('打开开关')
        data = self.operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        self.assertEqual(method, 'toggle_ctrl_neutral')
        param_values = data['params']
        print('method:' + method)
        self.assertTrue('channel_0' == param_values[0], '请求参数错误：预期参数：channel_0 实际参数：' + param_values[0])
        self.assertTrue('on' == param_values[1], '请求参数错误：预期参数：on 实际参数：' + param_values[1])
        for value in param_values:
            print('params中带有' + value + '参数')


    def set_toggle_plug_off(self):
        '''关闭开关'''
        print('关闭开关')
        data = self.operation_json.read_data()
        print('请求参数:',data)
        method = data['method']
        self.assertEqual(method,'toggle_ctrl_neutral')
        param_values = data['params']
        self.assertTrue('channel_0' == param_values[0],'请求参数错误：预期参数：channel_0 实际参数：' + param_values[0])
        self.assertTrue('off' == param_values[1],'请求参数错误：预期参数：off 实际参数：' + param_values[1])
        for value in param_values:
            print('params中带有' + value + '参数')


    def test_case4(self):
        '''返回首页：滑动到顶部'''
        if room_exists == False:
            print('房间不存在')
            self.assertTrue(self.ctrl_neutral1_v1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")
            return

        if device_exists == False:
            print('设备不存在')
            self.assertTrue(self.ctrl_neutral1_v1_handle.click_room_list_back_element(),'返回到房间列表的箭头按钮不存在')
            self.assertTrue(self.ctrl_neutral1_v1_handle.scroll_to_top(),'下滑到最后没有找到+按钮')
            return

        if is_no_network:
            print('无网络状态')
            self.expected_conditions()
            return

        if is_offline:
            print('设备离线状态')
            self.assertTrue(self.ctrl_neutral1_v1_handle.click_offline_close(),'离线框右上角关闭按钮不存在')
            self.expected_conditions()
            return

        self.expected_conditions()

    def expected_conditions(self):
        self.assertTrue(self.ctrl_neutral1_v1_handle.click_plugin_back_homepage_element(), '返回到房间里面的箭头按钮不存在')
        self.assertTrue(self.ctrl_neutral1_v1_handle.click_room_list_back_element(), '返回到房间列表的箭头按钮不存在')
        self.assertTrue(self.ctrl_neutral1_v1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")

    def tearDown(self) -> None:
        '''用例结束'''
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

def get_suite():
    # 定义一个测试容器
    suite = unittest.TestSuite()
    suite.addTest(Ctrl_Neutral1_V1_Case('test_case1'))
    suite.addTest(Ctrl_Neutral1_V1_Case('test_case2'))
    suite.addTest(Ctrl_Neutral1_V1_Case('test_case3'))
    suite.addTest(Ctrl_Neutral1_V1_Case('test_case4'))
    # unittest.TextTestRunner().run(suite)
    # 定义个报告存放的路径，支持相对路径
    # filename = '../report/tesecase'+str(i)+'_report'+'.html'
    filename = '../report/HTMLReport.html'
    # filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'
    file_result = open(filename, 'wb')
    # 定义测试报告
    HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                  title='Aqara墙壁开关(单火线单键版)测试用例结果',
                                  description='测试报告详情:').run(suite)
    file_result.close()

if __name__ == '__main__':
    server = Server()
    server.execute_command_on_thread()
    get_suite()
    server.kill_server()

