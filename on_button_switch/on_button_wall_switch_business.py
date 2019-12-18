from common.function.device_rename_function import Device_Rename_Function
from common.function.timer_function import Timer_Function
from base.base_business import BaseBusiness
import time
class On_Button_Wall_Switch_Business(BaseBusiness):
    def __init__(self,handle_model):
        self.device_rename_function = Device_Rename_Function(handle_model)
        self.timer_function  = Timer_Function(handle_model)
        self.handle = handle_model
        BaseBusiness.__init__(self,handle_model)


    # 滑动左边picker_view
    def swip_left_picker(self,start, end):
        self.timer_function.swip_left_picker(start,end)


    # 滑动右边picker_view
    def swip_right_picker(self,start, end):
        self.timer_function.swip_right_picker(start, end)


    def time_period_no_shutdown_time_set(self):
        '''定时功能:时间段定时，执行一次,未设置关闭时间'''
        self.timer_function.time_period_no_shutdown_time_set()


    def time_period_execute_once(self):
        '''定时功能:时间段定时，执行一次'''
        return self.timer_function.time_period_execute_once()


    def time_period_daily(self):
        '''定时功能:时间段定时,每天'''
        return self.timer_function.time_period_daily()


    def time_period_legal_working_day(self):
        '''定时功能:时间段定时,法定工作日'''
        return self.timer_function.time_period_legal_working_day()


    def time_period_legal_holidays(self):
        '''定时功能:时间段定时,法定节假日'''
        return self.timer_function.time_period_legal_holidays()


    def time_period_custom(self):
        '''定时功能:时间段定时，自定义'''
        return self.timer_function.time_period_custom()


    def timed_on_execute_once(self):
        '''定时功能:定时开启,执行一次'''
        return self.timer_function.timed_on_execute_once()


    def timed_on_execute_daily(self):
        '''定时功能:定时开启,每天'''
        return self.timer_function.timed_on_execute_daily()


    def timed_on_legal_working_day(self):
        '''定时功能:定时开启，法定工作日'''
        return self.timer_function.timed_on_legal_working_day()


    def timed_on_legal_holidays(self):
        '''定时功能:定时开启,法定节假日'''
        return self.timer_function.timed_on_legal_holidays()


    def timed_on_custom(self):
        '''定时功能:定时开启,自定义'''
        return self.timer_function.timed_on_custom()


    def timed_off_execute_once(self):
        '''定时功能:定时关闭,执行一次'''
        return self.timer_function.timed_off_execute_once()


    def timed_off_execute_daily(self):
        '''定时功能:定时关闭,每天'''
        return self.timer_function.timed_off_execute_daily()


    def timed_off_legal_working_day(self):
        '''定时功能:定时关闭，法定工作日'''
        return self.timer_function.timed_off_legal_working_day()


    def timed_off_legal_holidays(self):
        '''定时功能:定时关闭,法定节假日'''
        return self.timer_function.timed_off_legal_holidays()


    def timed_off_custom(self):
        '''定时功能:定时关闭,自定义'''
        return self.timer_function.timed_off_custom()


    def get_on_off_time_text(self,time_text = None):
        self.timer_function.get_on_off_time_text(time_text)


    def cancel_modify_device_name(self):
        '''修改设备名称:取消修改设备名称'''
        self.device_rename_function.cancel_modify_device_name()


    def modify_device_name_0_characters(self):
        '''修改设备名称:0个字符'''
        self.device_rename_function.modify_device_name_0_characters()


    def modify_device_name(self):
        '''修改设备名称:21个字符'''
        self.device_rename_function.modify_device_name()


    def modify_device_name_exceed_character_limit(self):
        '''修改设备名称:>21个字符'''
        self.device_rename_function.modify_device_name_exceed_character_limit()


    def get_the_correct_electricity_data(self,one_button_wall_switch_data,is_day_type):
        count = 0
        while count < 50:
            electricity_element = self.handle.get_electricity_or_power_degree_element()
            if electricity_element != None:
                # 进入页面 拿到元素功率元素为''，表示数据还未刷新，接口数据还未返回，继续获取该元素直到拿到不为''的数据
                if electricity_element.text == '':
                    # print('电量数据加载中...', count)
                    count = count + 1
                    time.sleep(1)
                else:
                    if is_day_type:
                        one_button_wall_switch_data.get_the_current_electricity_request_data(True)
                        interface_day_electricity = one_button_wall_switch_data.statistics_electricity(True)
                        show_day_electricity = electricity_element.text
                        print('页面当日电量度数为:', show_day_electricity)
                        assert interface_day_electricity in show_day_electricity,'接口返回后计算当日电量与页面显示电量不一致'
                        break
                    else:
                        one_button_wall_switch_data.get_the_current_electricity_request_data(False)
                        interface_month_electricity = one_button_wall_switch_data.statistics_electricity(False)
                        show_month_electricity = electricity_element.text
                        print('页面当月电量度数为:', show_month_electricity)
                        assert interface_month_electricity in show_month_electricity, '接口返回计算当月电量与页面显示电量不一致'
                        break

    def get_the_correct_power_data(self,one_button_wall_switch_data,is_day_type):
        count = 0
        while count < 50:
            power_element = self.handle.get_electricity_or_power_degree_element()
            if power_element != None:
                # 进入页面 拿到元素功率元素为''，表示数据还未刷新，接口数据还未返回，继续获取该元素直到拿到不为''的数据
                if power_element.text == '':
                    # print('功率数据加载中...', count)
                    count = count + 1
                    time.sleep(1)
                else:
                    if is_day_type:
                        one_button_wall_switch_data.get_the_current_power_request_data(True)
                        interface_power_or_time = one_button_wall_switch_data.statistics_power(True)
                        interface_day_power = interface_power_or_time[0]
                        interface_day_time = interface_power_or_time[1]
                        show_day_power = power_element.text
                        print('页面当日功率显示为', show_day_power)
                        assert interface_day_power in show_day_power,'接口返回后计算的当日功率与页面显示电量不一致'
                        time_element = self.handle.get_power_time_element()
                        if time_element != None:
                            show_day_time = time_element.text
                            print('页面当前时间为:', show_day_time)
                            assert interface_day_time in show_day_time,'接口返回时间与页面显示时间不一致'
                        break
                    else:
                        one_button_wall_switch_data.get_the_current_power_request_data(False)
                        interface_power_or_time = one_button_wall_switch_data.statistics_power(False)
                        interface_week_power = interface_power_or_time[0]
                        interface_week_time = interface_power_or_time[1]
                        show_week_power = power_element.text
                        print('页面本周功率显示为', show_week_power)
                        assert interface_week_power in show_week_power,'接口返回后计算的本周功率与页面显示电量不一致'
                        time_element = self.handle.get_power_time_element()
                        if time_element != None:
                            show_week_time = time_element.text
                            print('页面当前时间为:', show_week_time)
                            assert interface_week_time in show_week_time,'接口返回时间与页面显示时间不一致'
                        break




