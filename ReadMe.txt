1�����ܣ�����һ��ģ���û�����������¼�˻��������cookiesƴ���ַ�����Ȼ����Я��cookie���з�������ҳ��Ĳ����
	��������������������������ѻ��ʣ����Ҷ��Ѿ�ģ���û���¼�ˣ����ҾͿ��Լ���ģ���û�����¼���������ҳ�氡����Ϊʲô������ҪЯ��cookiesȥ��������ҳ���أ��ѽ⣡������
	����������΢����һ�£���������Ŀ�Ĳ��Ǵﵽĳ�ֹ��ܣ�����ͨ�����������ǿ������������Ҫ�Ĺ��ܣ�����˵��ȡ����֮��ġ�������ȫ���Ը�дһ�²���������������Ĺ��ܣ�
	���ȣ�ģ���û���¼�����cookies��Ȼ��cookies�浽���ݿ⣨�����κ�����Ҫ��ĵط�����Ȼ����һ������Ҫ��ȡ��¼�û����ݵ�ʱ��ֻ��Ҫȥ���ݿ��ѯ��Ӧcookie���ɣ��������ȡ����
	�Ĺ����У�����cookieʧЧ��������һ��ģ���û���¼����ȡcookies��
	��
2���ò������python������ʹ�õ���selenium��chrome webdriver�������headless�������в�����ͬѧ�����Է���һ����ַ��https://www.cnblogs.com/573734817pc/p/11176815.html��
3��ʹ�õ�ʱ��ֻ��Ҫ���ú�SimulateLogInConf�ļ����ɡ�
����demo���£���¼yahoo���䣩��
	# Ĭ�ϱ���
        self.encoding = 'utf8'
        #��¼ҳ
        self.loginUrl = 'https://www.yahoo.com'
        #��¼��
        self.userName = 'bj****1111'
        #��¼����
        self.passWord = 'Zf****34'
        # �������¼��õ���cookie��Ҳ���ǸղŸ��Ƶ��ַ���
        cookies_str = self.get_cookie_str()
        self.cookie_str = cookies_str
        # ��Ҫ���ʵ�Ŀ����ҳ
        self.url = 'https://mail.yahoo.com'
        # User-Agent
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        #����login����
        self.simulate_login()


