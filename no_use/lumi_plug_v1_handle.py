#coding=utf8
from page.lumi_plug_v1_page import Plugv_V1_Page

class Plug_V1_Handle:
    def __init__(self,i):
        self.plug_v1_page = Plugv_V1_Page(i)

    '''
    插座电源
    '''
    def click_power_element(self):
        self.plug_v1_page.get_power_element().click()


    '''
    今日用电
    '''
    def click_day_cost_element(self):
        self.plug_v1_page.get_day_cost_element().click()


    '''
    当月电量
    '''
    def click_electricity_month_element(self):
        self.plug_v1_page.get_electricity_month_element().click()

    '''
    当前功率
    '''
    def click_current_power_element(self):
        self.plug_v1_page.get_current_power_element()


    '''
    开关
    '''
    def click_on_off_element(self):
        self.plug_v1_page.get_on_off_element().click()


    '''
    定时
    '''
    def click_timing_element(self):
        self.plug_v1_page.get_timing_element().click()

    '''
    倒计时
    '''
    def click_time_count_down_element(self):
        return self.plug_v1_page.get_time_count_down_element()
