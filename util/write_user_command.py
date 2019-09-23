#codimng=utf-8
'''
操作yaml文件： 读/取
'''
import yaml
class WriteUserCommand:
    def read_yaml_data(self):
        '''
        加载ymal文件内容
        :return:
        '''
        with open('../config/userconfig.yaml') as  fr:
            # 返回的是字典信息 通过默认加载​​器（FullLoader）禁止执行任意函数，该load函数也变得更加安全
            data = yaml.load(fr,Loader=yaml.FullLoader)
            return data


    def get_yaml_value(self,key,info):
        '''
        获取value
        :return:
        '''
        data = self.read_yaml_data()
        value = data[key][info]
        return  value


    def write_yaml_data(self,i,deviceName,bp,port):
        '''
        写入数据到yamal文件
        :param data:
        :return:
        '''
        with open('../config/userconfig.yaml','a') as fr:
            data =self.join_data(i,deviceName,bp,port)
            yaml.dump(data,fr)


    def join_data(self,i,deviceName,bp,port):
        '''
        拼接需要写入到yaml文件的参数
        :param i:
        :param deviceName:
        :param bp:
        :param port:
        :return:
        '''
        data = {
            "user_info_"+str(i):{
                "deviceName":deviceName,
                "bp":bp,
                "port":port
            }
        }
        return data


    def clear_yaml_data(self):
        with open('../config/userconfig.yaml', 'w') as fr:
            fr.truncate()
        fr.close()


    # 获取yaml中的个数
    def get_yaml_file_lines(self):
        data = self.read_yaml_data()
        return len(data)


if __name__ == '__main__':
    command = WriteUserCommand()
    # command.get_yaml_value('user_info_0','port')
    print(command.get_yaml_value('user_info_0', 'deviceName'))
    print(command.get_yaml_value('user_info_0','port'))
    






