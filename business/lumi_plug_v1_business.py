#coding=utf-8
from handle.lumi_plug_v1_handle import Plug_V1_Handle
class Plug_V1_Business:
    def __init__(self,i):
        self.plug_v1_handle = Plug_V1_Handle(i)

    '''
     插座电源
     '''
    def click_power(self):
        self.plug_v1_handle.click_power_element()

    '''
    今日用电
    '''
    def click_day_cost(self):
        self.plug_v1_handle.click_day_cost_element()


    '''
    当月电量
    '''
    def click_electricity_month(self):
        self.plug_v1_handle.click_electricity_month_element()


    '''
    当前功率
    '''
    def click_current_power(self):
        self.plug_v1_handle.click_current_power_element()


    '''
    开关
    '''
    def click_on_off(self):
        self.plug_v1_handle.click_on_off_element()

    '''
    定时
    '''
    def click_timing(self):
        self.plug_v1_handle.click_timing_element()

    '''
    倒计时
    '''
    def click_time_count_down(self):
        return self.plug_v1_handle.click_time_count_down_element()
