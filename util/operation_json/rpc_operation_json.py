import json

class RPC_Operation_Json:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path =  './json_data/rpc_json_data.json'
        else:
            self.file_path = file_path
        self.json_data = {}


    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def read_request_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            request_data = data['request_data:']
            return request_data

    def read_response_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            response_data = data['response_data:']
            return response_data

    def write_request_data(self,data):
        with open(self.file_path,'w') as  fp:
            # data = data.update({"request_data":data})
            # request_data = {"request_data": data}
            self.json_data.update({"request_data:": data})
            # print(self.json_data)
            # data = json.dump(self.json_data, fp, ensure_ascii=False, indent=4)
            return data

    def write_response_data(self,data):
        with open(self.file_path,'w') as fp:
            # response_data = {"response_data":data}
            self.json_data.update({"response_data:": data})
            json.dump(self.json_data, fp, ensure_ascii=False, indent=4)
            # print("data:",data)
            return data














