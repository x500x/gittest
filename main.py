from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听

tab.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
for _ in range(5):
    tab('@rel=next').click()  # 点击下一页
    res = tab.listen.wait()  # 等待并获取一个数据包
    print(res.url)  # 打印数据包url