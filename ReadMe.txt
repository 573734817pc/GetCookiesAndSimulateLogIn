1、功能：这是一个模拟用户点击和输入登录账户，并获得cookies拼接字符串，然后再携带cookie进行访问其它页面的插件。
	（看到上面的描述，可能有朋友会问：“我都已经模拟用户登录了，那我就可以继续模拟用户点击事件访问其它页面啊！那为什么我有又要携带cookies去访问其它页面呢？费解！！！”
	在这里我稍微解释一下，这个插件的目的不是达到某种功能，而是通过这个插件我们可以完成我们想要的功能，比如说爬取数据之类的。我们完全可以改写一下插件，将其变成这样的功能：
	首先，模拟用户登录并获得cookies，然后将cookies存到数据库（或者任何你想要存的地方），然后下一次你想要爬取登录用户数据的时候，只需要去数据库查询相应cookie即可，如果在爬取数据
	的过程中，发现cookie失效，可以再一次模拟用户登录并获取cookies。
	）
2、该插件基于python开发，使用到了selenium（chrome webdriver）插件的headless技术（有不懂的同学，可以访问一下网址：https://www.cnblogs.com/573734817pc/p/11176815.html）
3、使用的时候只需要配置好SimulateLogInConf文件即可。
配置demo如下（登录yahoo邮箱）：
	# 默认编码
        self.encoding = 'utf8'
        #登录页
        self.loginUrl = 'https://www.yahoo.com'
        #登录名
        self.userName = 'bj****1111'
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


