#coding=utf8


from dos.dos_cmd import DosCmd
class Port:
    '''
    确认端口是否被占用
        # windows: netstate -nao | findstr:4723
        # mac:     lsof -i | 4723
    '''
    def port_is_used(self,port_num):
        self.dos = DosCmd()

        result = self.dos.execute_cmd_result('lsof -i:'+str(port_num))

        flag = None
        # 返回的有结果，表示这个端口已经被占用
        if len(result) > 0:
            # 被占用
            flag = False
        else:
            # 没有被占用
            flag = True
        return flag



    def create_port_list(self,start_port,device_list):
        '''
        根据设备列表个数生成p和bp两个可用端口 如有两个设备 生成两个-p和两个bp端口
        :param start_port:初始端口
        :param device_list:设备list
        :return:
        appium -p 4701 bp 4901 -U 192.168.56.102:5555 --no-reset --session-override
        '''
        port_list = []
        # get_devices获取的设备列表可能返回为空的情况
        if device_list != None:
            while len(port_list) != len(device_list):
                # 这个端口没被占用 添加到port_list
                if self.port_is_used(start_port):
                   port_list.append(start_port)
                # 端口号+1
                start_port = start_port + 1
            return port_list




if __name__ == '__main__':
   port = Port()
   print(port.create_port_list(4325,[1,2,3,4]))
   # print(port.port_is_used(4723))



