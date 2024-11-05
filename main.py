#coding=utf-8
from DrissionPage import Chromium
import requests
import json
import time
import sys
# import re


tab = Chromium().latest_tab
cookies="domain=m.ting13.cc;PHPSESSID=91drha7467okr72hb7jh946bf5; PTCMS_history=19170%2C95267%7C21360%2C98080; PTCMS_comeurl=%2F; PTCMS_userid=39023; PTCMS_username=1033652712%40qq.com; PTCMS_usernames=%E5%90%AC%E5%8F%8B_28222; PTCMS_token=6690e87104404eb5c923c6a3e50947a6; PTCMS_logintime=1730780762"

tab.set.cookies(cookies)
# tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包

#tab.get('https://m.ting13.cc/play/21360_1_98080.html')  # 访问网址，这行产生的数据包不监听

cid=98081

i=0
# Time=time.time()
# flag=-1

tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包
tab.get(f"https://m.ting13.cc/play/21360_1_{cid}.html")
cid+=1
# res = tab.listen.wait()  # 等待并获取一个数据包
# print(res.url)  # 打印数据包url
# print(res)

# tab.listen.wait_silent(timeout=60*3)
#for res in tab.listen.steps(timeout=60*3):
for packet in tab.listen.steps(timeout=30):
    if cid>98091: break
    tab.get(f"https://m.ting13.cc/play/21360_1_{cid}.html")
    cid+=1
    # while time.time()-Time>=5:
        # Time=time.time()
        # tab.get(f"https://m.ting13.cc/play/21360_1_{cid}.html")
        # cid+=1
        # flag=-1
    # else:
        # flag=1
# res = tab.listen.wait(timeout=60)  # 等待并获取一个数据包
    print(packet.url)  # 打印数据包url
    print(packet.response.status)
    # print(res.response.headers)
    # print(res.response.body)
    # print(res.response.raw_body)
    
    # print(res.request.url)
    print(packet.request.method)
    # print(res.request.headers)
    print(packet.request.postData)
    
    url="https://m.ting13.cc/api/mapi/play"
    
    rheardes=packet.request.headers
    
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      'Accept': "application/json, text/javascript, */*; q=0.01",
      'Accept-Encoding': "gzip, deflate",
      'sp': rheardes['sp'],
      'x-requested-with': "XMLHttpRequest",
      'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
      'sc': rheardes['sc'],
      'origin': rheardes['origin'],
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': rheardes['Referer'],
      'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
      'Cookie': rheardes['cookie']
    }
    
    response = requests.post(url, params=packet.request.postData, headers=headers)
    
    print(response.text)
    
    res=response.text.encode('utf-8').decode("unicode_escape").replace("\\","")
    jresponse=json.loads(res)
    while jresponse['status']==300:
        time.sleep(1)
        response = requests.post(url, params=packet.request.postData, headers=headers)
        res=response.text.encode('utf-8').decode("unicode_escape").replace("\\","")
        jresponse=json.loads(res)
        i+=i
        if i>10:
            print("i>10,exiting");
            sys.exit()
    # with open('C:\\info.txt', 'a',encoding="utf-8") as f:
    i=0
    with open('C:\\info.txt', 'a',encoding="utf-8") as f:
        # f.write(jresponse['name'].encode('utf-8').decode("unicode_escape").replace("\\",""))
        # f.write('\n')
        # f.write(jresponse['url'].encode('utf-8').decode("unicode_escape").replace("\\",""))
        # f.write('\n')
        f.write(jresponse['name'])
        f.write('\n')
        f.write(jresponse['url'])
        f.write('\n')
        # f.write('\n')
        # f.write(response.text.encode('utf-8').decode("unicode_escape").replace("\\",""))
            # json.dump(jresponse, f)
        # f.write('\n')
        # text=re.sub(r"/","",response.text.encode('unicode_escape').decode("unicode_escape"))
    # if flag>0:
        # flag=-flag
        # while time.time()-Time<5: pass
        # Time=time.time()
        # tab.get(f"https://m.ting13.cc/play/21360_1_{cid}.html")
        # cid+=1
            
        # f.write(text)
        # f.write('\n')
        # json.dump(jresponse['name'].encode('utf-8').decode('utf-8'), f)
        # json.dump(jresponse['url'].encode('utf-8').decode('utf-8'), f)
        # f.write('\n')
        # print(jresponse,file=f)
    
    
    
    
    
# for _ in range(5):
    # tab('@rel=next').click()  # 点击下一页
    # res = tab.listen.wait()  # 等待并获取一个数据包
    # print(res.url)  # 打印数据包url