
#coding=utf8
from appium import  webdriver
from util.write_user_command import WriteUserCommand
import threading

def get_android_driver():
        write_file=WriteUserCommand()
        i = 0
        # 获取第一个device的deviceName i代表的是第n个手机
        deviecs = write_file.get_yaml_value('user_info_'+str(i),'deviceName')
        # 获取第一个device的port
        port=write_file.get_yaml_value('user_info_' + str(i), 'port')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9.1.0',
            'deviceName': deviecs,
            'app': '/Users/lumi/Desktop/apk/commonfile_apk_5ac6e5d37cc13085a6b4b30f66a18113.apk',
            "automationName": "UiAutomator2",
            # 切换Activity
            'appActivity': 'com.xiaomi.smarthome.SmartHomeMainActivity',
            # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
            # 是否重置安装应用  执行的时候不会到指引页面
            'noReset': 'true',
            # 最新版本的这两个参数不需要配置
            # desired_caps['appActivity'] = ''
            # desired_caps['appPackage'] = ''
            'unicodeKeyboard' : 'true',
            'resetKeyboard':'true'
        }
        driver = webdriver.Remote('http://localhost:'+str(port)+'/wd/hub', desired_caps)
        print('启动driver',driver)
        print('首页的activity：',driver.current_activity)
        driver.wait_activity(driver.current_activity,25)
        return driver

class DriverUtil:
    '''driver工具类'''
    __instance = None
    __instance_lock = threading.Lock()
    @classmethod
    def get_driver(cls):
        '''获取driver'''
        with DriverUtil.__instance_lock:
            if not DriverUtil.__instance:
                DriverUtil.__instance = get_android_driver()
        return DriverUtil.__instance




