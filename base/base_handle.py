#coding=utf8
from util.swip_operation import Swip_Common
from base.base_driver import DriverUtil
from selenium.common import exceptions as ex
from util.get_by_local import GetByLocal
from util.get_image_rgb import ImageRGBD
from base.base_page import BasePage

class BaseHandle:
    def __init__(self,page_model):
        self.driver = DriverUtil.get_driver()
        self.my_local = GetByLocal(self.driver)
        self.swipe_common = Swip_Common(self.driver)
        self.page_model = page_model
        # 判断是否已经找到房间或设备
        self.is_flag = False


    '''
    处理首页弹窗
    '''
    def handling_the_home_popup(self):
        '''
        1、发现附近设备弹窗--关闭
        2、发现共享设备弹窗--关闭
        3、发现门锁报警弹窗我知道了--点击
        '''
        if self.page_model.get_discovery_device_alert_element() != None:
            print('发现附近设备弹窗')
            self.click_cancel_button_element()

        if self.page_model.get_home_share_alert_element() != None:
            print('发现共享设备弹窗')
            self.click_cancel_button_element()

        i_know_tips = self.get_home_i_know_alert_element()
        if i_know_tips != None:
            print('发现门锁报警弹窗我知道了')
            i_know_tips.click()

    '''
    找到房间：'room'
    '''
    def get_title_bar_room_element(self):
        # self.handling_the_home_popup()
        element = self.page_model.get_room_element()
        if element == None:
            self.handling_the_home_popup()
            element = self.page_model.get_room_element()
            return self.element_operation(element)
        else:
            self.handling_the_home_popup()
            return self.element_operation(element)

    '''
    按照方向滑动页面
    '''
    def swipe_with(self,direction):
        if direction == 'up':
            self.swipe_common.swipe_up()
        elif direction == 'down':
            self.swipe_common.swipe_down()


    '''
    控件内向上滑动页面
    '''
    def swipe_based_on_element(self, element, start_point, end_point):
        swipe_operation = Swip_Common(self.driver)
        swipe_operation.swipe_in_element(element, start_point, end_point)

    '''
    判断设备是否离线
    '''
    def is_offline_element(self):
        element = self.page_model.get_offline_element()
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
        i = 0
        count = 20
        while i < count:
            element = self.page_model.get_add_device_element()
            if element:
                print('向下滑动了' + str(i) + '次到达顶部')
                self.is_flag = True
                break
            else:
                self.swipe_with('down')
                i = i + 1
                if(i == count):
                    print('滑动了'+str(i)+'次仍然没有找到+按钮')
                    self.is_flag = False
                    break
        return self.is_flag


    '''
    点击离线框右上角关闭按钮
    '''
    def click_offline_close(self):
        element = self.page_model.get_offline_close()
        return self.element_operation(element)

    '''
    返回到插件首页按钮
    '''
    def click_plugin_back_homepage_element(self):
        element = self.page_model.get_plugin_back_homepage_element()
        return self.element_operation(element)


    '''
    通过返回按钮:房间页面返回房间列表页面
    '''
    def click_room_list_back_element(self):
        try:
            self.element = self.page_model.get_room_list_back_element()
        except ex.StaleElementReferenceException:
            print('StaleElementReferenceExceptionStaleElementReferenceExceptionStaleElementReferenceException')
            self.element = self.page_model.get_room_list_back_element()
        return self.element_operation(self.element)


    '''
    获取toast元素:如加载失败
    '''
    def get_fail_toast(self, message):
        toast_element = self.page_model.get_toast_element(message)
        if toast_element:
            # print('无网络状态')
            return True
        else:
            print('有网络状态')
            return False

    '''
    三个点
    '''
    def click_more_element(self):
        element = self.page_model.get_more_element()
        return self.element_operation(element)


    '''设置-设备名称'''
    def click_device_name_settings_element(self):
        element = self.page_model.get_device_name_settings_element()
        return self.element_operation(element)


    '''修改设备名称-删除按钮'''
    def click_input_view_clear_element(self):
        element = self.page_model.get_input_view_clear_element()
        return self.element_operation(element)


    '''修改设备名称-编辑框'''
    def click_edit_device_name_input_view(self):
        element = self.page_model.get_input_view_edit_element()
        return self.get_element(element)

    '''确认'''
    def click_confirm_button_element(self):
        element = self.page_model.get_confirm_button_element()
        return self.element_operation(element)


    '''取消确认'''
    def click_cancel_button_element(self):
        element = self.page_model.get_cancel_button_element()
        return self.element_operation(element)


    '''设置页-设备名称-右边显示设备的名称'''
    def show_right_detail_device_name_element(self):
        element = self.page_model.get_right_detail_device_name_element()
        return self.get_element(element)


    '''设置-设备名称-超出最大字符限制'''
    def show_exceeded_the_maximum_character_limit_alert(self):
        element = self.page_model.get_exceeded_the_maximum_character_limit_alert()
        return self.get_element(element)


    '''设置-定时'''
    def click_timing_section_element(self):
        element = self.page_model.get_timing_section_element()
        return self.element_operation(element)


    '''定时页面+号按钮'''
    def click_timing_add_button_element(self):
        element = self.page_model.get_timing_add_button_element()
        return self.element_operation(element)


    '''定时页面-定时picker_view'''
    def get_timing_picker_view(self):
        return self.page_model.get_timing_picker_view_element()


    '''定时页面-时间段定时'''
    def click_time_period_element(self):
        element = self.page_model.get_time_period_element()
        return self.element_operation(element)


    '''定时页面-定时开启'''
    def click_time_on_element(self):
        element = self.page_model.get_time_on_element()
        return self.element_operation(element)

    '''定时页面-定时关闭'''
    def click_time_off_element(self):
        element = self.page_model.get_time_off_element()
        return self.element_operation(element)


    '''具体定时页面picker_view左边'''
    def get_picker_view_left_element(self):
        return self.page_model.get_picker_view_left_element()


    '''具体定时页面picker_view右边'''
    def get_picker_view_right_element(self):
        return self.page_model.get_picker_view_right_element()


    '''具体定时页面确定按钮'''
    def click_picker_bottom_confirm_element(self):
        element = self.page_model.get_picker_bottom_confirm_element()
        return self.element_operation(element)


    '''重复选项picker_view'''
    def get_repeat_option_picker_view_element(self):
        element = self.page_model.get_repeat_option_picker_view_element()
        return self.element_operation(element)


    '''执行一次'''
    def click_repeat_option_picker_one_cell_element(self):
        element = self.page_model.get_repeat_option_picker_one_cell_element()
        return self.element_operation(element)


    '''每天'''
    def click_repeat_option_picker_two_cell_element(self):
        element = self.page_model.get_repeat_option_picker_two_cell_element()
        return self.element_operation(element)


    '''法定工作日'''
    def click_repeat_option_picker_three_cell_element(self):
        element = self.page_model.get_repeat_option_picker_three_cell_element()
        return self.element_operation(element)


    '''法定节假日'''
    def click_repeat_option_picker_forth_cell_element(self):
        element = self.page_model.get_repeat_option_picker_forth_cell_element()
        return self.element_operation(element)


    '''自定义'''
    def click_repeat_option_picker_fifth_cell_element(self):
        element = self.page_model.get_repeat_option_picker_fifth_cell_element()
        return self.element_operation(element)


    '''定时确定'''
    def click_title_bar_timing_confirm_element(self):
        element = self.page_model.get_title_bar_timing_confirm_element()
        return self.element_operation(element)


    '''定时取消'''
    def click_title_bar_timing_cancel_element(self):
        element = self.page_model.get_title_bar_timing_cancel_element()
        return self.element_operation(element)


    '''
    定时功能左上角关闭按钮
    '''
    def click_title_bar_return_button_element(self):
        element = self.page_model.get_title_bar_return_button_element()
        return self.element_operation(element)


    '''
    重复
    '''
    def click_repeat_cell_element(self):
        element = self.page_model.get_repeat_cell_element()
        return self.element_operation(element)


    '''
    开启
    '''
    def click_view_timer_on_cell_element(self):
        element = self.page_model.get_view_timer_on_cell_element()
        return self.element_operation(element)


    '''
    关闭
    '''
    def click_view_timer_off_cell_element(self):
        element = self.page_model.get_view_timer_off_cell_element()
        return self.element_operation(element)

    '''
    自定义重复选项--周日
    '''
    def click_custom_repeat_sunday_element(self):
        element = self.page_model.get_custom_repeat_sunday_element()
        return self.element_operation(element)

    '''
    开启的具体时间
    '''
    def get_timer_on_detail_element(self):
        element = self.page_model.get_timer_on_detail_element()
        return self.get_element(element)


    '''
    关闭的具体时间
    '''
    def get_timer_off_detail_element(self):
        element = self.page_model.get_timer_off_detail_element()
        return self.get_element(element)


    '''发现附近设备弹窗'''
    def get_discovery_device_alert_element(self):
        element = self.page_model.get_discovery_device_alert_element()
        return self.get_element(element)


    '''家庭共享弹窗'''
    def get_home_share_alert_element(self):
        element = self.page_model.get_home_share_alert_element()
        return self.get_element(element)



    '''门锁报警弹窗类的我知道了按钮'''
    def get_home_i_know_alert_element(self):
        element = self.page_model.get_home_i_know_alert_element()
        return self.get_element(element)


    '''升级提醒框'''
    def get_device_upgrade_alert(self):
        element = self.page_model.get_device_upgrade_alert_element()
        return self.get_element(element)


    '''进入插件的loading图标'''
    def get_loading_icon_element(self):
        element = self.page_model.get_loading_element()
        return self.get_element(element)


    '''授权弹窗'''
    def get_user_licence_title(self):
        element = self.page_model.get_user_licence_title_element()
        return self.get_element(element)


    '''授权弹窗确认授权按钮'''
    def get_user_licence_agree(self):
        element = self.page_model.get_user_licence_agree_element()
        return self.get_element(element)


    '''room_tag 判断是否还停留在房间页面'''
    def get_room_tag_element(self):
        element = self.page_model.get_room_tag_element()
        return self.get_element(element)


    def element_operation(self,element):
        if element:
            try:
                element.click()
            except ex.StaleElementReferenceException:
                print('StaleElementReferenceException:',self.page_model)
                element = self.page_model.get_room_list_back_element()
                element.click()
            return True
        else:
            print('元素不存在')
            return None



    def get_element(self,element):
        if element:
            return element
        else:
            print('元素不存在')
            return None

























