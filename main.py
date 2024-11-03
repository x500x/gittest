#coding=utf-8
from DrissionPage import Chromium
import sys, locale


tab = Chromium().latest_tab
cookies="domain=m.ting13.cc;PHPSESSID=91drha7467okr72hb7jh946bf5; PTCMS_comeurl=%2F; PTCMS_userid=39023; PTCMS_username=1033652712%40qq.com; PTCMS_usernames=%E5%90%AC%E5%8F%8B_28222; PTCMS_token=7e372fc4e01597a6dfc75ffaeba49899; PTCMS_logintime=1730608518"

tab.set.cookies(cookies)
# tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包

#tab.get('https://m.ting13.cc/play/21360_1_98080.html')  # 访问网址，这行产生的数据包不监听



tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包
tab.get('https://m.ting13.cc/play/21360_1_98080.html')
# res = tab.listen.wait()  # 等待并获取一个数据包
# print(res.url)  # 打印数据包url
# print(res)

# tab.listen.wait_silent(timeout=60*3)
#for res in tab.listen.steps(timeout=60*3):
for res in tab.listen.steps(timeout=60):
# res = tab.listen.wait(timeout=60)  # 等待并获取一个数据包
    print(res.url)  # 打印数据包url
    print(res.response.status)
    # print(res.response.headers)
    print(res.response.body)
    print(res.response.raw_body)
    
    print(res.request.url)
    print(res.request.method)
    print(res.request.headers)
    print(res.request.postData)
    params="nid=21360&cid=98080&sort=read"

    url="https://m.ting13.cc/api/mapi/play"
    
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      'Accept': "application/json, text/javascript, */*; q=0.01",
      'Accept-Encoding': "gzip, deflate",
      'sp': res.request.headers['sp'],
      'x-requested-with': "XMLHttpRequest",
      'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
      'sc': res.request.headers['sc'],
      'origin': res.request.headers['origin'],
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': res.request.headers['Referer'],
      'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
      'Cookie': res.request.headers['cookie']
    }
    
    response = requests.post(url, params=params, headers=headers)
    
    print(response.text)
# for _ in range(5):
    # tab('@rel=next').click()  # 点击下一页
    # res = tab.listen.wait()  # 等待并获取一个数据包
    # print(res.url)  # 打印数据包url