'''
使用unittest编写测试用例

'''
#coding=utf8
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import HTMLTestRunner
import unittest
import threading
from appium import webdriver
from business.lumi_plug_v1_business import Plug_V1_Business
from util.server import Server
from util.write_user_command import WriteUserCommand
import multiprocessing
import time


'''
setUpClass中需要传入参数有没有入口
需要ParameTestCase这个方法来传入parames
'''
class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName)
        global parames
        parames = parame

class TestCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass',parames)
        cls.plug_v1_business = Plug_V1_Business(parames)
        # cls.login_business.click_go_login()

    def setUp(self):
        print('setUp')

    def test_case1(self):
        flag = True
        print('test_case1里面的参数===========',parames)

        # self.assertNotEqual('1','2')
        # 判断对象是否为True
        # self.assertTrue(flag)
        time.sleep(10)
        self.plug_v1_business.click_power()
        time.sleep(1)
        self.plug_v1_business.click_day_cost()

    def test_case2(self):
        print('test_case2里面的参数===========',parames)

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

# appium_init初始化
def appium_init():
    server = Server()
    server.execute_command_on_thread()

# 通过yaml中的个数获取运行的进程个数()
def get_count():
    write_file =WriteUserCommand()
    return write_file.get_yaml_file_lines()

def get_suite(i):
    print('get_suite里面的参数', i)
    # 定义一个测试容器
    suite = unittest.TestSuite()
    suite.addTest(TestCase('test_case1',parame=i))
    suite.addTest(TestCase('test_case2',parame=i))
    unittest.TextTestRunner().run(suite)

    '''
    # 定义个报告存放的路径，支持相对路径
    filename = '../report/tesecase'+str(i)+'_report'+'.html'
    file_result = open(filename, 'wb')

    # 定义测试报告
    HTMLTestRunner.HTMLTestRunner(stream=file_result,
                                  title='this is first report',
                                  description='测试报告详情:').run(suite)
    file_result.close()
    '''


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        # 如果是多线程的话会遇到线程互相穿插和混乱的情况
        t = multiprocessing.Process(target=get_suite, args=(i, ))
        threads.append(t)

    for j in threads:
        j.start()





















