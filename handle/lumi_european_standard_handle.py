#coding=utf8
from page.lumi_european_standard_page import European_Standard_Page
from util.get_image_rgb import ImageRGBD
import time
from base.base_handle import BaseHandle



class European_Standard_Handle(BaseHandle):
    '''
    def __init__(self,i):
        self.european_standard_page = European_Standard_Page(i)
    '''
    def __init__(self):
        BaseHandle.__init__(self)
        self.european_standard_page = European_Standard_Page()

    '''
    首页滑动控件直到欧标插座出现并点击:设置最多滑动50次能够找到元素
    '''
    def click_home_european_standard_element(self):
        return self.get_home_device(self.european_standard_page)

    '''
    上滑到顶部 最多滑动50次直到找到这样元素为止
    '''
    def scroll_to_top(self):
        return self.to_top(self.european_standard_page)


    '''
    首页滑动控件直到欧标插座出现并点击:设置最多滑动50次能够找到元素
    首页--滚动--找到设备
    '''
    def get_european_standard_element(self):
        return self.get_home_device(self.european_standard_page)


    '''
    首页滑动控件直到欧标插座出现并点击:设置最多滑动50次能够找到元素
    首页--房间--具体房间--设备
    '''
    def get_room_european_standard_element(self):
        self.get_room_element()
        return self.get_room_device(self.european_standard_page)


    def get_room_element(self):
        element = self.european_standard_page.get_room_element()
        return self.element_operation(element)


    def click_universal_back_element(self):
        element = self.european_standard_page.get_universal_back_element()
        return self.element_operation(element)


    def click_offline_close(self):
        element = self.european_standard_page.get_offline_close()
        return self.element_operation(element)

    '''
    获取top开关按钮控件颜色
    '''
    def get_top_element_rgba(self):
        image_rgb = ImageRGBD()
        # 截屏操作
        file_path = self.european_standard_page.get_screen_shot_image()

        # 需要获取top_element RGB元素
        top_element = self.european_standard_page.get_top_group_view_element()

        # 获取该元素中心位置的RGB颜色
        return image_rgb.get_element_rgb(top_element,file_path)


    def click_offline_close_element(self):
        element = self.european_standard_page.get_offline_close()
        return self.element_operation(element)

    '''
    top_button
    '''
    def click_top_element(self):
        # 上滑动
        self.swipe_with('up')
        element=self.european_standard_page.get_top_group_view_element()
        return self.element_operation(element)

    '''
    定时
    '''
    def click_timing_element(self):
        element=self.european_standard_page.get_timing_element()
        return self.element_operation(element)



    '''
    开启/关闭
    '''
    def click_on_off_element(self):
        element=self.european_standard_page.get_on_off_element()
        return self.element_operation(element)

    '''
    今日用电
    '''
    def click_day_cost_element(self):
        element=self.european_standard_page.get_day_cost_element()
        return self.element_operation(element)

    '''
    当月电量
    '''
    def click_electricity_month_element(self):
        element=self.european_standard_page.get_electricity_month_element()
        return self.element_operation(element)


    '''
    当前功率
    '''
    def click_current_power_element(self):
        element=self.european_standard_page.get_current_power_element()
        return self.element_operation(element)



    '''
    开启/关闭电源按钮
    '''
    def click_on_off_light_element(self):
        self.sleep()
        element=self.european_standard_page.get_on_off_light_element()
        return self.element_operation(element)

    '''
    电器脱离
    '''
    def click_get_electrical_disconnect_element(self):
        self.sleep()
        element = self.european_standard_page.get_electrical_disconnect_element()
        return self.element_operation(element)

    '''
    三个点
    '''
    def click_more_element(self):
        element=self.european_standard_page.get_more_element()
        return self.element_operation(element)

    '''
    点击最大功率限制
    '''
    def click_max_power_limit_element(self):
        element= self.european_standard_page.get_max_power_limit_element()
        return self.element_operation(element)

    '''
    确认最大功率限制
    '''
    def click_confirm_power_limit(self):
        limit_element = self.click_max_power_limit_element()
        if limit_element != None:
            element = self.european_standard_page.get_max_power_limit_picker_view()
            print('picker_view', element)
            if element != None:
                self.swipe_maximum_power_limit(element)
                element = self.european_standard_page.confirm_maximum_power_limit()
                self.element_operation(element)
                return element
            else:
                print('找不到pickerView这个元素')
                return None
        else:
            return None


    '''
    断电记忆
    '''
    def click_power_off_memory_element(self):
        element=self.european_standard_page.get_failure_memory_element()
        return self.element_operation(element)

    '''
    更换坐标
    '''
    def click_change_element(self):
        element=self.european_standard_page.get_change_element()
        return self.element_operation(element)

    '''
    日志
    '''
    def click_log_element(self):
        element=self.european_standard_page.get_log_element()
        return self.element_operation(element)

    '''
    插件版本号
    '''
    def click_plugin_version(self):
        element=self.european_standard_page.get_plugin_version()
        return self.element_operation(element)

    '''
    设备名称
    '''
    def click_device_element(self):
        element=self.european_standard_page.get_device_element()
        return self.element_operation(element)

    '''
    确定修改设备名称
    '''
    def click_confirm_fix_device_name(self):
        element = self.european_standard_page.confirm_fix_device_name()
        return self.element_operation(element)

    '''
    取消修改设备名称
    '''
    def click_cancel_fix_device_name(self):
        element = self.european_standard_page.cancel_fix_device_name()
        return element.click()

    '''
    位置管理
    '''
    def click_location_management(self):
        element=self.european_standard_page.get_location_management()
        return self.element_operation(element)

    '''
    位置管理返回页面
    '''
    def click_position_cancel_back(self):
        return self.european_standard_page.get_position_cancel_back()

    '''
    智能场景
    '''
    def click_intelligent_scene(self):
        element=self.european_standard_page.get_intelligent_scene()
        return self.element_operation(element)

    '''
    更多设置
    '''
    def click_more_setting(self):
        element = self.european_standard_page.more_setting()
        return self.element_operation(element)


    '''
    指定控件内上滑（如最大功率设置的pickerView）
    '''
    def swipe_maximum_power_limit(self,element):
        self.european_standard_page.swipe_up_based_on_element(element)


    def element_operation(self, element):
        if element:
            print(element, '元素存在')
            element.click()
            return True
        else:
            print('元素不存在')
            return False

    '''
    判断设备是否离线
    '''
    def is_offline_element(self):
        element = self.european_standard_page.get_offline_element()
        if element:
            # print('设备离线')
            return True
        else:
            print('设备在线')
            return False

    '''
    获取toast元素
    '''
    def get_fail_toast(self, message):
        toast_element = self.european_standard_page.get_toast_element(message)
        if toast_element:
            # print('无网络状态')
            return True
        else:
            print('有网络状态')
            return False








