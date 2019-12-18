#coding=utf-8

class Swip_Common():
    def __init__(self,driver):
        # 控件内滑动需要传入driver
        self.driver = driver

    '''
    获取屏幕的宽和高
    在整个屏幕上进行滑动
    默认是在整体页面上进行滑动
    '''
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    '''
    在相关控件内进行滑动
    比如滑动日期控件
    '''
    def get_element_size(self, element):
        # print('self.element',self.element)
        location = element.location
        size = element.size
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        # print(x,y,width,height)
        return x, y, width, height

    '''
    控件内滑动
    '''
    def swipe_in_element(self,element, start_point, end_point):
        element_size = self.get_element_size(element)
        # print('start_point:=======', start_point)
        # print('end_point:======', end_point)
        x1 = element_size[0] + element_size[2]/2
        # print('x1:======', x1)
        y = element_size[1] + element_size[3]/ 10*start_point
        # print('y:', y)
        # y1 = element_size[1] + element_size[3]/end_point
        y1 = self.get_size()[1] / 10*end_point
        # print('y1:',y1)
        print('从'+str(y) + "滑动到" + str(y1) + "的位置")
        self.driver.swipe(x1, y, x1, y1, 1000)


    # 全屏基础上向上滑动
    def swipe_up(self):
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*8
        y = self.get_size()[1]/10*4
        self.driver.swipe(x1, y1, x1, y,1000)

    # 全屏基础上向下滑动
    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*4
        y = self.get_size()[1]/10*8
        self.driver.swipe(x1, y1, x1, y,1000)
