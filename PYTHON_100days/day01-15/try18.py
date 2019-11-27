from time import time
from threading import Thread
import requests

# 继承thread类创建自定义的线程类
class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url
    def run(self):
        filename = self._url[self._url.rfind('/') + 1: ]
        resp = requests.get(self._url)
        with open('./News/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=7adf9ab5c720adfec0bc3abb5e5b42a1&num=10')
    # 将服务器返回的JSON格式的数据解析成字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()