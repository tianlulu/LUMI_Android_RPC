#coding=utf8

import os
# 执行相关shell命令

# 直接执行 不能拿到结果集
# print(os.system('adb devices'))
# print(os.popen('adb devices').readlines())


# ['List of devices attached\n', '192.168.56.101:5555\tdevice\n', '192.168.56.102:5555\tdevice\n', '\n']
# ['List of devices attached\n', '192.168.56.101:5555\tdevice\n', '192.168.56.102:5555\tdevice\n']
# ['List of devices attached', '192.168.56.101:5555\tdevice', '192.168.56.102:5555\tdevice']

class DosCmd():
    def execute_cmd_result(self,command):
        result = os.popen(command).readlines()
        result_list = []
        # print(result)

        for i in result:
            # 去掉最末端的'\n'
            if i == '\n':
                continue

            # 去掉字符串末尾的'\n'
            result_list.append(i.strip('\n'))
        # print(result_list)
        return result_list


    def excute_cmd(self,command):
        os.system(command)


    def excute_addons(self):
        # 获得当前目录
        path = '../util'
        current_path = os.getcwd()
        print('当前工作目录为:',current_path)

        os.chdir(path)
        new_path = os.getcwd()
        print('新的工作目录为:',new_path)

        # 执行相关命令
        os.popen('mitmdump -s addons.py').readlines()


if __name__ == '__main__':
    dos_cmd = DosCmd()
    # dos_cmd.execute_cmd_result('adb devices')
    # print(dos_cmd.execute_cmd_result('adb devices'))
    # ['List of devices attached\n', '192.168.56.101:5555\tdevice\n', '192.168.56.102:5555\tdevice\n', '\n']
    # ['List of devices attached\n', '192.168.56.101:5555\tdevice\n', '192.168.56.102:5555\tdevice\n']
    # ['List of devices attached', '192.168.56.101:5555\tdevice', '192.168.56.102:5555\tdevice']
    dos_cmd.excute_addons()