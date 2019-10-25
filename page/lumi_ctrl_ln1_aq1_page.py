#coding=utf8
from base.base_page import BasePage
class Ctrl_Ln1_Aq1_Page(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        print('Aqara墙壁开关(零火线单键版):',self.driver)
        self.element = 'ctrl_ln1_aq1_element'

    '''
    房间Aqara墙壁开关(零火线单键版)
    '''
    def get_home_device_element(self):
        device_name = self.custom_name.get_ctrl_ln1_aq1_device_name()
        # print('device_name:',device_name)
        if device_name != "":
            return self.get_custom_element(device_name, 5, 0.5)
        else:
            return self.my_local.get_element('home_ctrl_ln1_aq1', self.element)

    '''
    房间
    '''
    def get_device_room(self):
        room_name = self.custom_name.get_ctrl_ln1_aq1_room_name()
        # print('room_name:',room_name)
        if room_name != "":
            return self.get_custom_element(room_name, 5, 0.5)
        else:
            return self.find_element('device_room', self.common_element)

    '''
    灯泡
    '''
    def get_light_bulb_view_element(self):
        return self.find_element('light_bulb', self.element)


    '''
    开启/关闭
    '''
    def get_on_off_element(self):
        return self.find_element('on_off', self.element)

    '''
    插件首页返回按钮
    '''
    def get_use_back_element(self):
        return self.find_element('use_back', self.element)