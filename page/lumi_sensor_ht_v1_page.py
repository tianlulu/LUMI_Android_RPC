#coding=utf8
from base.base_page import BasePage
'''
米家温湿度所有元素元素
'''
class Sensor_Ht_V1_Page(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        print('米家温湿度:', self.driver)
        self.element = 'sensor_h1_v1_element'

    '''
    房间米家温湿度按钮
    '''
    def get_home_device_element(self):
        device_name = self.custom_name.get_sensor_ht_v1_device_name()
        # print('device_name:',device_name)
        if device_name != "":
            return self.get_custom_element(device_name, 5, 0.5)
        else:
            return self.my_local.get_element('home_temperature_and_humidity', self.element)

    '''
    房间
    '''
    def get_device_room(self):
        room_name = self.custom_name.get_sensor_ht_v1_room_name()
        # print('room_name:',room_name)
        if room_name != "":
            return self.get_custom_element(room_name, 5, 0.5)
        else:
            return self.find_element('device_room', self.common_element)

    '''
    温度
    '''
    def get_temperature_element(self):
        return self.my_local.get_element('temperature', self.element)


    '''
    湿度
    '''
    def get_humidity_element(self):
        return self.find_element('humidity', self.element)











