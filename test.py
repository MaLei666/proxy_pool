# -*- coding: utf-8 -*-

from Schedule import ProxyRefreshSchedule
import requests
def get_proxy():
    return requests.get("http://111.207.68.150:8001/get/").content

def delete_proxy(proxy):
    requests.get("http://111.207.68.150:8001/delete/?proxy={}".format(proxy))

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None