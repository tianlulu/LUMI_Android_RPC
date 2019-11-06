from mitmproxy import ctx
from urllib.parse import unquote
import json
from operation_json.rpc_operation_json import RPC_Operation_Json
from operation_json.electricity_statistics_operation_json import Electricity_Statistics_Operation_Json

class Write_Interface_Data:
    def __init__(self):
        self.rpc_path = '/app/home/rpc/'
        self.electricity_statistics_path = '/v2/user/statistics'
        self.rpc_operation_json = RPC_Operation_Json()
        self.electricity_statistics_operation_json = Electricity_Statistics_Operation_Json()

    def transcoding(self,flow, ctx):
        if 'POST' == str(flow.request.method):
            ctx.log.warn(str(flow.request.url))
            ctx.log.warn(str(flow.request.host))
            ctx.log.warn(str(flow.request.path))
            ctx.log.alert('rpc转码前')
            ctx.log.info(str(flow.request.get_text()))
        data = unquote(str(flow.request.get_text()))
        ctx.log.alert('rpc转码后')
        ctx.log.warn(data)
        return data


    def deal_with_data(self,flow, json_data):
        if self.rpc_path in flow.request.path:
            self.rpc_operation_json.write_request_data(json_data)
        if self.electricity_statistics_path in flow.request.path:
            self.electricity_type = json_data['data_type']
            ctx.log.info(self.electricity_type)
            self.electricity_statistics_operation_json.get_request_data(json_data, self.electricity_type)
        ctx.log.warn(str(json_data.keys()))
        ctx.log.warn(str(json_data.values()))


    def request(self,flow):
        if self.rpc_path in flow.request.path or self.electricity_statistics_path in flow.request.path:
            content = self.transcoding(flow, ctx)
            data = content.split('&')
            for item in data:
                kv = str(item)
                kv_list = kv.split('=')
                str_con = 'key:' + str(kv_list[0]) + ',value:' + str(kv_list[1])
                ctx.log.info(str_con)
                if str(kv_list[0]) == 'data':
                    json_data = json.loads(kv_list[1])
                    ctx.log.alert('oh ～ 拿到了最终需要的json')
                    ctx.log.error((kv_list[1]))
                    self.deal_with_data(flow, json_data)


    def response(self,flow):
        if self.rpc_path in flow.request.path:
            ctx.log.alert('获取返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.rpc_operation_json.write_response_data(json.loads(content))
        if self.electricity_statistics_path in flow.request.path:
            ctx.log.alert('获取返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.electricity_statistics_operation_json.get_response_data(json.loads(content),self.electricity_type)



addons = [
    Write_Interface_Data()
]
