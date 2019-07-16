import logging
import time
class Base(object):
    # 定义构造函数，定义各种属性和logging类的配置
    def __init__(self):
        #默认编码
        self.encoding = ''
        #浏览器登录后得到的cookie，也就是刚才复制的字符串
        self.cookie_str = ''
        #登录后才能访问的网页
        self.url = ''
        #登录页面
        self.loginUrl = ''
        #登录名
        self.userName = ''
        #登录密码
        self.passWord = ''
        #User-Agent
        self.user_agent = ''

        logging.basicConfig(level=logging.WARNING,  # 控制台打印的日志级别 DEBUG WARNING
                            filename='./log/' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log',
                            filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                            # a是追加模式，默认如果不写的话，就是追加模式
                            format=
                            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                            # 日志格式
                            )