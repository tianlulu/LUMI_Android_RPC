#coding=utf8
from base.base_page import BasePage
class Ctrl_Neutral1_V1_Page(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        print('Aqara墙壁开关(单火线单键版):',self.driver)
        self.element = 'one_button_switch_element'

    '''
    房间Aqara墙壁开关(单火线单键版)
    '''
    def get_home_device_element(self):
        device_name = self.custom_name.get_ctrl_neutral_v1_device_name()
        # print('device_name:',device_name)
        if device_name != "":
            return self.get_custom_element(device_name, 5, 0.5)
        else:
            return self.my_local.get_element('home_ctrl_ln1_aq1', self.element)

    '''
    房间
    '''
    def get_device_room(self):
        room_name = self.custom_name.get_ctrl_neutral_v1_room_name()
        # print('room_name:',room_name)
        if room_name != "":
            return self.get_custom_element(room_name, 5, 0.5)
        else:
            return self.find_element('device_room', self.common_element)

    '''
    底部指示灯
    '''
    def get_light_bulb_view_element(self):
        return self.find_element('bottom_light', self.element)


    '''
    开启/关闭
    '''
    def get_on_off_element(self):
        return self.find_element('on_off', self.element)
