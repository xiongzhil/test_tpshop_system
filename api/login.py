import requests

# 创建封装登录接口的测试类
class LoginApi:
    def __init__(self):
        self.session = requests.Session

    # 封装获取验证码接口
    def get_verify(self, session, url):
        response = session.get(url)
        return response
    # 封装登录接口
    def login(self, session, url, data):
        response_login = session.post(url, data=data)
        return response_login