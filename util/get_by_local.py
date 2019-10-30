#coding=utf-8
from util.read_init import Readini
from selenium.common import exceptions as ex

class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self,key,section=None):
        if section != None:
            read_ini = Readini()
            # 根据Readini中的关键字获取定位信息 id classname xpath
            # eg：id>com.xiaomi.gateway:id/plug_big_toggle_iv
            local = read_ini.get_value(key,section)
            # if local != None:
            # 以>分隔 id > com.xiaomi.gateway:id/plug_big_toggle_iv
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                # 需要有容错处理，否则预期元素为空额话就就会报错
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'xpath':
                    return self.driver.find_element_by_xpath(local_by)
                else:
                    return self.driver.find_element_by_accessibility_id(local_by)
            except:
                return None
        else:
            return None








