#coding=utf8
from base.base_page import BasePage
from common.constant_enum import ELEMENT_INI_PATH
from common.constant_enum import ELEMENT_INI
class One_Button_Wall_Switch_Page(BasePage):
    def __init__(self):
        self.ini_element = ELEMENT_INI.one_button_wall_switch
        self.ini_element_file_path = ELEMENT_INI_PATH.control
        BasePage.__init__(self)

    '''
    Aqara墙壁开关(零火线单键版)--房间
    '''
    def get_ctrl_ln1_aq1_room_element(self):
        room_name = self.custom_name.get_ctrl_ln1_aq1_room_name()
        print('room_name:',room_name)
        if room_name != "":
            return self.get_custom_element(room_name, 5, 0.5)
        else:
            return self.find_element('device_room')


    '''
    房间Aqara墙壁开关(零火线单键版)--设备
    '''
    def get_ctrl_ln1_aq1_device_element(self):
        device_name = self.custom_name.get_ctrl_ln1_aq1_device_name()
        if device_name != "":
            return self.get_custom_element(device_name, 5, 0.5)
        else:
            return self.my_local.get_element('home_ctrl_ln1_aq1', self.ini_element, self.ini_element_file_path)

    '''
    底部指示灯
    '''
    def get_light_bulb_view_element(self):
        return self.find_element('bottom_light', self.ini_element,self.ini_element_file_path)


    '''
    开启/关闭
    '''
    def get_on_off_element(self):
        return self.find_element('on_off', self.ini_element,self.ini_element_file_path)


    '''
    首页-今日用电
    '''
    def get_current_day_electricity_element(self):
        return self.find_element('current_day_electricity', self.ini_element,self.ini_element_file_path)


    '''
    首页-当月用电
    '''
    def get_current_month_electricity_element(self):
        return self.find_element('current_month_electricity', self.ini_element,self.ini_element_file_path)


    '''首页-功率历史记录'''
    def get_current_power_element(self):
        return self.find_element('power_history',self.ini_element,self.ini_element_file_path)



    '''首页-功率显示'''
    def get_history_power_text_element(self):
        return self.find_element('power_history_test',self.ini_element,self.ini_element_file_path)


    '''
    插件首页的返回按钮
    '''
    def get_plugin_back_homepage_element(self):
        return self.find_element('plugin_back_homepage', self.ini_element,self.ini_element_file_path)

    '''
    电量显示
    '''
    def get_electricity_degree_element(self):
        return self.find_element('electricity_degree',self.ini_element,self.ini_element_file_path)


    '''
    功率历史-时间显示
    '''
    def get_power_time_element(self):
        return self.find_element('power_time', self.ini_element,self.ini_element_file_path)


    '''
    电量统计-日按钮
    '''
    def get_day_degree_element(self):
        return self.find_element('day_degree',self.ini_element,self.ini_element_file_path)

    '''
    电量统计-月按钮
    '''
    def get_month_degree_element(self):
        return self.find_element('month_degree', self.ini_element,self.ini_element_file_path)


    '''
    历史功率-周按钮
    '''
    def get_week_degree_element(self):
        return self.find_element('week_degree', self.ini_element,self.ini_element_file_path)


    '''
    设置-转无线开关设置
    '''
    def get_turn_wireless_switch_settings_element(self):
        return self.find_element('turn_wireless_switch_settings',self.ini_element,self.ini_element_file_path)

    '''
    转无线开关设置-转无线开关功能切换按钮
    '''
    def get_wireless_switch_function_switching_element(self):
        return self.find_element('wireless_switch_function_switching',self.ini_element,self.ini_element_file_path)







