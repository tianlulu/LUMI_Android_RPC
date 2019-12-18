class Device_Rename_Function():
    def __init__(self,handle_model):
        self.handle = handle_model

    def cancel_modify_device_name(self):
        '''修改设备名称:取消修改设备名称'''
        assert self.handle.click_device_name_settings_element() == True, '设置-设备名称元素不存在'
        assert self.handle.click_input_view_clear_element() == True, '修改设备名称-删除设备名称按钮不存在'
        assert self.handle.click_cancel_button_element() == True, '修改设备名称-取消不存在'
        print('成功取消修改设备名称')


    def modify_device_name_0_characters(self):
        '''修改设备名称:0个字符'''
        assert self.handle.click_device_name_settings_element() == True, '设置-设备名称元素不存在'
        element = self.handle.click_edit_device_name_input_view()
        print('原来的的设备名称:', element.text)

        assert self.handle.click_input_view_clear_element() == True, '修改设备名称-删除设备名称按钮不存在'
        if element != None:
            print('修改后的设备名称:', element.text)
        assert self.handle.click_confirm_button_element() == True, '设备命名确认按钮不存在'
        assert self.handle.click_input_view_clear_element() == True, '点击确认按钮后修改设备名称框需要存在当前页面'
        assert self.handle.click_cancel_button_element() == True,'修改设备名称-取消不存在'
        print('修改设备名称为0个字符时，点击确认按钮后修改设备名称框依然存在')
        print('设置页面显示的设备名称:', self.handle.show_right_detail_device_name_element().text)


    def modify_device_name(self):
        '''修改设备名称:21个字符'''
        assert self.handle.click_device_name_settings_element() == True, '设置-修改设备名称元素不存在'
        element = self.handle.click_edit_device_name_input_view()
        print('原来的的设备名称:', element.text)
        assert self.handle.click_input_view_clear_element() == True, '修改设备名称-删除设备名称按钮不存在'
        if element != None:
            element.send_keys('修改设备名称1修改设备名称2修改设备名称3')
            print('修改后的设备名称:', element.text)
        assert self.handle.click_confirm_button_element() == True, '设备命名确认按钮不存在'
        '''发请求'''
        print('设置页面显示的设备名称:',self.handle.show_right_detail_device_name_element().text)


    def modify_device_name_exceed_character_limit(self):
        '''修改设备名称:>21个字符'''
        assert self.handle.click_device_name_settings_element() == True, '设置-修改设备名称元素不存在'
        element = self.handle.click_edit_device_name_input_view()
        print('原来的的设备名称:', element.text)
        assert self.handle.click_input_view_clear_element() == True, '修改设备名称-删除设备名称按钮不存在'
        if element != None:
            element.send_keys('修改设备名称1修改设备名称2修改设备名称3修改设备名称4修改设备名称5修改设备名称')
            print('修改后的设备名称:', element.text)
        assert self.handle.click_confirm_button_element() == True, '设备命名确认按钮不存在'
        assert self.handle.show_exceeded_the_maximum_character_limit_alert() != None, '超出字符限制红色提示不存在'
        assert self.handle.click_cancel_button_element() == True,'修改设备名称-取消不存在'
        print('修改设备名称为41个字符时，出现超出字符限制红色提示框')
        print('设置页面显示的设备名称:', self.handle.show_right_detail_device_name_element().text)
        assert self.handle.click_plugin_back_homepage_element(), '返回到插件首页的箭头按钮不存在'