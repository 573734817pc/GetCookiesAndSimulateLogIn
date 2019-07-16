#这是模拟登陆配置页
#首先导入我们想要继承的类
from SimulateLogInLib import SimulateLogIn
from SimulateLogInLib import GetCookieStr
#这里我们采用多继承的方式继承上面两个类
class SimulateLogInConf(SimulateLogIn.SimulateLogIn, GetCookieStr.GetCookieStr):
    def simulate_login_conf(self):
        # 默认编码
        self.encoding = 'utf8'
        #登录页
        self.loginUrl = 'https://www.yahoo.com'
        #登录名
        self.userName = 'bjzf****11'
        #登录密码
        self.passWord = 'Zf****34'
        # 浏览器登录后得到的cookie，也就是刚才复制的字符串
        cookies_str = self.get_cookie_str()
        self.cookie_str = cookies_str
        # 想要访问的目标网页
        self.url = 'https://mail.yahoo.com'
        # User-Agent
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        #运行login方法
        self.simulate_login()
