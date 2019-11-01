#coding=utf8
from base.base_handle import BaseHandle
from page.lumi_switch_b1nacn02_page import Switch_B1nacn02_Page
from util.get_image_rgb import ImageRGBD
from selenium.common import exceptions as ex

class Switch_B1nacn02_Handle(BaseHandle):
    def __init__(self):
        BaseHandle.__init__(self)
        self.switch_b1nacn02_page = Switch_B1nacn02_Page()

    '''
    首页滑动控件直到房间出现(如:Sweet)
    首页--room--具体房间
    '''
    def click_room_element(self):
        self.get_room_element()
        return self.find_room(self.switch_b1nacn02_page)

    '''
    首页滑动控件直到 Aqara智能墙壁开关 D1（零火线单键版）出现
    首页--room--具体房间--设备
    '''
    def click_device_element(self):
        return self.find_device(self.switch_b1nacn02_page)

    '''
    找到房间：'room'
    '''
    def get_room_element(self):
        element = self.switch_b1nacn02_page.get_room_element()
        return self.element_operation(element)

    '''
    无网络状态toast
    '''
    def get_fail_toast(self, message):
        toast_element = self.switch_b1nacn02_page.get_toast_element(message)
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
        element = self.switch_b1nacn02_page.get_offline_element()
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
        return self.to_top(self.switch_b1nacn02_page)


    '''
    点击离线框右上角关闭按钮
    '''
    def click_offline_close(self):
        element = self.switch_b1nacn02_page.get_offline_close()
        return self.element_operation(element)


    '''
    插件首页返回按钮
    '''
    def click_plugin_back_homepage_element(self):
        element = self.switch_b1nacn02_page.get_plugin_back_homepage_element()
        return self.element_operation(element)


    '''
    通过返回按钮:房间页面返回房间列表页面
    '''
    def click_room_list_back_element(self):
        # element = self.ctrl_ln1_page.get_room_list_back_element()
        # return self.element_operation(element)
        try:
            self.element = self.switch_b1nacn02_page.get_room_list_back_element()
        except ex.StaleElementReferenceException:
            print('StaleElementReferenceExceptionStaleElementReferenceExceptionStaleElementReferenceException')
            self.element = self.switch_b1nacn02_page.get_room_list_back_element()
        return self.element_operation(self.element)


    '''
    获取顶部💡颜色
    蓝色：开状态
    灰色：关状态
    '''
    def get_light_bulb_element_rgba(self):
        image_rgb = ImageRGBD()
        # 截屏操作
        file_path = self.switch_b1nacn02_page.get_screen_shot_image()

        # 需要获取top_element RGB元素
        light_element = self.switch_b1nacn02_page.get_light_bulb_view_element()

        # 获取该元素中心位置的RGB颜色
        return image_rgb.get_element_rgb(light_element,file_path)


    '''
    开启/关闭电源按钮
    '''
    def click_on_off_light_element(self):
        element = self.switch_b1nacn02_page.get_on_off_element()
        return self.element_operation(element)


    def element_operation(self,element):
        if element:
            try:
                element.click()
            except ex.StaleElementReferenceException:
                print('Switch_B1nacn02_Handle--------------get_room_list_back_element')
                element = self.switch_b1nacn02_page.get_room_list_back_element()
                element.click()
            return True
        else:
            print('元素不存在')
            return False