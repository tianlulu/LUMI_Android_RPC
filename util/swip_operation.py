#coding=utf-8

class Swip_Common():
    def __init__(self,driver, element=None):
        # 控件内滑动需要传入driver
        self.driver = driver
        if element != None:
            self.element = element

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
    def get_element_size(self):
        # print('self.element',self.element)
        location = self.element.location
        size = self.element.size
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        print(x,y,width,height)
        return x, y, width, height

    '''
    控件内滑动
    '''
    def swipe_element_up(self):
        element_size = self.get_element_size()
        x1 = (element_size[0] + element_size[0] + element_size[2]) / 2
        y = (element_size[1] + element_size[3]) / 10*9
        y1 = element_size[1] / 10*6
        # print('开始滑动页面============================')
        # print('滑动距离:',x1,y,x1,y1)
        self.driver.swipe(x1, y, x1, y1, 2000)


    '''
        # 按照一定的比例向左边滑动
        def swipe_left(self):
            # [100,200]
            x1 = self.get_size()[0]/10*9
            y1 = self.get_size()[1]/2
            x = self.get_size()[0]/10
            self.driver.swipe(x1, y1, x, y1,2000)

        # 向右边滑动
        def swipe_right(self):
            # [100,200]
            x1 = self.get_size()[0]/10
            y1 = self.get_size()[1]/2
            x = self.get_size()[0]/10*9
            self.driver.swipe(x1, y1, x, y1,2000)
        '''
    # 向上滑动
    def swipe_up(self):
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*8
        y = self.get_size()[1]/10*4
        self.driver.swipe(x1, y1, x1, y,1000)

    # 向下滑动
    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*4
        y = self.get_size()[1]/10*8
        self.driver.swipe(x1, y1, x1, y,1000)