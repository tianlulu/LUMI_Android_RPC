#coding=utf8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import DriverUtil
from util.get_by_local import GetByLocal
from util.freedom_name import My_Custom_Name
from util.get_image_rgb import ImageRGBD
class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.my_local = GetByLocal(self.driver)
        self.custom_name = My_Custom_Name()

    '''
    获取toast元素信息
    '''
    def get_toast(self, message, timeout, poll_frequency):
        try:
            toast_element = ("xpath", "//*[contains(@text, " + "'" + message + "'" + ")]")
            toast = WebDriverWait(self.driver, timeout, poll_frequency)\
                .until( EC.presence_of_all_elements_located(toast_element))
            print('获取到了toast:',toast[0].text)
            return True
        except Exception as e:
            # print('Exception message',e)
            return False


    '''
    获取自定义房间中的设备名称（如：欧标插座）
    '''
    def get_custom_element(self, message, timeout, poll_frequency):
        try:
            custom_element = ("xpath", "//*[contains(@text, " + "'" + message + "'" + ")]")
            WebDriverWait(self.driver, timeout, poll_frequency)\
                .until(EC.presence_of_element_located(custom_element))
            # print('获取到了元素:',toast.text,type)
            return self.driver.find_element_by_xpath(custom_element[1])
        except Exception:
            # raise e
            # print('没有获取到元素')
            return None

    '''
    找到元素
    '''
    def find_element(self,loc_key, element = None, file_path = None):
        try:
            element = WebDriverWait(self.driver,5, poll_frequency=0.5) \
            .until(lambda driver: self.my_local.get_element(loc_key,element,file_path))
            return element
        except Exception:
            return None

    '''
    房间
    '''
    def get_room_element(self):
        return self.find_element('room')


    '''
    添加设备
    '''
    def get_add_device_element(self):
        return self.find_element('add_device')


    '''
    离线元素
    '''
    def get_offline_element(self):
        return self.find_element('is_offline')


    '''
    离线框关闭按钮
    '''
    def get_offline_close(self):
        return self.find_element('universal_offline_close')


    '''
    获取toast元素 如加载失败
    '''
    def get_toast_element(self, message):
        if self.get_toast(message, 5, 0.5):
            return True
        else:
            return False

    '''
    返回到插件首页的按钮
    '''
    def get_plugin_back_homepage_element(self):
        return self.find_element('plugin_back_homepage')


    '''
    通过返回按钮:房间页面返回房间列表页面
    '''
    def get_room_list_back_element(self):
        return self.find_element('room_list_back')


    '''
    三个点
    '''
    def get_more_element(self):
        return self.find_element('more')



    '''设置-定时'''
    def get_timing_section_element(self):
        return self.find_element('timing_section')



    '''定时页面+号按钮'''
    def get_timing_add_button_element(self):
        return self.find_element('timing_add_button')


    '''定时页面-定时picker_view'''
    def get_timing_picker_view_element(self):
        return self.find_element('timing_picker_view')


    '''定时页面-时间段定时'''
    def get_time_period_element(self):
        return self.find_element('time_period')


    '''定时页面-定时开启'''
    def get_time_on_element(self):
        return self.find_element('time_on')



    '''定时页面-定时关闭'''
    def get_time_off_element(self):
        return self.find_element('time_off')


    '''具体定时页面picker_view左边'''
    def get_picker_view_left_element(self):
        return self.find_element('picker_view_left')


    '''具体定时页面picker_view右边'''
    def get_picker_view_right_element(self):
        return self.find_element('picker_view_right')


    '''底部确定按钮'''
    def get_picker_bottom_confirm_element(self):
        return self.find_element('picker_view_bottom_confirm')


    '''重复选项picker_view'''
    def get_repeat_option_picker_view_element(self):
        return self.find_element('repeat_option_picker_view')


    '''执行一次'''
    def get_repeat_option_picker_one_cell_element(self):
        return self.find_element('repeat_option_picker_one_cell')


    '''每天'''
    def get_repeat_option_picker_two_cell_element(self):
        return self.find_element('repeat_option_picker_two_cell')


    '''法定工作日'''
    def get_repeat_option_picker_three_cell_element(self):
        return self.find_element('repeat_option_picker_three_cell')


    '''法定节假日'''
    def get_repeat_option_picker_forth_cell_element(self):
        return self.find_element('repeat_option_picker_forth_cell')


    '''自定义'''
    def get_repeat_option_picker_fifth_cell_element(self):
        return self.find_element('repeat_option_picker_fifth_cell')


    '''定时确定'''
    def get_title_bar_timing_confirm_element(self):
        return self.find_element('title_bar_timing_confirm')


    '''定时取消'''
    def get_title_bar_timing_cancel_element(self):
        return self.find_element('title_bar_timing_cancel')

    '''
    请设置关闭时间
    '''
    def get_timing_none_toast_element(self):
        return self.find_element('off_time_none')

    '''
    定时功能左上角关闭按钮
    '''
    def get_title_bar_return_button_element(self):
        return self.find_element('return_to_timing')

    '''
    重复一次
    '''
    def get_repeat_cell_element(self):
        return self.find_element('repeat')

    '''
    开启
    '''
    def get_view_timer_on_cell_element(self):
        return self.find_element('view_timer_on')

    '''
    关闭
    '''
    def get_view_timer_off_cell_element(self):
        return self.find_element('view_timer_off')


    '''
    自定义重复选项：周日
    '''
    def get_custom_repeat_sunday_element(self):
        return self.find_element('custom_repeat_sunday')


    '''
    开启的具体时间
    '''
    def get_timer_on_detail_element(self):
        return self.find_element('timer_on_detail')


    '''
    关闭的具体时间
    '''
    def get_timer_off_detail_element(self):
        return self.find_element('timer_off_detail')


    '''设置-设备名称'''
    def get_device_name_settings_element(self):
        return self.find_element('device_name_settings')


    '''修改设备名称-删除按钮'''
    def get_input_view_clear_element(self):
        return self.find_element('input_view_clear')


    '''修改设备名称-编辑框'''
    def get_input_view_edit_element(self):
        return self.find_element('input_view_edit')


    '''修改设备名称-确认删除'''
    def get_confirm_button_element(self):
        return self.my_local.get_element('modal_ok_btn')
        # return self.find_element('modal_ok_btn')


    '''修改设备名称-取消确认'''
    def get_cancel_button_element(self):
        return self.my_local.get_element('modal_cancel_btn')
        # return self.find_element('modal_cancel_btn')


    '''设置-设备名称-具体名称'''
    def get_right_detail_device_name_element(self):
        return self.find_element('device_name_right_detail')


    '''设置-设备名称-超出最大字符限制'''
    def get_exceeded_the_maximum_character_limit_alert(self):
        return self.find_element('exceeded_the_maximum_character_limit_alert')


    '''发现附近设备弹窗'''
    def get_discovery_device_alert_element(self):
        return self.my_local.get_element('discovery_device_modal')


    '''家庭共享弹窗'''
    def get_home_share_alert_element(self):
        return self.my_local.get_element('home_share_modal')


    '''门锁报警弹窗类的我知道了按钮'''
    def get_home_i_know_alert_element(self):
        return self.my_local.get_element('home_i_know_tips')


    '''升级提醒框'''
    def get_device_upgrade_alert_element(self):
        return self.my_local.get_element('device_upgrade_modal_desc')


    '''进入插件的loading图标'''
    def  get_loading_element(self):
        return self.my_local.get_element('device_loading_icon')


    '''授权弹窗'''
    def get_user_licence_title_element(self):
        return self.my_local.get_element('user_license_title')


    '''授权弹窗确认授权按钮'''
    def get_user_licence_agree_element(self):
        return self.my_local.get_element('user_license_agree')


    '''room_tag 判断是否还停留在房间页面'''
    def get_room_tag_element(self):
        return self.my_local.get_element('room_tag')


    '''
    截屏
    '''
    def get_screen_shot_image(self):
        imageRGB = ImageRGBD()
        file_path = imageRGB.get_screenshot_path()
        self.driver.get_screenshot_as_file(file_path)
        return file_path
















