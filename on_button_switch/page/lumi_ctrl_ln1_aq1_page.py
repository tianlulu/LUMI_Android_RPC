#coding=utf8
from on_button_switch.one_button_wall_switch_page import One_Button_Wall_Switch_Page
class Ctrl_Ln1_Aq1_Page(One_Button_Wall_Switch_Page):
    def __init__(self):
        One_Button_Wall_Switch_Page.__init__(self)

    '''
    Aqara墙壁开关(零火线单键版)--房间
    '''
    def get_ctrl_ln1_aq1_room_element(self):
        room_name = self.custom_name.get_ctrl_ln1_aq1_room_name()
        if room_name != "":
            return self.get_custom_element(room_name, 1, 0.5)
        else:
            return self.my_local.get_element('device_room')

    '''
    房间Aqara墙壁开关(零火线单键版)--设备
    '''
    def get_ctrl_ln1_aq1_device_element(self):
        device_name = self.custom_name.get_ctrl_ln1_aq1_device_name()
        if device_name != "":
            return self.get_custom_element(device_name, 1, 0.5)
        else:
            return self.my_local.get_element('home_ctrl_ln1_aq1', self.ini_element, self.ini_element_file_path)

    # '''
    # def get_home_tag_element(self):
    #     return self.my_local.get_element('electricity_degree',self.ini_element,self.ini_element_file_path)





