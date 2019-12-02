# coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import unittest
from on_button_switch.on_button_wall_switch_business import On_Button_Wall_Switch_Business
from on_button_switch.on_button_wall_switch_data import One_Button_Wall_Switch_Data
from on_button_switch.handle.lumi_ctrl_ln1_aq1_handle import Ctrl_Ln1_Aq1_Handle
from util.server import Server
import HTMLTestRunner
from common.constant_enum import TIME_TYPE
from common.constant_enum import TIME_CUSTOME_TYPE

'''
Aqara墙壁开关(零火线单键版)测试用例  PA
'''
class Ctrl_Ln1_Aq1_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('开始Ctrl_Ln1_Aq1_Case')
        cls.one_button_wall_switch_data = One_Button_Wall_Switch_Data()
        cls.ctrl_ln1_aq1_handle = Ctrl_Ln1_Aq1_Handle()
        cls.one_button_wall_switch_business = On_Button_Wall_Switch_Business(cls.ctrl_ln1_aq1_handle)

    def setUp(self) -> None:
        print('setUp')

    def test_case1(self):
        '''找出Aqara墙壁开关(零火线单键版)'''
        global room_exists
        room_exists = self.ctrl_ln1_aq1_handle.click_ctrl_ln1_aq1_room_element()
        self.assertTrue(room_exists,'滑动到底部仍然没有找到房间')

        global device_exists
        device_exists = self.ctrl_ln1_aq1_handle.click_ctrl_ln1_aq1_device_element()
        self.assertTrue(device_exists, '滑动到底部仍然没有找到设备或者点击设备无响应')

        global is_no_network
        is_no_network = self.ctrl_ln1_aq1_handle.get_fail_toast('请求失败，请检查网络')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')

        # 判断设备是否离线状态
        global is_offline
        is_offline = self.ctrl_ln1_aq1_handle.is_offline_element()
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')


    def test_case2(self):
        '''进入首页获取设备状态(get_device_prop_exp)'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_data.get_home_data_and_analysis(False)


    def test_case3(self):
        '''打开/关闭开关（toggle_ctrl_neutral)'''
        self.determine_current_status_of_the_device()
        gray_rgba = (216, 216, 216, 255)
        rgba = self.ctrl_ln1_aq1_handle.get_light_bulb_element_rgba()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_on_off_light_element(), '找不到开关按钮')
        self.one_button_wall_switch_data.set_toggle_plug_on_off(rgba == gray_rgba,False)


    def test_case4(self):
        '''是否请求当日电量接口'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_data.get_the_current_electricity_request_data(True)


    def test_case5(self):
        '''是否请求当月电量接口'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_data.get_the_current_electricity_request_data(False)


    def test_case6(self):
        '''点击今日用电:进入当日电量统计页面'''
        '''
        1、点击今日用电:请求当日用电请求接口,进入电量统计界面
        2、获取电量元素 
        3、判断元素上面的值
        '''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_current_day_electricity_element())
        self.one_button_wall_switch_business.get_the_correct_electricity_data(self.one_button_wall_switch_data, True)


    def test_case7(self):
        '''点击"月":统计当月用电'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_month_degree_element())
        self.one_button_wall_switch_business.get_the_correct_electricity_data(self.one_button_wall_switch_data,False)


    def test_case8(self):
        '''点击当月电量:进入当月电量统计页面'''
        '''
        1、点击今日用电:请求当日用电请求接口,进入电量统计界面
        2、获取电量元素 
        3、判断元素上面的值
        '''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_plugin_back_homepage_element(), '返回到插件首页的箭头按钮不存在')
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_current_month_electricity_element())
        self.one_button_wall_switch_business.get_the_correct_electricity_data(self.one_button_wall_switch_data,False)

    def test_case9(self):
        '''点击"日":统计当日电量'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_day_degree_element())
        self.one_button_wall_switch_business.get_the_correct_electricity_data(self.one_button_wall_switch_data,True)

    def test_case10(self):
        '''点击功率历史记录:进入当日功率历史记录页面'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_plugin_back_homepage_element(), '返回到插件首页的箭头按钮不存在')
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_current_power_element())
        self.one_button_wall_switch_business.get_the_correct_power_data(self.one_button_wall_switch_data, True)

    def test_case11(self):
        '''点击"周":统计本周功率'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_week_degree_element())
        self.one_button_wall_switch_business.get_the_correct_power_data(self.one_button_wall_switch_data,False)

    def test_case12(self):
        '''定时功能:时间段定时，执行一次,未设置关闭时间'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_plugin_back_homepage_element(), '返回到插件首页的箭头按钮不存在')
        self.one_button_wall_switch_business.time_period_no_shutdown_time_set()

    def test_case13(self):
        '''定时功能:时间段定时，执行一次'''
        self.determine_current_status_of_the_device()
        on_off_time_text = self.one_button_wall_switch_business.time_period_execute_once()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on_off,TIME_CUSTOME_TYPE.once,on_off_time_text[0],on_off_time_text[1])


    def test_case14(self):
        '''定时功能:时间段定时,每天'''
        self.determine_current_status_of_the_device()
        on_off_time_text = self.one_button_wall_switch_business.time_period_daily()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on_off,TIME_CUSTOME_TYPE.period_daily,on_off_time_text[0],on_off_time_text[1])


    def test_case15(self):
        '''定时功能:时间段定时,法定工作日'''
        self.determine_current_status_of_the_device()
        on_off_time_text = self.one_button_wall_switch_business.time_period_legal_working_day()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on_off,TIME_CUSTOME_TYPE.legal_working_day,on_off_time_text[0],on_off_time_text[1])


    def test_case16(self):
        '''定时功能:时间段定时,法定节假日'''
        self.determine_current_status_of_the_device()
        on_off_time_text = self.one_button_wall_switch_business.time_period_legal_holidays()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on_off,TIME_CUSTOME_TYPE.legal_holidays,on_off_time_text[0],on_off_time_text[1])



    def test_case17(self):
        '''定时功能:时间段定时，自定义'''
        self.determine_current_status_of_the_device()
        on_off_time_text = self.one_button_wall_switch_business.time_period_custom()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on_off,TIME_CUSTOME_TYPE.custom,on_off_time_text[0],on_off_time_text[1])


    def test_case18(self):
        '''定时功能:定时开启,执行一次'''
        self.determine_current_status_of_the_device()
        on_time_text = self.one_button_wall_switch_business.timed_on_execute_once()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on,TIME_CUSTOME_TYPE.once,start_time_str=on_time_text)


    def test_case19(self):
        '''定时功能:定时开启,每天'''
        self.determine_current_status_of_the_device()
        on_time_text = self.one_button_wall_switch_business.timed_on_execute_daily()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on, TIME_CUSTOME_TYPE.period_daily, start_time_str=on_time_text)


    def test_case20(self):
        '''定时功能:定时开启，法定工作日'''
        self.determine_current_status_of_the_device()
        on_time_text = self.one_button_wall_switch_business.timed_on_legal_working_day()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on, TIME_CUSTOME_TYPE.legal_working_day, start_time_str=on_time_text)


    def test_case21(self):
        '''定时功能:定时开启,法定节假日'''
        self.determine_current_status_of_the_device()
        on_time_text = self.one_button_wall_switch_business.timed_on_legal_holidays()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on, TIME_CUSTOME_TYPE.legal_holidays, start_time_str=on_time_text)


    def test_case22(self):
        '''定时功能:定时开启,自定义'''
        self.determine_current_status_of_the_device()
        on_time_text = self.one_button_wall_switch_business.timed_on_custom()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_on, TIME_CUSTOME_TYPE.custom, start_time_str=on_time_text)


    def test_case23(self):
        '''定时功能:定时关闭,执行一次'''
        self.determine_current_status_of_the_device()
        off_time_text = self.one_button_wall_switch_business.timed_off_execute_once()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_off, TIME_CUSTOME_TYPE.once, end_time_str=off_time_text)


    def test_case24(self):
        '''定时功能:定时关闭,每天'''
        self.determine_current_status_of_the_device()
        off_time_text = self.one_button_wall_switch_business.timed_off_execute_daily()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_off, TIME_CUSTOME_TYPE.period_daily, end_time_str=off_time_text)


    def test_case25(self):
        '''定时功能:定时关闭，法定工作日'''
        self.determine_current_status_of_the_device()
        off_time_text = self.one_button_wall_switch_business.timed_off_legal_working_day()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_off, TIME_CUSTOME_TYPE.legal_working_day, end_time_str=off_time_text)


    def test_case26(self):
        '''定时功能:定时关闭,法定节假日'''
        self.determine_current_status_of_the_device()
        off_time_text = self.one_button_wall_switch_business.timed_off_legal_holidays()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_off, TIME_CUSTOME_TYPE.legal_holidays, end_time_str=off_time_text)


    def test_case27(self):
        '''定时功能:定时关闭,自定义'''
        self.determine_current_status_of_the_device()
        off_time_text = self.one_button_wall_switch_business.timed_off_custom()
        self.one_button_wall_switch_data.checking_timing_set(TIME_TYPE.time_off, TIME_CUSTOME_TYPE.custom, end_time_str=off_time_text)


    def test_case28(self):
        '''转无线开关设置：获取转无线开关状态'''
        self.determine_current_status_of_the_device()
        assert self.ctrl_ln1_aq1_handle.click_title_bar_return_button_element() == True,'定时首页返回按钮不存在'
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_turn_wireless_switch_settings_element(), '转无线开关设置cell元素不存在')
        self.one_button_wall_switch_data.get_wireless_switch_status()


    def test_case29(self):
        '''转无线开关设置：打开/关闭转无线开关按钮'''
        self.determine_current_status_of_the_device()
        self.ctrl_ln1_aq1_handle.swipe_with('up')
        # 蓝色
        blue_rgba = (50, 186, 192, 255)
        rgba = self.ctrl_ln1_aq1_handle.get_switch_element_rgba()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_wireless_switch_function_switching_element(), '没有获取到转无线开关的按钮')
        print('rgba:',rgba)
        self.one_button_wall_switch_data.turn_wireless_switch_settings(rgba == blue_rgba)


    def test_case30(self):
        '''修改设备名称:取消修改设备名称'''
        self.determine_current_status_of_the_device()
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_plugin_back_homepage_element(), '返回到插件首页的箭头按钮不存在')
        self.one_button_wall_switch_business.cancel_modify_device_name()


    def test_case31(self):
        '''修改设备名称:0个字符'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_business.modify_device_name_0_characters()

    def test_case32(self):
        '''修改设备名称:21个字符'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_business.modify_device_name()
        self.one_button_wall_switch_data.device_rename()

    def test_case33(self):
        '''修改设备名称:>21个字符'''
        self.determine_current_status_of_the_device()
        self.one_button_wall_switch_business.modify_device_name_exceed_character_limit()

    def test_case34(self):
        '''返回首页：滑动到顶部'''
        if room_exists == False:
            print('房间不存在')
            self.assertTrue(self.ctrl_ln1_aq1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")
            return

        if device_exists == False:
            print('设备不存在')
            self.assertTrue(self.ctrl_ln1_aq1_handle.click_room_list_back_element(),'返回到房间列表的箭头按钮不存在')
            self.assertTrue(self.ctrl_ln1_aq1_handle.scroll_to_top(),'下滑到最后没有找到+按钮')
            return

        if is_no_network:
            print('无网络状态')
            self.expected_conditions()
            return

        if is_offline:
            print('设备离线状态')
            self.assertTrue(self.ctrl_ln1_aq1_handle.click_offline_close(),'离线框右上角关闭按钮不存在')
            self.expected_conditions()
            return

        self.expected_conditions()

    def expected_conditions(self):
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_plugin_back_homepage_element(), '返回到房间里面的箭头按钮不存在')
        self.assertTrue(self.ctrl_ln1_aq1_handle.click_room_list_back_element(), '返回到房间列表的箭头按钮不存在')
        self.assertTrue(self.ctrl_ln1_aq1_handle.scroll_to_top(), "下滑到最后没有找到+按钮")

    def determine_current_status_of_the_device(self):
        self.assertTrue(room_exists,'房间不存在')
        self.assertTrue(device_exists, '设备不存在')
        self.assertFalse(is_no_network, '无网络状态，请联网后重试')
        self.assertFalse(is_offline, '设备已离线，请重新连接设备')

    def tearDown(self) -> None:
        '''用例结束'''
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

def get_suite():
    # 定义一个测试容器
    suite = unittest.TestSuite()
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case1'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case2'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case3'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case4'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case5'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case6'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case7'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case8'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case9'))

    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case10'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case11'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case12'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case13'))

    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case14'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case15'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case16'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case17'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case18'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case19'))

    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case20'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case21'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case22'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case23'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case24'))


    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case25'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case26'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case27'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case28'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case29'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case30'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case31'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case32'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case33'))
    suite.addTest(Ctrl_Ln1_Aq1_Case('test_case34'))

    # unittest.TextTestRunner().run(suite)
    # 定义个报告存放的路径，支持相对路径
    # filename = '../report/tesecase'+str(i)+'_report'+'.html'
    # filename = '../report/HTMLReport.html'

    filename = '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC/report/HTMLReport.html'
    file_result = open(filename, 'wb')
    # 定义测试报告
    HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                  title='Aqara墙壁开关(零火线单键版)测试用例结果',
                                  description='测试报告详情:').run(suite)
    file_result.close()


if __name__ == '__main__':
    server = Server()
    server.execute_command_on_thread()
    get_suite()
    server.kill_server()



