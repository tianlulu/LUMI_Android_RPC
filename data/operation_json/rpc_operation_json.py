import os
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import json
import time
class RPC_Operation_Json:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC/data/json_data/rpc_json_data.json'
        else:
            self.file_path = file_path
        self.json_data = {}

    def read_set_device_prop_request_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['set_device_prop_request_data']
            return request_data

    def read_get_device_prop_request_data(self):
        time.sleep(3)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['get_device_prop_request_data']
            return request_data

    def read_get_device_prop_exp_request_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['get_device_prop_exp_request_data']
            return response_data


    def read_toggle_ctrl_neutral_request_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['toggle_ctrl_neutral_request_data']
            return response_data


    def read_set_device_prop_response_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['set_device_prop_response_data']
            return request_data


    def read_get_device_prop_response_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['get_device_prop_response_data']
            return request_data


    def read_get_device_prop_exp_response_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['get_device_prop_exp_response_data']
            return response_data

    def read_toggle_ctrl_neutral_response_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['toggle_ctrl_neutral_response_data']
            return response_data


    def get_request_data(self,data,request_method):
        try:
            if request_method == 'set_device_prop':
                self.json_data.update({"set_device_prop_request_data": data})
            if request_method == 'get_device_prop':
                self.json_data.update({"get_device_prop_request_data": data})
            if request_method == 'get_device_prop_exp':
                self.json_data.update({"get_device_prop_exp_request_data": data})
            if request_method == 'toggle_ctrl_neutral':
                self.json_data.update({"toggle_ctrl_neutral_request_data": data})
        except Exception:
            return data


    def write_response_data(self,data,request_method):
        try:
            if request_method == 'set_device_prop':
                self.json_data.update({"set_device_prop_response_data": data})
            if request_method == 'get_device_prop':
                self.json_data.update({"get_device_prop_response_data": data})
            if request_method == 'get_device_prop_exp':
                self.json_data.update({"get_device_prop_exp_response_data": data})
            if request_method == 'toggle_ctrl_neutral':
                self.json_data.update({"toggle_ctrl_neutral_response_data": data})
            self.write_data()
        except Exception:
            return data


    def write_data(self):
        with open(self.file_path, 'w') as fp:
            json.dump(self.json_data, fp, ensure_ascii=False, indent=4)









