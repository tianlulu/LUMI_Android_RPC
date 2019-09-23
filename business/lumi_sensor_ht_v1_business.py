#coding=utf8
from handle.lumi_sensor_ht_v1_handle import Sensor_Ht_V1_Handle
class Sensor_Ht_V1_Business:
    def __init__(self,i):
        self.sensor_ht_v1_handle = Sensor_Ht_V1_Handle(i)


    def click_temperature(self):
        self.sensor_ht_v1_handle.click_temperature_element()


    def click_humidity(self):
        self.sensor_ht_v1_handle.click_humidity_element()

    def click_use_back(self):
        self.sensor_ht_v1_handle.click_use_back_element()








