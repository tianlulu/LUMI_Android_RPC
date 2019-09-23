class My_Custom_Name:
    model_name = ""
    european_standard_device_name = ""
    european_standard_room_name = ""
    sensor_ht_v1_device_name = ""
    sensor_ht_v1_room_name = ""

    def set_european_standard_device_name(self,custom_device_name):
        global european_standard_device_name
        european_standard_device_name = custom_device_name
        return european_standard_device_name


    def set_european_standard_room_name(self,custom_room_name):
        global european_standard_room_name
        european_standard_room_name = custom_room_name
        return european_standard_room_name

    def set_sensor_ht_v1_device_name(self,custom_device_name):
        global sensor_ht_v1_device_name
        sensor_ht_v1_device_name = custom_device_name
        return sensor_ht_v1_device_name

    def set_sensor_ht_v1_room_name(self,custom_room_name):
        global sensor_ht_v1_room_name
        sensor_ht_v1_room_name = custom_room_name
        return sensor_ht_v1_room_name

    def set_model_name(self,model_key):
        global model_name
        model_name = model_key
        return model_name


    def get_european_standard_device_name(self):
        # print('得到的欧标插座设备名称:',european_standard_device_name)
        try:
            return european_standard_device_name
        except Exception:
            return My_Custom_Name.european_standard_device_name


    def get_european_standard_room_name(self):
        # print('得到的欧标插座房间名称:', european_standard_room_name)
        try:
            return european_standard_room_name
        except Exception:
            return My_Custom_Name.european_standard_room_name


    def get_sensor_ht_v1_room_name(self):
        # print('得到的米家温湿度的房间名称:',sensor_ht_v1_room_name)
        try:
            return sensor_ht_v1_room_name
        except Exception:
            return My_Custom_Name.sensor_ht_v1_room_name


    def get_sensor_ht_v1_device_name(self):
        # print('得到的米家温湿度的设备名称:',sensor_ht_v1_device_name)
        try:
            return sensor_ht_v1_device_name
        except Exception:
            return My_Custom_Name.sensor_ht_v1_device_name


    def get_model_name(self):
        try:
            return model_name
        except Exception:
            return My_Custom_Name.model_name


if __name__ == '__main__':
    my_custom = My_Custom_Name()
    # my_custom.set_sensor_ht_v1_device_name('mmdddddmmm')
    # print(my_custom.get_sensor_ht_v1_device_name())
    my_custom.set_european_standard_room_name('helllo')
    print(my_custom.get_european_standard_room_name())







