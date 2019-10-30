#coding=utf8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import DriverUtil
from util.get_by_local import GetByLocal
from util.freedom_name import My_Custom_Name
from util.get_image_rgb import ImageRGBD
from selenium.common import exceptions as ex
class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.my_local = GetByLocal(self.driver)
        self.common_element = 'common_element'
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
            print('Exception message',e)
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
    def find_element(self,loc_key, element):
        try:
            element = WebDriverWait(self.driver,5, poll_frequency=0.5) \
            .until(lambda driver: self.my_local.get_element(loc_key,element))
            return element
        except Exception:
            return None

    '''
    房间
    '''
    def get_room_element(self):
        return self.find_element('room', self.common_element)


    '''
    添加设备
    '''
    def get_add_device_element(self):
        return self.find_element('add_device',self.common_element)


    '''
    离线元素
    '''
    def get_offline_element(self):
        return self.find_element('is_offline',self.common_element)

    '''
    离线框关闭按钮
    '''
    def get_offline_close(self):
        return self.find_element('universal_offline_close', self.common_element)


    '''
    获取toast元素 如加载失败
    '''
    def get_toast_element(self, message):
        if self.get_toast(message, 5, 0.5):
            return True
        else:
            return False

    '''
    插件首页的返回按钮
    '''
    def get_plugin_back_homepage_element(self):
        return self.find_element('plugin_back_homepage', self.common_element)


    '''
    通过返回按钮:房间页面返回房间列表页面
    '''
    def get_room_list_back_element(self):
        return self.find_element('room_list_back', self.common_element)


    '''
    截屏
    '''
    def get_screen_shot_image(self):
        imageRGB = ImageRGBD()
        file_path = imageRGB.get_screenshot_path()
        self.driver.get_screenshot_as_file(file_path)
        return file_path














