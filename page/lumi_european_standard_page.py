#coding=utf8
from util.get_by_local import GetByLocal
from util.swip_operation import Swip_Common
from util.get_image_rgb import ImageRGBD
from base.base_page import BasePage

'''
Aqara温湿度上面所有元素元素
'''
class European_Standard_Page(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        print('欧标插座:', self.driver)
        self.element = 'european_standard_element'


    '''
    首页欧标插座
    '''
    def get_home_device_element(self):
        device_name = self.custom_name.get_european_standard_device_name()
        if device_name != "":
            print('device_name不为空')
            return self.get_custom_element(device_name, 10, 0.5)
        else:
            print('device_name为空')
            return self.my_local.get_element('home_european_standard', self.element)

    '''
    房间
    '''
    def get_device_room(self):
        room_name = self.custom_name.get_european_standard_room_name()
        if room_name != "":
            print('room_name不为空')
            return self.get_custom_element(room_name, 10, 0.5)
        else:
            print('room_name为空')
            return self.find_element('device_room', self.common_element)

    '''
    top_view
    '''
    def get_top_group_view_element(self):
        return self.find_element('on_off_light', self.element)


    '''
    定时
    '''
    def get_timing_element(self):
        return self.find_element('timing', self.element)

    '''
    开启/关闭
    '''
    def get_on_off_element(self):
        return self.find_element('on_off', self.element)

    '''
    今日用电
    '''
    def get_day_cost_element(self):
        return self.find_element('day_cost', self.element)


    '''
    当月电量
    '''
    def get_electricity_month_element(self):
        return self.find_element('month_cost', self.element)


    '''
    当前功率
    '''
    def get_current_power_element(self):
        return self.find_element('current_power_cost', self.element)


    '''
    检查电器是否脱离
    '''
    def get_electrical_disconnect_element(self):
        return self.find_element('electrical_disconnect', self.element)


    '''
    开启/关闭电源按钮
    '''
    def get_on_off_light_element(self):
        return self.find_element('on_off_light', self.element)


    '''
    三个点
    '''
    def get_more_element(self):
        return self.find_element('more',self.element)


    '''
    最大功率限制
    '''
    def get_max_power_limit_element(self):
        return self.find_element('maximum_power_limit', self.element)


    '''
    确认最大功率限制
    '''
    def confirm_maximum_power_limit(self):
        return self.find_element('maximum_power_limit_confirm', self.element)


    '滑动最大功率控件'
    def get_max_power_limit_picker_view(self):
        return self.find_element('maximum_power_picker_view', self.element)


    '''
    取消最大功率限制
    '''
    def cancel_maximum_power_limit(self):
        return self.find_element('maximum_power_limit_cancel', self.element)


    '''
    断电记忆
    '''
    def get_failure_memory_element(self):
        return self.find_element('power_failure_memory', self.element)


    '''
    更换坐标
    '''
    def get_change_element(self):
        return self.find_element('change_coordinates', self.element)


    '''
    日志
    '''
    def get_log_element(self):
        return self.find_element('log', self.element)


    '''
    插件版本号
    '''
    def get_plugin_version(self):
        return self.find_element('plugin_version_number', self.element)


    '''
    确定修改设备名称
    '''
    def confirm_fix_device_name(self):
        return self.find_element('confirm_fix_decvice_name', self.element)


    '''
    取消修改设备名称
    '''
    def cancel_fix_device_name(self):
        return self.find_element('cancel_fix_device_name', self.element)


    '''
    位置管理
    '''
    def get_location_management(self):
        return self.find_element('location_management', self.element)


    '''
    位置管理返回页面
    '''
    def get_position_cancel_back(self):
        return self.find_element('cancel_position_back', self.element)


    '''
    智能场景
    '''
    def get_intelligent_scene(self):
        return self.find_element('intelligent_scene', self.element)


    '''
    更多设置
    '''
    def more_setting(self):
        return self.find_element('more_setting', self.element)


    '''
    截屏
    '''
    def get_screen_shot_image(self):
        imageRGB = ImageRGBD()
        file_path = imageRGB.get_screenshot_path()
        self.driver.get_screenshot_as_file(file_path)
        return file_path


    '''
    控件内向上滑动页面
    '''
    def swipe_up_based_on_element(self,element):
        swipe_operation = Swip_Common(self.driver,element)
        swipe_operation.swipe_element_up()













