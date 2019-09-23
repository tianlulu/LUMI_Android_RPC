# import demo.counter as counter
# import demo.joker  as  joker
#
# addons = [
#     counter.Counter(),
#     joker.Joker(),
# ]

import mitmproxy.http
from mitmproxy import ctx, http
from urllib.parse import unquote
import json
from operation_json import OperationJson

def request(flow):
    ctx.log.info(str(flow.request.get_text()))
    # host = 'pv.api.io.mi.com'
    path = '/app/home/rpc/'

    # if host not in flow.request.host:
    #     return

    if  path not in flow.request.path:
        return

    operation_json = OperationJson()
    if path in flow.request.path:
        if 'POST' == str(flow.request.method):
            ctx.log.warn(str(flow.request.url))
            ctx.log.warn(str(flow.request.host))
            ctx.log.warn(str(flow.request.path))
            ctx.log.alert('转码前')
            ctx.log.info(str(flow.request.get_text()))

        content=unquote(str(flow.request.get_text()))
        ctx.log.alert('转码后')
        ctx.log.warn(content)

        ctx.log.alert('遍历post的body值 start=========================================')
        data=content.split('&')
        for item in data:
            kv=str(item)
            # ctx.log.error(kv)
            kv_list=kv.split('=')
            str_con='key:'+str(kv_list[0])+',value:'+str(kv_list[1])
            ctx.log.warn(str_con)

            if str(kv_list[0]) == 'data':
                json_data=json.loads(kv_list[1])
                ctx.log.alert('oh ～ 拿到了最终需要的json')
                # ctx.log.info(str(json_data))
                ctx.log.error((kv_list[1]))
                operation_json.write_data(json_data)
                # ctx.log.warn(json_data.type())
                # ctx.log.warn(json.loads(json_data))
                # ctx.log.warn(json.loads(json_data).type())
                # ctx.log.warn(str(json_data.keys()))
                # ctx.log.warn(str(json_data.values()))
        ctx.log.alert('遍历post的body值 end=========================================')


def response(flow):
    path = '/app/home/rpc/'
    if path in flow.request.path:
        ctx.log.alert(str(flow.response.status_code))
        ctx.log.alert(str(flow.response.text))


