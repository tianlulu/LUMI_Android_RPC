class Timer_Function:
    def __init__(self,handle_model):
        self.handle = handle_model

    # 滑动左边picker_view
    def swip_left_picker(self,start, end):
        left_picker = self.handle.get_picker_view_left_element()
        if left_picker != None:
            self.handle.swipe_based_on_element(left_picker,start,end)
        else:
            print('定时页面picker_view左边元素不存在')
            return None

    # 滑动右边picker_view
    def swip_right_picker(self,start, end):
        right_picker = self.handle.get_picker_view_right_element()
        if right_picker != None:
            self.handle.swipe_based_on_element(right_picker,start,end)
        else:
            print('定时页面picker_view右边元素不存在')
            return None

    def time_period_no_shutdown_time_set(self):
        '''定时功能:时间段定时，执行一次,未设置关闭时间'''
        assert self.handle.click_more_element() == True, '三个点更多按钮元素不存在'
        assert self.handle.click_timing_section_element()==True,'设置页定时cell元素不存在'
        assert self.handle.click_timing_add_button_element()==True,'定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view()!= None,'定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_period_element()==True,'时间段定时选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 9)
        assert self.handle.click_picker_bottom_confirm_element(),'定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_title_bar_timing_confirm_element(),'定时页面右上角确定按钮不存在'
        assert self.handle.get_fail_toast('请设置关闭时间')==True,'没有获取到请设置关闭时间toast'


    def time_period_execute_once(self):
        '''定时功能:时间段定时，执行一次'''
        assert self.handle.click_view_timer_off_cell_element() == True, '时间段定时页面关闭cell按钮不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text()
        assert self.handle.click_title_bar_timing_confirm_element()== True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def time_period_daily(self):
        '''定时功能:时间段定时,每天'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_period_element() == True, '时间段定时选择方式不存在'
        self.swip_left_picker(8, 3)
        self.swip_right_picker(1, 9)
        assert self.handle.click_picker_bottom_confirm_element(), '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element(), '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_two_cell_element() == True,'每天选项不存在'
        assert self.handle.click_view_timer_off_cell_element() == True, '时间段定时页面关闭cell按钮不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text()
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text


    def time_period_legal_working_day(self):
        '''定时功能:时间段定时,法定工作日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_period_element() == True, '时间段定时选择方式不存在'
        self.swip_left_picker(1, 9)
        self.swip_right_picker(8, 7)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_three_cell_element() == True, '法定工作日选项不存在'
        assert self.handle.click_view_timer_off_cell_element() == True, '时间段定时页面关闭cell按钮不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text()
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def time_period_legal_holidays(self):
        '''定时功能:时间段定时,法定节假日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_period_element() == True, '时间段定时选择方式不存在'
        self.swip_left_picker(8, 7)
        self.swip_right_picker(1, 9)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_forth_cell_element() == True, '法定节假日选项不存在'
        assert self.handle.click_view_timer_off_cell_element() == True, '时间段定时页面关闭cell按钮不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text()
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def time_period_custom(self):
        '''定时功能:时间段定时，自定义'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_period_element() == True, '时间段定时选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element(), '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_fifth_cell_element() == True, '自定义选项不存在'
        assert self.handle.click_custom_repeat_sunday_element() == True,'自定义重复--周日不存在'
        assert self.handle.click_picker_bottom_confirm_element() == True, '自定义重复--确定按钮不存在'
        assert self.handle.click_view_timer_off_cell_element() == True, '时间段定时页面关闭cell按钮不存在'
        self.swip_left_picker(1, 8)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text()
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def timed_on_execute_once(self):
        '''定时功能:定时开启,执行一次'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_on_element() == True, '定时开启选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 6)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        on_time_text =self.get_on_off_time_text('on')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_time_text

    def timed_on_execute_daily(self):
        '''定时功能:定时开启,每天'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_on_element() == True, '定时开启选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element(), '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_two_cell_element() == True, '每天选项不存在'
        on_off_time_text = self.get_on_off_time_text('on')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def timed_on_legal_working_day(self):
        '''定时功能:定时开启，法定工作日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_on_element() == True, '定时开启选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_three_cell_element() == True, '法定工作日选项不存在'
        on_off_time_text = self.get_on_off_time_text('on')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text


    def timed_on_legal_holidays(self):
        '''定时功能:定时开启,法定节假日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_on_element() == True, '定时开启选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_forth_cell_element() == True, '法定节假日选项不存在'
        on_off_time_text = self.get_on_off_time_text('on')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def timed_on_custom(self):
        '''定时功能:定时开启,自定义'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_on_element() == True, '定时开启时选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_fifth_cell_element() == True, '自定义选项不存在'
        assert self.handle.click_custom_repeat_sunday_element() == True, '自定义重复--周日不存在'
        assert self.handle.click_picker_bottom_confirm_element() == True, '自定义重复--确定按钮不存在'
        on_off_time_text = self.get_on_off_time_text('on')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return on_off_time_text

    def timed_off_execute_once(self):
        '''定时功能:定时关闭,执行一次'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_off_element() == True, '定时关闭选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 6)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        off_time_text = self.get_on_off_time_text('off')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return off_time_text

    def timed_off_execute_daily(self):
        '''定时功能:定时关闭,每天'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_off_element() == True, '定时关闭选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element() == True, '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_two_cell_element() == True, '每天选项不存在'
        off_time_text = self.get_on_off_time_text('off')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return off_time_text

    def timed_off_legal_working_day(self):
        '''定时功能:定时关闭，法定工作日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_off_element() == True, '定时关闭选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element(), '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_three_cell_element() == True, '法定工作日选项不存在'
        off_time_text = self.get_on_off_time_text('off')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return off_time_text

    def timed_off_legal_holidays(self):
        '''定时功能:定时关闭,法定节假日'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_off_element() == True, '定时关闭选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(9, 3)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element(), '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_forth_cell_element() == True, '法定节假日选项不存在'
        off_time_text = self.get_on_off_time_text('off')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return off_time_text

    def timed_off_custom(self):
        '''定时功能:定时关闭,自定义'''
        assert self.handle.click_timing_add_button_element() == True, '定时页面+号按钮不存在'
        assert self.handle.get_timing_picker_view() != None, '定时页面-定时方式选择元素不存在'
        assert self.handle.click_time_off_element() == True, '定时关闭时选择方式不存在'
        self.swip_left_picker(9, 3)
        self.swip_right_picker(1, 8)
        assert self.handle.click_picker_bottom_confirm_element() == True, '定时页面确定按钮picker_view底部确定按钮不存在'
        assert self.handle.click_repeat_cell_element(), '时间段定时页面重复选项cell按钮不存在'
        assert self.handle.click_repeat_option_picker_fifth_cell_element() == True, '自定义选项不存在'
        assert self.handle.click_custom_repeat_sunday_element() == True, '自定义重复--周日不存在'
        assert self.handle.click_picker_bottom_confirm_element() == True, '自定义重复--确定按钮不存在'
        off_time_text = self.get_on_off_time_text('off')
        assert self.handle.click_title_bar_timing_confirm_element() == True, '定时页面右上角确定按钮不存在'
        return off_time_text

    def get_on_off_time_text(self,time_text = None):
        if time_text == 'off':
            off_time_text = self.handle.get_timer_off_detail_element().text
            print('设置的定时关闭时间为:',off_time_text)
            return off_time_text
        elif time_text == 'on':
            on_time_text = self.handle.get_timer_on_detail_element().text
            print('设置的定时开启时间为:',on_time_text)
            return on_time_text
        else:
            off_time_text = self.handle.get_timer_off_detail_element().text
            print('时间段定时结束时间为:', off_time_text)
            on_time_text = self.handle.get_timer_on_detail_element().text
            print('时间段定时开启时间为:', on_time_text)
            return on_time_text,off_time_text


    '''定时首页校验设置的定时功能'''
    def find_out_timing_set(self):
        pass
