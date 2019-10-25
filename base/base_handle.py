#coding=utf8
from util.swip_operation import Swip_Common
from base.base_driver import DriverUtil

class BaseHandle:
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.swipe_common = Swip_Common(self.driver)
        self.is_flag = False

    '''
    按照方向滑动页面
    '''
    def swipe_with(self,direction):
        if direction == 'up':
            self.swipe_common.swipe_up()
        elif direction == 'down':
            self.swipe_common.swipe_down()

    '''
    直接从首页滚动找到设备
    '''
    def get_home_device(self,page_model):
        i=0
        count = 40
        while i < count:
            element = page_model.get_home_device_element()
            if element != None:
                element.click()
                print('滑动了'+str(i)+'次找到设备')
                self.is_flag = True
                break
            else:
                self.swipe_with('up')
                i=i+1
                if(i == count):
                    print('滑动了'+str(i)+'次仍然没有找到设备')
                    self.is_flag = False
                    break
        return self.is_flag


    '''
    从房间里面找到设备
    step1:找房间
    '''
    def find_room(self,page_model):
        i=0
        count = 4
        while i < count:
            # 找房间
            element = page_model.get_device_room()
            # print('找到的房间号:',element)
            if element != None:
                element.click()
                print('滑动了'+str(i)+'次找到房间')
                # 找设备
                # self.is_flag =self.find_device(page_model)
                self.is_flag = True
                break
            else:
                self.swipe_with('up')
                i=i+1
                if(i == count):
                    print('滑动了'+str(i)+'次仍然没有找到该房间')
                    self.is_flag = False
                    break
        return self.is_flag


    '''
    从房间里面找到设备
    step2:找设备
    '''
    def find_device(self,page_model):
        i=0
        count = 5
        while i < count:
            # 找设备
            element = page_model.get_home_device_element()
            if element != None:
                element.click()
                print('滑动了'+str(i)+'次找到设备')
                self.is_flag = True
                break
            else:
                self.swipe_with('up')
                i=i+1
                if(i == count):
                    print('滑动了'+str(i)+'次仍然没有找到该设备')
                    self.is_flag = False
                    break
        return self.is_flag


    '''用例运行完之后返回滚动到首页顶部'''
    def to_top(self,page_model):
        i = 0
        count = 20
        while i < count:
            element = page_model.get_add_device_element()
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


















