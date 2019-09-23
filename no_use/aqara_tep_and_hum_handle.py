#coding=utf8
from page.aqara_tem_and_hum_page import Temp_And_Humn_Page


class Temp_And_Humn_Handle:
    def __init__(self,i):
        self.temp_hum_page = Temp_And_Humn_Page(i)

    '''
    top
    '''
    def click_top_element(self):
        self.temp_hum_page.get_top_element().click()


    '''
    温度
    '''
    def click_temp_element(self):
        self.temp_hum_page.get_temp_element().click()


    '''
    湿度
    '''
    def click_humidity_element(self):
        self.temp_hum_page.get_humidity_element().click()

    '''
    气压  
    '''
    def click_pressure_element(self):
        self.temp_hum_page.get_pressure_element().click()


    def get_linearLayoout_elements(self):
        return self.temp_hum_page.get_linearLayoout_elements()
