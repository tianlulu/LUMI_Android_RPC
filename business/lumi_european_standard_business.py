#coding=utf-8
from handle.lumi_european_standard_handle import European_Standard_Handle
import time
class European_Standard_Business:
    def __init__(self,i):
        self.european_standard_handle= European_Standard_Handle(i)

    def operation_main_page(self):
        '''
        向上滑动页面
        :return:
        '''
        # self.european_standard_handle.swipe_page_up()

        # top_on_off
        self.european_standard_handle.click_on_off_light_element()
        time.sleep(2)
        # 电器脱离
        self.european_standard_handle.click_get_electrical_disconnect_element()
        time.sleep(2)
        # 今日用电
        self.european_standard_handle.click_day_cost_element()
        time.sleep(2)
        # 今日用电 / 当月用电 / 当前功率返回按钮
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)
        # 当月电量
        self.european_standard_handle.click_electricity_month_element()
        time.sleep(2)
        # 今日用电 / 当月用电 / 当前功率返回按钮
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)
        # 当前功率
        # self.european_standard_handle.click_current_power_element()
        # time.sleep(2)
        # 今日用电 / 当月用电 / 当前功率返回按钮
        # self.european_standard_handle.click_use_back_element()
        # time.sleep(2)
        self.european_standard_handle.click_on_off_element()
        time.sleep(2)
        self.european_standard_handle.click_timing_element()
        time.sleep(2)
        # 今日用电 / 当月用电 / 当前功率返回按钮
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)


    def operation_more_page(self):
        # 三个点
        self.european_standard_handle.click_more_element()
        time.sleep(2)

        # 最大功率限制
        self.european_standard_handle.click_max_power_limit_element()
        time.sleep(2)
        # 取消设置功率限制
        self.european_standard_handle.click_cancel_power_limit()
        time.sleep(2)
        # self.european_standard_handle.click_use_back_element()
        # time.sleep(2)
        # 断电记忆
        self.european_standard_handle.click_power_off_memory_element()
        time.sleep(2)
        # 更换图标
        self.european_standard_handle.click_change_element()
        time.sleep(2)
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)
        # 获取日志
        self.european_standard_handle.click_log_element()
        time.sleep(2)
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)
        # 插件版本号
        self.european_standard_handle.click_plugin_version()
        time.sleep(2)
        # 设备名称
        self.european_standard_handle.click_device_element()
        time.sleep(2)
        # 取消修改设备名称
        self.european_standard_handle.click_cancel_fix_device_name()
        time.sleep(2)
        # 位置管理
        self.european_standard_handle.click_location_management()
        time.sleep(2)
        self.european_standard_handle.click_position_cancel_back()
        time.sleep(2)
        # 智能场景
        self.european_standard_handle.click_intelligent_scene()
        time.sleep(2)
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)
        # 更多设置
        self.european_standard_handle.click_more_setting()
        time.sleep(2)
        self.european_standard_handle.click_use_back_element()
        time.sleep(2)





