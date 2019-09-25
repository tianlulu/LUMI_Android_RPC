#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import HTMLTestRunner
import unittest
from util.server import Server
from util.write_user_command import WriteUserCommand
from util.operation_json import OperationJson
from handle.lumi_european_standard_handle import European_Standard_Handle
from dos.dos_cmd import DosCmd
from base.base_driver import DriverUtil

'''
欧标插座测试用例--demo
'''
class European_Standard_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始European_Standard_Case')
        global operation_json
        operation_json = OperationJson()
        cls.european_standard_handle = European_Standard_Handle()

    def setUp(self):
        '''用例开始'''
        print('setUp')

    def test_case1(self):
        '''找出欧标插座设备'''
        global device_exists
        device_exists = self.european_standard_handle.get_room_european_standard_element()
        self.assertTrue(device_exists,'滑动到底部仍然没有找到设备')

    def test_case2(self):
        '''进入首页(get_prop_plug)'''
        self.assertTrue(device_exists,'该设备不在房间内')

        global is_no_network
        is_no_network = self.european_standard_handle.get_fail_toast('加载失败')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')

        global is_offline
        is_offline = self.european_standard_handle.is_offline_element()
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')

        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'get_prop_plug')
        param_values = data['params']
        self.assertTrue(param_values[0] == 'channel_0','预期参数：channel_0 实际参数：' + param_values[0])
        self.assertTrue(param_values[1] == 'load_power','预期参数：load_power 实际参数：' + param_values[1])
        for value in param_values:
            print('params中带有' + value + '参数')

    def test_case3(self):
        '''top开关(toggle_plug)'''
        self.assertTrue(device_exists, '该设备不在房间内')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        gray_rgba = (67, 74, 81, 255)
        rgba = self.european_standard_handle.get_top_element_rgba()
        self.assertTrue(self.european_standard_handle.click_top_element(), '找不到top顶部按钮')
        if rgba == gray_rgba:
            self.set_toggle_plug_on()
        else:
            self.set_toggle_plug_off()


    def test_case4(self):
        '''开启/关闭(toggle_plug)'''
        self.assertTrue(device_exists, '该设备不在房间内')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        gray_rgba = (67, 74, 81, 255)
        rgba = self.european_standard_handle.get_top_element_rgba()
        self.assertTrue(self.european_standard_handle.click_on_off_light_element(), '找不到开启/关闭按钮')
        if rgba == gray_rgba:
            self.set_toggle_plug_on()
        else:
            self.set_toggle_plug_off()


    def set_toggle_plug_on(self):
        '''打开插座'''
        print('打开插座')
        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        self.assertEqual(method,'toggle_plug')
        param_values = data['params']
        print('method:' + method)
        self.assertTrue('channel_0' == param_values[0],'预期参数：channel_0 实际参数：' + param_values[0])
        self.assertTrue('on' == param_values[1],'预期参数：on 实际参数：' + param_values[1])
        for value in param_values:
            print('params中带有' + value + '参数')


    def set_toggle_plug_off(self):
        '''关闭插座'''
        print('关闭插座')
        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'toggle_plug')
        param_values = data['params']
        self.assertTrue('channel_0' == param_values[0],'预期参数：channel_0 实际参数：' + param_values[0])
        self.assertTrue('off' == param_values[1],'预期参数：off 实际参数：' + param_values[1])
        for value in param_values:
            print('params中带有' + value + '参数')


    def test_case5(self):
        ''''更多功能(get_device_prop)'''
        self.assertTrue(device_exists, '该设备不在房间内')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        self.assertTrue(self.european_standard_handle.click_more_element(), '找不到更多三个点')
        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'get_device_prop')
        param_values = data['params']
        self.assertTrue('en_night_tip_light' == param_values[1],'预期参数：en_night_tip_light 实际参数：' + param_values[1])
        self.assertTrue('poweroff_memory' == param_values[2],'预期参数：poweroff_memory 实际参数：' + param_values[2])
        self.assertTrue('max_power' == param_values[3],'预期参数：max_power 实际参数：' + param_values[3])
        for value in param_values:
            print('params中带有' + value + '参数')


    def test_case6(self):
        ''''确认最大功率设置(set_device_prop)'''
        self.assertTrue(device_exists, '该设备不在房间内')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        self.assertTrue(self.european_standard_handle.click_confirm_power_limit(), '找不到设置最大功率到元素pickView')
        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'set_device_prop')
        param_values = data['params']
        key_sid = list(param_values.keys())[0]
        key_max_powers = list(param_values.keys())[1]
        self.assertTrue('sid' == key_sid,'预期参数：sid 实际参数：' + key_sid)
        self.assertTrue('max_power' == key_max_powers,'预期参数：max_power 实际参数：' + key_max_powers)
        for value in param_values.keys():
            print('params中带有' + value + '参数')


    def test_case7(self):
        ''''断电记忆(set_device_prop)'''
        self.assertTrue(device_exists, '该设备不在房间内')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        self.assertTrue(self.european_standard_handle.click_power_off_memory_element(), '找不到断电记忆元素')
        data = operation_json.read_data()
        print('请求参数:', data)
        method = data['method']
        print('method:' + method)
        self.assertEqual(method,'set_device_prop')
        param_values = data['params']
        key_sid = list(param_values.keys())[0]
        key_memory = list(param_values.keys())[1]
        self.assertTrue('sid' == key_sid,'预期参数：sid 实际参数：' + key_sid)
        self.assertTrue('poweroff_memory' == key_memory,'预期参数：poweroff_memory 实际参数：' + key_memory)
        for value in param_values.keys():
            print('params中带有' + value + '参数')


    def test_case8(self):
        '''返回首页吧：滑动到顶部'''
        if device_exists == False:
            print('设备不在房间内')
            # 返回到房间列表
            self.assertTrue(self.european_standard_handle.click_universal_back_element(), '返回到房间列表的箭头按钮不存在')
            # 滑动直到顶部
            self.assertTrue(self.european_standard_handle.scroll_to_top(), "下滑到最后没有找到+按钮")
            return

        if is_no_network:
            self.expected_conditions()
            return

        if is_offline:
            self.assertTrue(self.european_standard_handle.click_offline_close(), '离线框右上角关闭按钮不存在')
            self.expected_conditions()
            return

        # 返回到插件首页
        self.assertTrue(self.european_standard_handle.click_universal_back_element(), '返回到插件首页的箭头按钮不存在')
        self.expected_conditions()


    def expected_conditions(self):
        # 返回到主界面
        self.assertTrue(self.european_standard_handle.click_universal_back_element(), '返回到房间里面的箭头按钮不存在')
        # 返回到房间列表
        self.assertTrue(self.european_standard_handle.click_universal_back_element(), '返回到房间列表的箭头按钮不存在')
        # 滑动直到顶部
        self.assertTrue(self.european_standard_handle.scroll_to_top(), "下滑到最后没有找到+按钮")


    def tearDown(self):
        '''用例结束'''
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        # kill_server()
        # european_standard_handle.quite_driver()

