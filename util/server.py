#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from dos.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand
import time

class Server:
    def __init__(self):
        self.dos = DosCmd()
        # 获取可用的设备信息
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        '''
        获取可用的设备信息
        '''
        # 处理result_list的结果,也就是真正想要的设备信息，有时候device是offline用不了
        devices_list = []

        #result_list： ['List of devices attached', '192.168.56.101:5555\tdevice', '192.168.56.102:5555\tdevice']
        # devices_list： ['192.168.56.101:5555', '192.168.56.102:5555']
        result_list = self.dos.execute_cmd_result('adb devices')

        if len(result_list)>= 2:
            for i in result_list:
                if 'List' in i:
                    continue

                # 192.168.56.101: 5555\tdevice
                device_info = i.split('\t')

                # device 如果是offine的话表明该设备不可用
                if device_info[1] == 'device':
                    # 192.168.56.101: 5555
                    devices_list.append(device_info[0])
            return devices_list
        else:
            return  None


    def create_port_list(self,start_port):
        '''
        拿到所有的port列表
        :param start_port:
        :return:
        '''
        port = Port()
        return port.create_port_list(start_port, self.device_list)


    def create_command_list(self,i):
        '''
        拿到所有的拼接命令列表
        :return:
        '''
        command_list = []
        # ['appium -p 4700 bp 4900 -U 192.168.56.101:5555 --no-reset --session-override',
        #  'appium -p 4701 bp 4901 -U 192.168.56.102:5555 --no-reset --session-override']

        first_port_list = self.create_port_list(4700)
        second_port_list = self.create_port_list(4900)
        device_list = self.device_list
        '''
        如果有俩个设备，就会有2个线程 第一个线程跑2遍 第二个线程跑2遍 一共四遍就会重复写入yaml文件中
            for i in range(len(device_list)):
            # 按照格式拼接command
            # command = 'appium -p '+str(first_port_list[i])+' -bp '+str(second_port_list[i]) + ' -U '+str(device_list[i])\
            #           +' --no-reset --session-override'
            command = 'appium -p '+str(first_port_list[i])+ ' -bp '+str(second_port_list[i])
            # print(command)
            command_list.append(command)
            # 将获得的数据写进yaml文件
            self.write_file.write_yaml_data(i,device_list[i],second_port_list[i],first_port_list[i])
        '''
        command = 'appium -p '+str(first_port_list[i])+' -bp '+str(second_port_list[i]) + ' -U '+str(device_list[i])\
                  +' --no-reset --session-override'
        # command = 'appium -p ' + str(first_port_list[i]) + ' -bp ' + str(second_port_list[i])

        print(command)
        command_list.append(command)

        # 将获得的数据写进yaml文件
        self.write_file.write_yaml_data(i, device_list[i], second_port_list[i], first_port_list[i])
        return command_list


    def execute_command(self, i):
        '''
        执行某一条拼接命令   即启动服务
        eg'appium -p 4700 -bp 4900 -U 192.168.56.101:5555 --no-reset --session-override
           appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset
        :return:
        '''
        print('执行的线程数', i)

        command_list = self.create_command_list(i)

        '''
        command_list现在返回值永远只有一个，不会存在多个的情况command_list[i]不合适
        如果有俩个设备  第一个4700 
                      第二个4701
        第一个线程进来的时候i=0   command_list[0]=4700没问题
        第一个线程进来的时候i=0   command_list[1]不存在 因为command_list列表中只有1个
        '''
        # self.dos.execute_cmd_result(command_list[i])
        self.dos.execute_cmd_result(command_list[0])
        # self.dos.execute_cmd_result('adb devices')


    def execute_command_on_thread(self):
        # 首先杀掉node相关进程
        self.kill_server()

        # 清理yaml中的数据
        self.write_file.clear_yaml_data()

        '''
        在多线程中执行command_list中的命令 根据设备数来确定线程数
        :return:
        '''
        threads = []
        for i in range(len(self.device_list)):
            t = threading.Thread(target=self.execute_command, args=(i, ))
            threads.append(t)

        for thread in threads:
            print(thread)
            thread.start()
        # 有时候服务并不能马上起来
        time.sleep(15)


    def kill_server(self):
        # 获取关于appium进程的结果   windows:tasklist | find "node.exe"
        node_list = self.dos.execute_cmd_result('ps -ef|grep node')
        if node_list != None:
            if len(node_list) > 0:
                # mac下杀掉node相关进程 windows:taskkill -F -PID node.exe"
                # self.dos.excute_cmd('kill -s 9 `pgrep node`')
                self.dos.excute_cmd('pkill node')


if __name__ == '__main__':
    server = Server()
    print(server.get_devices())
    # print(server.create_port_list(4700))
    # print(server.create_command_list())
    server.execute_command_on_thread()
