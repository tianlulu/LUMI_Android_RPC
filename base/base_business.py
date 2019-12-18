
class BaseBusiness:
    def __init__(self,handle_model):
        self.handle = handle_model

    '''
    处理首页弹窗
    '''
    def handling_the_home_popup(self):
        '''
        1、发现发现附近设备弹窗--关闭
        2、发现共享设备弹窗--关闭
        3、发现门锁报警弹窗我知道了--点击
        '''
        if self.handle.get_discovery_device_alert_element() != None:
            self.handle.click_cancel_button_element()

        if self.handle.get_home_share_alert_element() != None:
            self.handle.click_cancel_button_element()

        i_know_tips = self.handle.get_home_i_know_alert_element()
        if i_know_tips != None:
            i_know_tips.click()










