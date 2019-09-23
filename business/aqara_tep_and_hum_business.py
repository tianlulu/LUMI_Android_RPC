#coding=utf-8
from handle.lumi_plug_v1_handle import Plug_V1_Handle
from handle.aqara_tep_and_hum_handle import Temp_And_Humn_Handle
class Temp_And_Humn_Business:
    def __init__(self,i):
        self.temp_humidity_handle = Temp_And_Humn_Handle(i)

    '''
    top
    '''
    def click_top(self):
        self.temp_humidity_handle.click_top_element()


    '''
    温度
    '''
    def click_temp(self):
        # self.temp_humn_handle.click_temp_element()
        self.temp_humidity_handle.get_linearLayoout_elements()[0].click()


    '''
    湿度
    '''
    def click_humidity(self):
        # self.temp_humn_handle.click_humidity_element()
        self.temp_humidity_handle.get_linearLayoout_elements()[1].click()


    '''
    气压
    '''
    def click_pressure(self):
        # self.temp_humn_handle.click_pressure_element()
        self.temp_humidity_handle.get_linearLayoout_elements()[2].click()




