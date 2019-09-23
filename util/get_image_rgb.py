import os
import time
from PIL import Image

class ImageRGBD:
    '''
    保存截图到screenshots文件夹下
    '''
    def get_screenshot_path(self):
        # 获取当前项目的根路径
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) + '//screenshots'
        time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_save_path = img_folder + time_str + '.png'
        return screen_save_path

    '''
    获取截图中的单个元素中心位置的rgba值
    '''
    def get_element_rgb(self,element,screen_shot_path):
        # 使用PIL打开该图片
        image = Image.open(screen_shot_path)
        # width,height = image.size
        # print('image.size:',width,height)

        # top_element = self.european_standard_page.get_top_group_view_element()
        x = element.location['x']
        y = element.location['y']
        w = element.size['width']
        h = element.size['height']
        # print('top_element坐标:',x,y,w,h)

        top_image = image.crop(box = (x, y, x+w, y+h))
        # print('top_image_size:',x, y, x+w, y+h)
        # print('top_image:',top_image.size)

        top_rgba = top_image.getpixel((top_image.size[0]/2, top_image.size[1]/2))
        return top_rgba


    '''
    获取截图中的模块多个元素中心位置的rgba值
    '''
    def get_elements_rgb(self):
        pass



