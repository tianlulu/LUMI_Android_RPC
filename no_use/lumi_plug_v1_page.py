#coding=utf8
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver

'''
米家智能插座上面所有元素元素
'''

class Plugv_V1_Page:
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.get_android_driver(i)
        self.my_local = GetByLocal(self.driver)
        print('my_local_pppppp:',self.my_local)
        self.element = 'plug_v1_element'

    '''
    插座电源
    '''
    def get_power_element(self):
        return self.my_local.get_element('power',self.element)


    '''
    今日用电
    '''
    def get_day_cost_element(self):
        return self.my_local.get_element('day_cost',self.element)


    '''
    当月电量
    '''
    def get_electricity_month_element(self):
        return self.my_local.get_element('month_cost',self.element)


    '''
    当前功率
    '''
    def get_current_power_element(self):
        return self.my_local.get_element('current_power_cost',self.element)


    '''
    开关
    '''
    def get_on_off_element(self):
        return self.my_local.get_element('on_off_button',self.element)

    '''
    定时
    '''
    def get_timing_element(self):
        return self.my_local.get_element('timing',self.element)


    '''
    倒计时
    '''
    def get_time_count_down_element(self):
        return self.my_local.get_element('time_count_down',self.element)






