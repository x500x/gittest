#coding=utf-8
from DrissionPage import Chromium
import sys, locale


tab = Chromium().latest_tab
cookies="PHPSESSID=91drha7467okr72hb7jh946bf5; PTCMS_comeurl=%2F; PTCMS_userid=39023; PTCMS_username=1033652712%40qq.com; PTCMS_usernames=%E5%90%AC%E5%8F%8B_28222; PTCMS_token=7e372fc4e01597a6dfc75ffaeba49899; PTCMS_logintime=1730608518"


# tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包

tab.get('https://m.ting13.cc/play/21360_1_98080.html')  # 访问网址，这行产生的数据包不监听
tab.set.cookies(cookies)


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
    print(res.response.headers)
    print(res.response.body)
    print(res.response.raw_body)
    

# for _ in range(5):
    # tab('@rel=next').click()  # 点击下一页
    # res = tab.listen.wait()  # 等待并获取一个数据包
    # print(res.url)  # 打印数据包url