# appium_init初始化
def appium_init():
    server = Server()
    server.execute_command_on_thread()

def kill_server():
    server = Server()
    server.kill_server()

# 通过yaml中的个数获取运行的进程个数()
def get_count():
    write_file =WriteUserCommand()
    return write_file.get_yaml_file_lines()

def execute_addons():
    dos = DosCmd()
    dos.excute_addons()

def get_suite():
    # 定义一个测试容器
    suite = unittest.TestSuite()
    suite.addTest(European_Standard_Case('test_case1'))
    suite.addTest(European_Standard_Case('test_case2'))
    suite.addTest(European_Standard_Case('test_case3'))
    suite.addTest(European_Standard_Case('test_case4'))
    suite.addTest(European_Standard_Case('test_case5'))
    suite.addTest(European_Standard_Case('test_case6'))
    suite.addTest(European_Standard_Case('test_case7'))
    suite.addTest(European_Standard_Case('test_case8'))
    # unittest.TextTestRunner().run(suite)
    # 定义个报告存放的路径，支持相对路径
    # filename = '../report/tesecase'+str(i)+'_report'+'.html'
    filename = '../report/HTMLReport.html'
    # filename = '/Users/lumi/Documents/jenkins/workspace/miot_android_rpc/report//HTMLReport.html'
    file_result = open(filename, 'wb')
    # 定义测试报告
    HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                  title='欧标插座测试用例结果',
                                  description='测试报告详情:').run(suite)
    file_result.close()

if __name__ == '__main__':
    server = Server()
    server.execute_command_on_thread()
    get_suite()
    server.kill_server()























