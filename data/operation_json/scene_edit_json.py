import os
import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
import json
import time

class Scene_Edit_Json:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  '/Users/lumi/Documents/items/MIOT/Appium_Android_RPC/data/json_data/scene_edit_data.json'
        else:
            self.file_path = file_path
        self.json_data = {}


    def read_timer_request_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['timer_request_data']
            return response_data


    def read_timer_response_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['timer_response_data']
            return response_data


    def get_timer_request_data(self,data):
        try:
            self.json_data.update({"timer_request_data": data})
        except Exception:
            return data

    def write_timer_response_data(self,data):
        try:
            self.json_data.update({"timer_response_data": data})
            self.write_data()
        except Exception:
            return data


    def write_data(self):
        with open(self.file_path, 'w') as fp:
            json.dump(self.json_data, fp, ensure_ascii=False, indent=4)









