import sys
sys.path.append('/Users/lumi/Documents/items/MIOT/Appium_Android_RPC')
from mitmproxy import ctx
from urllib.parse import unquote
import json
from data.operation_json.statistics_operation_json import Statistics_Operation_Json
from data.operation_json.rpc_operation_json import RPC_Operation_Json
from data.operation_json.device_rename_json import Device_Rename_Json
from data.operation_json.scene_edit_json import Scene_Edit_Json
from common.constant_enum import URL_PATH

class Write_Interface_Data:
    def __init__(self):
        self.rpc_operation_json = RPC_Operation_Json()
        self.statistics_operation_json = Statistics_Operation_Json()
        self.device_rename_json = Device_Rename_Json()
        self.scene_edit_json = Scene_Edit_Json()


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
        if URL_PATH.rpc in flow.request.path:
            self.request_method = json_data['method']
            self.rpc_operation_json.get_request_data(json_data,self.request_method)
        if URL_PATH.electricity_statistics in flow.request.path:
            self.electricity_or_power_type = json_data['data_type']
            ctx.log.info(self.electricity_or_power_type)
            self.statistics_operation_json.get_request_data(json_data, self.electricity_or_power_type)
        if URL_PATH.device_rename in flow.request.path:
            self.device_rename_json.get_request_data(json_data)
        if URL_PATH.scene in flow.request.path:
            self.scene_edit_json.get_timer_request_data(json_data)
        ctx.log.warn(str(json_data.keys()))
        ctx.log.warn(str(json_data.values()))


    def request(self,flow):
        if URL_PATH.rpc in flow.request.path or URL_PATH.electricity_statistics in flow.request.path or URL_PATH.scene in flow.request.path\
                or URL_PATH.device_rename in flow.request.path:
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
        if URL_PATH.rpc in flow.request.path:
            ctx.log.alert('获取RPC返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.rpc_operation_json.write_response_data(json.loads(content),self.request_method)
        if URL_PATH.electricity_statistics in flow.request.path:
            ctx.log.alert('获取电量功率返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.statistics_operation_json.write_response_data(json.loads(content), self.electricity_or_power_type)
        if URL_PATH.device_rename in flow.request.path:
            ctx.log.alert('获取重命名接口返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.device_rename_json.write_response_data(json.loads(content))
        if URL_PATH.scene in flow.request.path:
            ctx.log.alert('获取sence接口返回值=========================================')
            content = unquote(str(flow.response.text))
            ctx.log.warn(content)
            self.scene_edit_json.write_timer_response_data(json.loads(content))



addons = [
    Write_Interface_Data()
]
