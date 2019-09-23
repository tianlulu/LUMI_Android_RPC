import json
import time
class OperationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  '../util/rpc_data.json'
        else:
            self.file_path = file_path

    '''
    读取json文件
    '''
    def read_data(self):
        time.sleep(2)
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    '''
    写入json文件
    '''
    def write_data(self,data):
        with open(self.file_path,'w') as  fp:
            data = json.dump(data, fp, ensure_ascii=False, indent=4)
            return data






