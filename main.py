from DrissionPage import Chromium
import sys


tab = Chromium().latest_tab
cookies="PHPSESSID=7lmrlred0bc04kpl21j4r9i8f3; PTCMS_history=21360%2C98080; PTCMS_comeurl=%2F; PTCMS_userid=39023; PTCMS_username=1033652712%40qq.com; PTCMS_usernames=%E5%90%AC%E5%8F%8B_28222; PTCMS_token=06061e4a35432ebc033907adb3cfb380; PTCMS_logintime=1730558324"
tab.set.cookies(cookies.encode('utf-8').decode(sys.stdout.encoding))

# tab.listen.start('m.ting13.cc/api/mapi/play')  # 开始监听，指定获取包含该文本的数据包
tab.listen.start('mp3m.ysxs.top/' , method=('POST'))  # 开始监听，指定获取包含该文本的数据包
tab.get('https://m.ting13.cc/play/21360_1_98080.html')  # 访问网址，这行产生的数据包不监听


# res = tab.listen.wait()  # 等待并获取一个数据包
# print(res.url)  # 打印数据包url
# print(res)


res = tab.listen.wait()  # 等待并获取一个数据包
print(res.url)  # 打印数据包url


# for _ in range(5):
    # tab('@rel=next').click()  # 点击下一页
    # res = tab.listen.wait()  # 等待并获取一个数据包
    # print(res.url)  # 打印数据包url