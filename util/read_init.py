
import configparser
# read_ini = configparser.ConfigParser()
# read_ini.read('../config/LocalElement.ini')
# print(read_ini.get('login_element','username'))


# 读取配置文件中的内容 即LocalElement.ini文件中的内容
class Readini:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '../config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()


    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # 通过key获取对应的value
    def get_value(self,key,section=None):
        # 默认为login_element节点 section也可以自己选择
        if section == None:
            section = 'plug_v1_element'
        # 异常处理 防止 程序传了错误的关键字信息
        try:
            value = self.data.get(section,key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = Readini()
    print(read_ini.get_value('username'))
    read_ini.get_value('username')
