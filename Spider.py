# date 2020-2-5 19:30:51
# version 1.0


import requests
import re

# 创建类
class beautypic():
    def __init__(self):
        # 定义session 加载HTML
        self.session = requests.session()
        # 爬取网址
        self.url = "https://www.mzitu.com/best/"
        # 模拟浏览器，防反
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Referer": "https://www.mzitu.com/best/"
        }

    def scrapy_(self):
        # 获取爬取结果
        scrapy_response = self.session.get(self.url, headers=self.headers)
        # 正则表达式 .*贪婪  ？停止贪婪
        image_infos = re.findall(
            "data-original='(.*)' alt='(.*?)'", scrapy_response.text)
        save_path = "E:/桌面/Python/spider_test2/image/"
        # 以‘url’，‘name’的格式下载文件
        for image_url, name in image_infos:
            print(image_url, name)
            image_content = requests.get(
                image_url, headers=self.headers).content
            with open(save_path + name + ".jpg", "wb") as f:
                f.write(image_content)


beautypic = beautypic()
beautypic.beautypic_()
