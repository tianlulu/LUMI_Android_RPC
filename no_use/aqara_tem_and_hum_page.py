#coding=utf8
from util.get_by_local import GetByLocal
from base.base_driver import DriverUtil

'''
Aqara温湿度上面所有元素元素
'''
class Temp_And_Humn_Page:
    def __init__(self,i):
        # base_driver = BaseDriver()
        # self.driver = base_driver.get_android_driver(i)
        # self.my_local = GetByLocal(self.driver)
        self.element = 'aqara_tep_and_hum_element'

    '''
    top_view
    '''
    def get_top_element(self):
        return self.my_local.get_element('top_view',self.element)

    '''
    温度
    '''
    def get_temp_element(self):
        return self.my_local.get_element('temperature_view',self.element)

    '''
    湿度
    '''
    def get_humidity_element(self):
        return self.my_local.get_element('humidity_view',self.element)

    '''
    气压
    '''
    def get_pressure_element(self):
        return self.my_local.get_element('pressure_view',self.element)



    def get_linearLayoout_elements(self):
        elements = self.my_local.get_elements('linearLayout_view',self.element)
        for subElement in elements:
            if subElement == len(elements)-1:
                print('最后一个元素,包含有子元素',subElement,len(subElement))
                return subElement
        else:
            return None










