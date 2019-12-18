from data.operation_json.rpc_operation_json import RPC_Operation_Json
from data.operation_json.statistics_operation_json import Statistics_Operation_Json
from data.operation_json.device_rename_json import Device_Rename_Json
from data.operation_json.scene_edit_json import Scene_Edit_Json
from common.constant_enum import TIME_TYPE
from common.constant_enum import TIME_CUSTOME_TYPE
import time

class One_Button_Wall_Switch_Data():
    def __init__(self):
        self.rpc_operation_json = RPC_Operation_Json()
        self.statistics_operation_json = Statistics_Operation_Json()
        self.device_rename_json = Device_Rename_Json()
        self.scene_edit_json = Scene_Edit_Json()

    '''
    插件首页--获取设备状态（ctrl_ln1_v1）
    '''
    def get_home_data_and_analysis(self,is_neutral):
        request_data = self.rpc_operation_json.read_get_device_prop_exp_request_data()
        print('请求参数:', request_data)
        method = request_data['method']
        print('请求方法为:' + method)
        assert method == 'get_device_prop_exp', '请求方法错误'
        # self.assertEqual(method,'get_device_prop_exp')
        param_list = request_data['params'][0]
        if is_neutral:
            assert param_list[1] == 'neutral_0', '请求参数错误：预期参数：neutral_0 实际参数：' + param_list[1]
        else:
            assert param_list[1] == 'channel_0', '请求参数错误：预期参数：channel_0 实际参数：' + param_list[1]
            assert param_list[2] == 'load_power', '请求参数错误：预期参数：load_power 实际参数：' + param_list[2]
        response_data = self.rpc_operation_json.read_get_device_prop_exp_response_data()
        try:
            result = response_data['result'][0][0]
            print('获取到的开关状态为' + result)
        except Exception as e:
            print('没有获取到开关状态', e)


    '''
    rpc获取当前功率
    '''
    def get_current_power(self):
        response_data = self.rpc_operation_json.read_get_device_prop_exp_response_data()
        result = response_data['result']
        # 保留两位小数
        power = '%.2f' % result[0][1]
        print('接口返回的当前功率为:', power)
        return str(power)

    '''
    开/关插座
    '''
    def set_toggle_plug_on_off(self, is_on,is_neutral):
        data = self.rpc_operation_json.read_toggle_ctrl_neutral_request_data()
        print('请求参数:', data)
        method = data['method']
        print('请求方法为:' + method)
        # self.assertEqual(method,'toggle_ctrl_neutral')
        assert method == 'toggle_ctrl_neutral', '请求方法错误'
        param_values = data['params']
        if is_neutral:
            assert param_values[0] == 'neutral_0', '请求参数错误：预期参数：neutral_0 实际参数：' + param_values[0]
        else:
            assert param_values[0] == 'channel_0', '请求参数错误：预期参数：channel_0 实际参数：' + param_values[0]
        if is_on:
            assert param_values[1] == 'on', '请求参数错误：预期参数：on 实际参数：' + param_values[1]
            print('成功打开开关')
        else:
            assert param_values[1] == 'off', '请求参数错误：预期参数：off 实际参数：' + param_values[1]
            print('成功关闭开关')
        for value in param_values:
            print('params请求参数中带有' + value)


    '''
    当日/月电量接口请求数据
    '''
    def get_the_current_electricity_request_data(self, is_day_type):
        if is_day_type:
            request_data = self.statistics_operation_json.read_request_electricity_day_data()
        else:
            request_data = self.statistics_operation_json.read_request_electricity_month_data()
        assert 'did' in request_data.keys(), '请求参数中没有did'
        assert 'key' in request_data.keys(), '请求参数中没有key'
        assert 'data_type' in request_data.keys(), '请求参数中没有data_type'
        assert 'limit' in request_data.keys(), '请求参数中没有limit'
        assert 'start_date' in request_data.keys(), '请求参数中没有start_date'
        assert 'end_date' in request_data.keys(), '请求参数中没有end_date'
        assert request_data['key'] == 'powerCost', 'key对应参数值错误,错误值为' + request_data['key']
        if is_day_type:
            assert request_data['data_type'] == 'stat_day', 'data_type对应参数值错误,错误值为' + request_data['data_type']
        else:
            assert request_data['data_type'] == 'stat_month', 'data_type对应参数值错误,错误值为' + request_data['data_type']
        for item, value in request_data.items():
            print('请求参数:' + item, '参数值:' + str(value))


    '''
    当日/周的功率
    '''
    def get_the_current_power_request_data(self, is_day_type):
        if is_day_type:
            request_data = self.statistics_operation_json.read_request_power_day_data()
            print('本日功率请求参数:', request_data)
        else:
            request_data = self.statistics_operation_json.read_request_power_week_data()
            print('本周功率请求参数:', request_data)
        assert 'did' in request_data.keys(), '请求参数中没有did'
        assert 'key' in request_data.keys(), '请求参数中没有key'
        assert 'data_type' in request_data.keys(), '请求参数中没有data_type'
        assert 'limit' in request_data.keys(), '请求参数中没有limit'
        assert 'time_start' in request_data.keys(), '请求参数中没有time_start'
        assert 'time_end' in request_data.keys(), '请求参数中没有time_end'
        assert request_data['key'] == 'load_power', 'key对应参数值错误,错误值为' + request_data['key']
        if is_day_type:
            assert request_data['data_type'] == 'stat_day_v3', 'data_type对应参数值错误,错误值为' + request_data['data_type']
        else:
            assert request_data['data_type'] == 'stat_week_v3', 'data_type对应参数值错误,错误值为' + request_data['data_type']
        for item, value in request_data.items():
            print('请求参数:' + item, '参数值:' + str(value))


    '''
    电量统计页面---统计当日/月电量
    '''
    def statistics_electricity(self, electricity_type):
        if electricity_type:
            response_data = self.statistics_operation_json.read_response_electricity_day_data()
        else:
            response_data = self.statistics_operation_json.read_response_electricity_month_data()
        print('返回参数:', response_data)
        if response_data['code'] == 0:
            try:
                if response_data['result'] == []:
                    data = '%.1f' % float(0)
                    return data
                else:
                    item = response_data['result'][0]
                    print('item:', item)
                    value = item['value'][1:-1]
                    print('value:', value)
                    data = '%.1f' % (int(value) / 1000)
                print('接口返回的电量度数为:', data)
                return data
            except Exception:
                print(Exception)
        else:
            print('获取电量情况失败')


    '''
    功率统计页---统计本周/日功率
    '''
    def statistics_power(self, power_type):
        if power_type:
            response_data = self.statistics_operation_json.read_response_power_day_data()
            print('当日功率请求后的返回参数:', response_data)
        else:
            response_data = self.statistics_operation_json.read_response_power_week_data()
            print('当月功率请求后的返回参数:', response_data)
        if response_data['code'] == 0:
            try:
                if response_data == []:
                    return ('暂无数据','None')
                else:
                    item = response_data['result'][0]
                    print('item:', item)
                    power_value = item['value'][1:-1]
                    power_data = '%.2f' % float(power_value)
                    power_time = time.strftime("%Y/%m/%d %H:%M", time.localtime(item['time']))
                    print('接口返回的功率瓦数为:', power_data)
                    print('接口返回的最新时间为:', power_time)
                    # 拿到接口数据之后将statistics_json_data中的数据置空，下次进来时依然可以拿最新数据
                    self.statistics_operation_json.clear_json_data()
                    return (power_data, power_time)
            except Exception:
                print(Exception)
        else:
            print('获取功率情况失败')


    def get_wireless_switch_status(self):
        request_data = self.rpc_operation_json.read_get_device_prop_request_data()
        print('请求参数:', request_data)
        method = request_data['method']
        print('请求方法为:' + method)
        assert method == 'get_device_prop', '请求方法错误'
        param = request_data['params'][1]
        print('param:', param)
        assert param == 'disable_btn0', '请求参数错误：预期参数：disable_btn0 实际参数：' + param
        for value in request_data['params']:
            print('params请求参数中带有' + value)

        response_data = self.rpc_operation_json.read_get_device_prop_response_data()
        print('返回参数:', response_data)
        try:
            result = response_data['result'][0]
            print('result:', result)
            print('获取到的转无线开关状态为:' + str(result))
        except Exception as e:
            print('没有获取到开关状态', e)



    def turn_wireless_switch_settings(self, is_open):
        data = self.rpc_operation_json.read_set_device_prop_request_data()
        print('请求参数:', data)
        method = data['method']
        print('请求方法为:' + method)
        assert method == 'set_device_prop', '请求方法错误'
        params = data['params']
        assert 'sid' in params.keys(), '请求参数中没有sid'
        assert 'disable_btn0' in params.keys(), '请求参数中没有disable_btn0'
        disable_btn0_status = params['disable_btn0']
        if is_open:
            assert disable_btn0_status == 0, '请求参数错误：预期参数：disable_btn0_status:0 实际参数：' + str(disable_btn0_status)
            print('成功发送关闭开关请求')
        else:
            assert disable_btn0_status == 1, '请求参数错误：预期参数：disable_btn0_status:1 实际参数：' + str(disable_btn0_status)
            print('成功发送打开开关请求')
        for key, value in params.items():
            print('请求参数:' + key, '参数值:' + str(value))

    def device_rename(self):
        request_data = self.device_rename_json.read_request_data()
        print('请求参数:', request_data)
        for key, value in request_data.items():
            print('请求参数:' + key, '参数值:' + str(value))
        response_data = self.device_rename_json.read_response_data()
        code = response_data['code']
        if code == 0:
            print('设备名修改成功,新修改的设备名称为:', request_data['newName'])

    '''定时首页校验设置的定时功能'''
    def checking_timing_set(self, timer_type,time_custom_type,start_time_str=None, end_time_str=None):
        request_data = self.scene_edit_json.read_timer_request_data()
        setting_data = request_data['setting']
        enable_timer_on = int(setting_data['enable_timer_on'])
        enable_timer_off = int(setting_data['enable_timer_off'])

        for key, value in setting_data.items():
            print('请求参数:' + key, '参数值:' + str(value))
        if timer_type == TIME_TYPE.time_on:
           assert enable_timer_on == 1,'定时开启enable_timer_on字段为1'
           assert enable_timer_off == 0, '定时关闭enable_timer_off字段为0'
        elif timer_type == TIME_TYPE.time_off:
            assert enable_timer_on == 0, '定时开启enable_timer_on字段为0'
            assert enable_timer_off== 1, '定时关闭enable_timer_off字段为1'
        else:
            assert enable_timer_on == 1, '定时开启enable_timer_on字段为1'
            assert enable_timer_off == 1, '定时关闭enable_timer_off字段为1'

        if start_time_str == None:
            if time_custom_type == TIME_CUSTOME_TYPE.once:
                assert self.get_on_off_once_time(end_time_str) in setting_data['off_time'], '定时关闭off_time参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_holidays:
                assert setting_data['on_filter'] == 'cn_freeday','法定节假日on_filter参数为cn_freeday'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '定时关闭off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.period_daily:
                assert setting_data['on_filter'] == '','每天on_filter参数为空'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '定时关闭off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_working_day:
                assert setting_data['on_filter'] == 'cn_workday','法定工作日on_filter参数为cn_workday'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '定时关闭off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.custom:
                assert self.get_custom_time(end_time_str) in setting_data['off_time'], '定时关闭off_time参数错误'
        elif end_time_str == None:
            if time_custom_type == TIME_CUSTOME_TYPE.once:
                assert self.get_on_off_once_time(start_time_str) in setting_data['on_time'], '定时开启on_time参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.period_daily:
                assert setting_data['on_filter'] == '','每天on_filter参数为空'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '定时开启on_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_working_day:
                assert setting_data['on_filter'] == 'cn_workday','法定工作日on_filter参数为cn_workday'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '定时开启on_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_holidays:
                assert setting_data['on_filter'] == 'cn_freeday','法定节假日on_filter参数为cn_freeday'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '定时开启on_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.custom:
                assert self.get_custom_time(start_time_str) in setting_data['on_time'], '定时开启on_time参数错误'
        else:
            if time_custom_type == TIME_CUSTOME_TYPE.once:
                assert self.get_on_off_once_time(start_time_str) in setting_data['on_time'], '时间段定时on_time请求参数错误'
                assert self.get_on_off_once_time(end_time_str) in setting_data['off_time'], '时间段定时off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_holidays:
                assert setting_data['on_filter'] == 'cn_freeday','法定节假日on_filter参数为cn_freeday'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '时间段定时on_time请求参数错误'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '时间段定时off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.period_daily:
                assert setting_data['on_filter'] == '','每天on_filter参数为空'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '时间段定时on_time请求参数错误'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '时间段定时off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.legal_working_day:
                assert setting_data['on_filter'] == 'cn_workday','法定工作日on_filter参数为cn_workday'
                assert self.get_on_off_daily_or_working_time(start_time_str) in setting_data['on_time'], '时间段定时on_time请求参数错误'
                assert self.get_on_off_daily_or_working_time(end_time_str) in setting_data['off_time'], '时间段定时off_time请求参数错误'
            if time_custom_type == TIME_CUSTOME_TYPE.custom:
                assert self.get_custom_time(start_time_str) in setting_data['on_time'], '时间段定时on_time请求参数错误'
                assert self.get_custom_time(end_time_str) in setting_data['off_time'], '时间段定时off_time请求参数错误'

    def get_on_off_once_time(self, time_str):
        if '明天' in time_str or '次日' in time_str:
            first_time = time.strftime('%d %m * %Y', time.localtime(time.time() + 24 * 60 * 60))
            time_str = time_str.split(' ')[1]
            hour = time_str.split(':')[0]
            minute = time_str.split(':')[1]
            hour_str = '0' if (hour == '00') else hour.lstrip('0')
            minute_str = '0' if (minute == '00') else minute.lstrip('0')
            time_content = '%s %s %s' % (minute_str, hour_str, first_time)
            print('请求时间参数应该为:',time_content)
            return time_content
        else:
            first_time = time.strftime('%d %m * %Y', time.localtime())
            hour = time_str.split(':')[0]
            minute = time_str.split(':')[1]
            hour_str = '0' if (hour == '00') else hour.lstrip('0')
            minute_str = '0' if (minute == '00') else minute.lstrip('0')
            time_content = '%s %s %s' % (minute_str, hour_str, first_time)
            print('请求时间参数应该为:',time_content)
            return time_content

    def get_on_off_daily_or_working_time(self,time_str):
        if '明天' in time_str:
            time_str = time_str.lstrip('明天 ')
        if '次日' in time_str:
            time_str = time_str.lstrip('次日 ')
        print(time_str)
        hour = time_str.split(':')[0]
        minute = time_str.split(':')[1]
        hour_str = '0' if (hour == '00') else hour.lstrip('0')
        minute_str = '0' if (minute == '00') else minute.lstrip('0')
        last_time_str = time.strftime('%Y', time.localtime())
        other_time_str = '* * 0,1,2,3,4,5,6'
        time_content = '%s %s %s %s' % (minute_str, hour_str, other_time_str,last_time_str)
        print('请求时间参数应该为:',time_content)
        return time_content


    def get_custom_time(self,time_str):
        if '明天' in time_str:
            time_str = time_str.lstrip('明天 ')
        if '次日' in time_str:
            time_str = time_str.lstrip('次日 ')
        print(time_str)
        hour = time_str.split(':')[0]
        minute = time_str.split(':')[1]
        hour_str = '0' if (hour == '00') else hour.lstrip('0')
        minute_str = '0' if (minute == '00') else minute.lstrip('0')
        last_time_str = time.strftime('%Y', time.localtime())
        other_time_str = '* * 0'
        time_content = '%s %s %s %s' % (minute_str, hour_str, other_time_str, last_time_str)
        print('请求时间参数应该为:', time_content)
        return time_content


if __name__ == '__main__':
    data = One_Button_Wall_Switch_Data()
    print(data.get_on_off_daily_or_working_time('明天 09:19'))
    # timer_type, time_custom_type, start_time_str = None, end_time_str = None
    # print(data.checking_timing_set(TIME_TYPE.time_on,TIME_CUSTOME_TYPE.once, start_time_str='明天 06:03'))

# 执行一次
# 20 56 9 27 11 * 2019
# 每天
# 46 51 09 * * 0,1,2,3,4,5,6 2019

# 法定工作日
# 19 55 09 * * 0,1,2,3,4,5,6 2019

# 法定节假日
# 21 54 9 * * 0,1,2,3,4,5,6 2019

# 自定义
# 15 58 12 * * 3 2019
# 16 59 13 * * 1,3 2019


