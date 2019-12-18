import configparser
from common.constant_enum import ELEMENT_INI_PATH
from common.constant_enum import ELEMENT_INI
# read_ini = configparser.ConfigParser()
# read_ini.read('../config/LocalElement.ini')
# print(read_ini.get('login_element','username'))


# 读取配置文件中的内容 即LocalElement.ini文件中的内容
class Readini:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC'+ELEMENT_INI_PATH.default
        else:
            self.file_path = '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC'+file_path
        # print('ini_file_path:',self.file_path)
        self.data = self.read_ini()


    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini


    # 通过key获取对应的value
    def get_value(self,key,section=None):
        # 默认为login_element节点 section也可以自己选择
        if section == None:
            section = ELEMENT_INI.default
        try:
            value = self.data.get(section,key)
            # print('value:',value)
        except:
            value = None
        return value


if __name__ == '__main__':
    file_path = '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC/config/ControlElement.ini'
    read_ini = Readini(file_path)
    print(read_ini.get_value('home_ctrl_ln1_aq1','one_button_wall_switch_element'))
