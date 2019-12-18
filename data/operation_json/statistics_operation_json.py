import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import time
import json

class Statistics_Operation_Json:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC/data/json_data/statistics_json_data.json'
        else:
            self.file_path = file_path
        self.json_data = {}


    # is_update_json_data = False
    # def set_data_is_update(self,is_update):
    #     global is_update_json_data
    #     is_update_json_data = is_update
    #     return is_update_json_data
    #
    # def get_data_is_update(self):
    #     try:
    #         return is_update_json_data
    #     except Exception:
    #         return False


    def read_request_electricity_day_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['request_day_data']
            return request_data

    def read_request_electricity_month_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['request_month_data']
            return request_data

    def read_request_power_day_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            if 'request_power_day_data' in data.keys():
                request_data = data['request_power_day_data']
                return request_data
            else:
                return None


    def read_request_power_week_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            if 'request_power_week_data' in data.keys():
                request_data = data['request_power_week_data']
                return request_data
            else:
                return None


    def read_response_electricity_day_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['response_day_data']
            return response_data


    def read_response_electricity_month_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['response_month_data']
            return response_data


    def read_response_power_day_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            if 'response_power_day_data' in data.keys():
                response_data = data['response_power_day_data']
                return response_data
            else:
                print('none')
                return None


    def read_response_power_week_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            if 'response_power_week_data' in data.keys():
                response_data = data['response_power_week_data']
                return response_data
            else:
                return None


    # stat_type: 电量类型：当日用电/当月用电
    def get_request_data(self,data,stat_type):
        print('get_request_data*************************************',stat_type)
        try:
            if stat_type == 'stat_day':
                self.json_data.update({"request_day_data": data})
            if stat_type == 'stat_month':
                self.json_data.update({"request_month_data": data})
            if stat_type == 'stat_day_v3':
                if self.read_request_power_day_data() == None:
                    print('request_power_day_data==========================', data)
                    self.json_data.update({"request_power_day_data":data})
            if stat_type ==  'stat_week_v3':
                if self.read_request_power_week_data() == None:
                    print('request_power_week_data==========================', data)
                    self.json_data.update({"request_power_week_data":data})
        except Exception:
            return data


    # stat_type:电量类型：当日用电/当月用电
    def write_response_data(self,data,stat_type):
        print('get_response_data*************************************', stat_type)
        try:
            if stat_type == 'stat_day':
                self.json_data.update({"response_day_data": data})
            if stat_type == 'stat_month':
                self.json_data.update({"response_month_data": data})
            if stat_type == 'stat_day_v3':
                if self.read_response_power_day_data() == None:
                    print('response_power_day_data====================================================================')
                    self.json_data.update({"response_power_day_data": data})
            if stat_type == 'stat_week_v3':
                if self.read_response_power_week_data() == None:
                    print('response_power_week_data====================================================================')
                    self.json_data.update({"response_power_week_data": data})
            self.write_data()
        except Exception:
            return data


    def write_data(self):
        with open(self.file_path, 'w') as fp:
            json.dump(self.json_data, fp, ensure_ascii=False, indent=4)


    def clear_json_data(self):
        self.json_data = {}
        with open(self.file_path,'w') as fp:
            json.dump(self.json_data,fp,ensure_ascii=False,indent=4)

    def test_write_data(self,data):
        with open(self.file_path, 'w') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)








