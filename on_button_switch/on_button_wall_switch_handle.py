
#coding=utf8
from base.base_handle import BaseHandle
from util.get_image_rgb import ImageRGBD
from selenium.common import exceptions as ex
from on_button_switch.one_button_wall_switch_page import One_Button_Wall_Switch_Page

class One_Button_Wall_Switch_Handle(BaseHandle):
    def __init__(self):
        self.page_model = One_Button_Wall_Switch_Page()
        BaseHandle.__init__(self,self.page_model)

    '''
    获取转无线开关按钮开关按钮颜色值
    '''
    def get_switch_element_rgba(self):
        image_rgb = ImageRGBD()
        # 截屏操作
        file_path = self.page_model.get_screen_shot_image()

        # 需要获取top_element RGB元素
        light_element = self.page_model.get_wireless_switch_function_switching_element()

        # 获取该元素中心位置的RGB颜色
        return image_rgb.get_element_rgb(light_element, file_path)


    '''
    获取顶部💡颜色
    蓝色：开状态
    灰色：关状态
    '''
    def get_light_bulb_element_rgba(self):
        image_rgb = ImageRGBD()
        # 截屏操作
        file_path = self.page_model.get_screen_shot_image()

        # 需要获取top_element RGB元素
        light_element = self.page_model.get_light_bulb_view_element()

        # 获取该元素中心位置的RGB颜色
        return image_rgb.get_element_rgb(light_element, file_path)


    '''
    开启/关闭电源按钮
    '''
    def click_on_off_light_element(self):
        element = self.page_model.get_on_off_element()
        return self.element_operation(element)


    '''
    首页-今日用电
    '''
    def click_current_day_electricity_element(self):
        element = self.page_model.get_current_day_electricity_element()
        return self.element_operation(element)


    '''
    首页-当月用电
    '''
    def click_current_month_electricity_element(self):
        element = self.page_model.get_current_month_electricity_element()
        return self.element_operation(element)


    '''
    获取电量度数显示/或者功率显示
    '''
    def get_electricity_or_power_degree_element(self):
        element = self.page_model.get_electricity_degree_element()
        return self.get_element(element)


    '''
    功率历史记录时间显示
    '''
    def get_power_time_element(self):
        element = self.page_model.get_power_time_element()
        return self.get_element(element)


    '''
    首页-功率历史记录
    '''
    def click_current_power_element(self):
        element = self.page_model.get_current_power_element()
        return self.element_operation(element)


    '''首页-功率显示'''
    def get_history_power_text_element(self):
        element = self.page_model.get_history_power_text_element()
        return self.get_element(element)


    '''
    电量统计-日按钮
    '''
    def click_day_degree_element(self):
        element = self.page_model.get_day_degree_element()
        return self.element_operation(element)


    '''
    电量统计-月按钮
    '''
    def click_month_degree_element(self):
        element = self.page_model.get_month_degree_element()
        return self.element_operation(element)


    '''
    功率历史--周按钮
    '''
    def click_week_degree_element(self):
        element = self.page_model.get_week_degree_element()
        return self.element_operation(element)


    '''
    设置-转无线开关设置
    '''
    def click_turn_wireless_switch_settings_element(self):
        element = self.page_model.get_turn_wireless_switch_settings_element()
        return self.element_operation(element)


    '''
    转无线开关设置-转无线开关功能切换按钮点击
    '''
    def click_wireless_switch_function_switching_element(self):
        element = self.page_model.get_wireless_switch_function_switching_element()
        return self.element_operation(element)



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






















