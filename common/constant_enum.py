class URL_PATH:
    rpc = '/app/home/rpc/'
    electricity_statistics = '/v2/user/statistics'
    device_rename = '/app/device/rename'
    scene = '/app/scene/edit'

class ELEMENT_INI_PATH:
    default = '/config/LocalElement.ini'
    control = '/config/ControlElement.ini'
    sensor = '/config/SendorElement.ini'

class ELEMENT_INI:
    default = 'common_element'
    one_button_wall_switch = 'one_button_wall_switch_element'

class TIME_TYPE:
    # 定时开启
    time_on = 1
    # 定时关闭
    time_off = 2
    # 时间段定时
    time_on_off = 3

class TIME_CUSTOME_TYPE:
    # 执行一次
    once = 1
    # 每天
    period_daily = 2
    # 法定工作日
    legal_working_day = 3
    # 法定节假日
    legal_holidays = 4
    # 自定义
    custom = 5


