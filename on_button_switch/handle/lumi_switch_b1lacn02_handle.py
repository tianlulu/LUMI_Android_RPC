from on_button_switch.on_button_wall_switch_handle import One_Button_Wall_Switch_Handle
from on_button_switch.page.lumi_switch_b1lacn02_page import Switch_B1lacn02_Page
import time
class Switch_B1lacn02_Handle(One_Button_Wall_Switch_Handle):
    def __init__(self):
        self.page_model = Switch_B1lacn02_Page()
        One_Button_Wall_Switch_Handle.__init__(self)
        self.is_flag = False

    '''
    首页滑动控件直到房间出现(如:Sweet)
    step2:找房间
    '''
    def click_switch_b1lacn02_room_element(self):
        self.get_title_bar_room_element()
        i = 0
        count = 7
        while i < count:
            # 找房间
            element = self.page_model.get_switch_b1lacn02_room_element()
            # print('找到的房间号:',element)
            if element != None:
                element.click()
                print('滑动了' + str(i) + '次找到房间')
                self.is_flag = True
                break
            else:
                self.handling_the_home_popup()
                self.swipe_with('up')
                i = i + 1
                if (i == count):
                    print('滑动了' + str(i) + '次仍然没有找到该房间')
                    self.is_flag = False
                    break
        return self.is_flag


    def check_home_tag_element(self,i):
        device_home_element = self.page_model.get_current_day_electricity_element()
        if device_home_element != None:
            print('过了加载页面,成功进入插件')
            print('滑动了' + str(i) + '次找到设备')
            self.is_flag = True
            return True
        else:
            loading_element = self.get_loading_icon_element()
            if loading_element != None:
                print('卡在了设备加载页面')
            else:
                print('其他原因没有进入插件首页')
            return False

    '''
    从房间里面找到设备
    step2:找设备
    '''
    def click_switch_b1lacn02_device_element(self):
        i = 0
        count = 5
        while i < count:
            # 找设备
            element = self.page_model.get_switch_b1lacn02_device_element()
            if element != None:
                element.click()
                # 判断是否成功进入插件
                time.sleep(2)
                room_tag_exists = self.page_model.get_room_tag_element()
                if room_tag_exists != None:
                    print('点击设备没反应还在房间里面,点击设备后页面没有跳转,没有进入插件首页')
                    self.is_flag = False
                    break
                else:
                    print('已经不在房间里面了')
                    return self.check_home_tag_element(i)
            else:
                self.handling_the_home_popup()
                self.swipe_with('up')
                i = i + 1
                if (i == count):
                    print('滑动了' + str(i) + '次仍然没有找到该设备')
                    self.is_flag = False
                    break
        return self.is_flag



