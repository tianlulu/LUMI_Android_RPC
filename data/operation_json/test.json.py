from data.operation_json.statistics_operation_json import Statistics_Operation_Json
import json
#from business.one_button_wall_switch_business import One_Button_Wall_Switch_Business
import time
class Teswwt:
    def __init__(self):
        self.statistics_operation_json  = Statistics_Operation_Json()

    def write_data(self):
        # self.statistics_operation_json.clear_json_data()
        # return self.statistics_operation_json.read_response_power_day_data()
        response_data = {"featchTemperatureHumidityPressure":[{"type":"success","requestTime":1575441230782,"params":[{"did":"254984411","siid":2,"piid":1},{"did":"254984411","siid":2,"piid":2},{"did":"254984411","siid":2,"piid":3}],"response":[{"did":"254984411","siid":2,"piid":1,"value":26.26,"code":0,"updateTime":1575440580203},{"did":"254984411","siid":2,"piid":2,"value":35.57,"code":0,"updateTime":1575440610068},{"did":"254984411","siid":2,"piid":3,"value":101.2,"code":0,"updateTime":1575434807306}],"responseTime":1575441231196},{"type":"success","requestTime":1575441234344,"params":[{"did":"254984411","siid":2,"piid":1},{"did":"254984411","siid":2,"piid":2},{"did":"254984411","siid":2,"piid":3}],"response":[{"did":"254984411","siid":2,"piid":1,"value":26.26,"code":0,"updateTime":1575440580203},{"did":"254984411","siid":2,"piid":2,"value":35.57,"code":0,"updateTime":1575440610068},{"did":"254984411","siid":2,"piid":3,"value":101.2,"code":0,"updateTime":1575434807306}],"responseTime":1575441234444}]}

        self.statistics_operation_json.test_write_data(data=response_data)

        # self.statistics_operation_json.get_response_data(json.loads(response_data),'stat_day_v3')
        # self.statistics_operation_json.write_response_data(response_data,'stat_week_v3')
        # if electricity_type:
        #     request_data = self.electricity_statistics_operation_json.read_response_day_data()
        # else:
        #     request_data = self.electricity_statistics_operation_json.read_response_month_data()
        # print('返回参数:',response_data)


        # response_data ={
        #     "code": 0,
        #     "message": "ok",
        #     "result": []
        # }
        #
        # print('返回参数:',response_data)
        # if response_data['code'] == 0:
        #     try:
        #         if response_data['result'] == []:
        #             data = '%.1f' % float(0)
        #             return data
        #         else:
        #             item = response_data['result'][0]
        #             print('item:', item)
        #             value = item['value'][1:-1]
        #             print('value:', value)
        #             data = '%.1f' % (int(value) / 1000)
        #         print('接口返回的电量度数为:', data)
        #         return data
        #     except Exception:
        #         print(Exception)
        # else:
        #     print('获取电量情况失败')


    def count_time(self,time_str):
        if '明天' in time_str or '次日' in time_str:
            first_time = time.strftime('%d %m * %Y' , time.localtime(time.time()+ 24*60*60))
            time_str = time_str.split(' ')[1]
            hour_str = time_str.split(':')[0]
            minute_str = time_str.split(':')[1]
            time_content =  '%s %s %s'  %(minute_str,hour_str,first_time)
            print(time_content)
        else:
            first_time = time.strftime('%d %m * %Y' , time.localtime())
            hour_str = time_str.split(':')[0]
            minute_str = time_str.split(':')[1]
            time_content = '%s %s %s' % (minute_str, hour_str, first_time)
            print(time_content)



if __name__ == '__main__':
    test = Teswwt()
    test.write_data()
    # test.count_time('14:24')

