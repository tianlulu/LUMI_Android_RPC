import json
class Electricity_Statistics_Operation_Json:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  './json_data/electricity_statistics_json_data.json'
        else:
            self.file_path = file_path
        self.json_data = {}

    def read_request_day_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['request_day_data:']
            return request_data


    def read_request_month_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['request_month_data:']
            return request_data


    def read_response_day_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['response_day_data:']
            return response_data

    def read_response_month_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['response_month_data:']
            return response_data


    # stat_type: 电量类型：当日用电/当月用电
    def get_request_data(self,data,stat_type):
        try:
            if stat_type == 'stat_day':
                self.json_data.update({"request_day_data:": data})
            if stat_type == 'stat_month':
                self.json_data.update({"request_month_data:": data})
        except Exception:
            return data


    # stat_type:电量类型：当日用电/当月用电
    def get_response_data(self,data,stat_type):
        try:
            if stat_type == 'stat_day':
                self.json_data.update({"response_day_data:": data})
            if stat_type == 'stat_month':
                self.json_data.update({"response_month_data:": data})
            self.write_data()
        except Exception:
            return data


    def write_data(self):
        with open(self.file_path, 'w') as fp:
            json.dump(self.json_data, fp, ensure_ascii=False, indent=4)











