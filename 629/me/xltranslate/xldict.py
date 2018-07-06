from tkinter import Tk,Button,Entry,Label,Text,END
import time
import random
import hashlib
import urllib
import urllib.request
import urllib.parse
import json

#Python GUI编程  Python 提供了多个图形开发界面的库
#Tkinter： Tkinter 模块(Tk 接口)

class xldict_class:
    def __init__(self):
        self.url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    def xl_translate(self,word):
        headers = {
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/?keyfrom=tegg.index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'

        }


        timestamp = int(time.time() * 1000) + random.randint(0, 10)
        S = 'fanyideskweb'
        n = word
        r = str(timestamp)
        D = "ebSeFb%=XZ%T[KZ)c(sy!"
        signd = hashlib.md5((S + n + r + D).encode('utf-8')).hexdigest()

        data_form = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': timestamp,
            'sign': signd,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }
        mydata = urllib.parse.urlencode(data_form).encode('utf-8')
        request = urllib.request.Request(url=self.url, data=mydata, headers=headers)
        response = urllib.request.urlopen(request)
        res = response.read().decode('utf-8')  # 返回str
        # 将字符串res转换成dict
        res_dict = json.loads(res)
        # 将字典值取出
        translateResult = res_dict['translateResult'][0][0]["tgt"]
        return translateResult


class Application(object):
    def __init__(self):
        self.xl = xldict_class()


        # 1.定义窗口
        self.window = Tk()
        # 窗口默认宽高和初始化坐标值
        self.window.geometry("280x350+600+300")


        # 2.窗口标题
        self.window.title(u'xl翻译')

        # 3.输入框（参数是父窗口）
        self.entry = Entry(self.window)
        # 输入框设置(x,y起始位置，kuangao)
        self.entry.place(x=10, y=10, width=200, height=25)

        # 4.查询按钮
        self.submit_btn = Button(self.window, text=u'查询', command=self.submit)  # 绑定函数执行
        self.submit_btn.place(x=220, y=10, width=50, height=25)

        # 5.翻译结果字段
        self.title_label = Label(self.window, text='翻译结果：')
        # y=10+25+20
        self.title_label.place(x=10, y=55)

        # 6.文本域添加背景颜色
        self.reslut_text = Text(self.window, background='#F5F5DC')
        self.reslut_text.place(x=10, y=75, width=260, height=265)

    def run(self):
        self.window.mainloop()

    # 查询事件
    def submit(self):
        # 1.从输入框中获取用户输入内容
        content = self.entry.get()

        #2.把内容传给有道服务器
        translateResult = self.xl.xl_translate(content)#返回的是翻译后的结果

        #2.将结果插入到翻译结果文本域内(设置插入位置)
        self.reslut_text.delete(1.0,END)

        self.reslut_text.insert(END,translateResult)

        #将内容传到url，获取响应结果打印到
        print(content)


if __name__ == '__main__':
    app = Application()
    app.run()

