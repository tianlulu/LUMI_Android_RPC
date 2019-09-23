from util.operation_json import OperationJson
import os,sys

class Test:
    def get_dict_data(self):
        tuple = ('xpath', "//*[contains(@text, '2升级版空调伴侣')]")
        print(tuple[1])

        # operation_json = OperationJson('../util/rpc_data.json')
        # data = operation_json.read_data()
        # print(data)
        # param_list = data['params'][0]
        # print(param_list[1])


        # print(data['method'])
        # print('method' in data.keys())
        # print(data['method'] == 'get_prop_plug')

        # param_values = data['params']
        # print(param_values)


        # for value in param_values:
        #     print(value)
        #     # for item in values:
        #     if ('channel_0' == value):
        #         print('yes')

        # {
        #         #     "id": 10,
        #         #     "method": "set_device_prop",
        #         #     "accessKey": "IOS00026747c5acafc2",
        #         #     "params": {
        #         #         "max_power": 2200,
        #         #         "sid": "lumi.4cf8cdf3c7463e2"
        #         #     }
        #         # }

        # {
        #     "id": 9356,
        #     "method": "set_device_prop",
        #     "params": {
        #         "sid": "lumi.4cf8cdf3c746423",
        #         "poweroff_memory": 0
        #     }
        # }
        #
        # data = operation_json.read_data()
        # print('请求参数:', data)
        # method = data['method']
        # print('method:' + method)
        # # self.assertTrue(method in data.values())
        # param_values = data['params']
        # print(param_values[0])
        # # self.assertTrue('max_power' == param_values[0])
        # # self.assertTrue('sid' == param_values[1])
        # for value in param_values:
        #     print('params中带有' + value + '参数')


if __name__ == '__main__':
    test = Test()
    test.get_dict_data()