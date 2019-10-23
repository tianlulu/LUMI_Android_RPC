#coding=utf8
from page.lumi_sensor_ht_v1_page import Sensor_Ht_V1_Page
from util.swip_operation import Swip_Common
import time
from base.base_handle import BaseHandle

class Sensor_Ht_V1_Handle(BaseHandle):
    def __init__(self):
        BaseHandle.__init__(self)
        self.sensor_ht_v1_page = Sensor_Ht_V1_Page()

    '''
    首页滑动控件直到欧标插座出现并点击:设置最多滑动50次能够找到元素
    首页--房间--具体房间--设备
    '''
    def get_room_sensor_ht_v1_element(self):
        self.get_room_element()
        return self.get_room_device(self.sensor_ht_v1_page)


    '''
    通用返回按钮
    '''
    def click_universal_back_element(self):
        element = self.sensor_ht_v1_page.get_universal_back_element()
        return self.element_operation(element)

    '''
    无网络状态toast
    '''
    def get_fail_toast(self, message):
        toast_element = self.sensor_ht_v1_page.get_toast_element(message)
        if toast_element:
            # print('无网络状态')
            return True
        else:
            print('有网络状态')
            return False

    '''
    判断设备是否离线
    '''
    def is_offline_element(self):
        element = self.sensor_ht_v1_page.get_offline_element()
        if element:
            print('设备离线')
            return True
        else:
            print('设备在线')
            return False


    '''
    上滑到顶部找到'+'按钮
    '''
    def scroll_to_top(self):
        return self.to_top(self.sensor_ht_v1_page)


    '''
    首页滑动控件直到米家温湿度
    首页--滚动--找到设备
    '''
    def get_sensor_ht_v1_element(self):
       return self.get_home_device(self.sensor_ht_v1_page)


    def get_room_element(self):
        element = self.sensor_ht_v1_page.get_room_element()
        return self.element_operation(element)

    '''
    温度
    '''
    def click_temperature_element(self):
        element=self.sensor_ht_v1_page.get_temperature_element()
        return self.element_operation(element)

    '''
    湿度
    '''
    def click_humidity_element(self):
        element=self.sensor_ht_v1_page.get_humidity_element()
        return self.element_operation(element)


    def get_custom_element(self,message):
        custom_element = self.sensor_ht_v1_page.get_custom_element(message,5, 0.01)
        if custom_element:
            print('找到了自定义元素',message)


    def click_use_back_element(self):
        element = self.sensor_ht_v1_page.get_use_back_element()
        return self.element_operation(element)



    def click_offline_close(self):
        element = self.sensor_ht_v1_page.get_offline_close()
        return self.element_operation(element)


    def element_operation(self, element):
        if element:
            # print(element, '元素存在')
            element.click()
            return True
        else:
            print('元素不存在')
            return False


