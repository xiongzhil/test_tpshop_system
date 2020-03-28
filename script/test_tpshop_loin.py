import unittest
import requests
from api.login import LoginApi

# 创建测试类
class TestTpshopLogin(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        # 实例化session
        self.session = requests.Session()
        # 定义获取验证码的url
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 定义登陆的url
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        # 实例化api中login.py中的LogiinApi类
        self.login_api = LoginApi()
    def tearDown(self):
        # 关闭session
        if self.session:
            self.session.close()

    # 测试登录成功
    def test01_login_success(self):
        # 发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session, url=self.verify_url)
        # 断言验证码
        self.assertEqual("image/png", response_verify.headers.get("Content-Type"))
        response_login = self.login_api.login(self.session, self.login_url,{"username": "15500000000",
                                                                                    "password": "123456",
                                                                                    "verify_code": "8888"},)
        print(response_login.json())
        # 断言tpshop登录响应数据：响应状态码，status，msg
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(1, response_login.json().get("status"))
        self.assertEqual("登陆成功", response_login.json().get("msg"))
    def test02_username_is_not_exists(self):
        # 发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session, self.verify_url)
        # 断言验证码
        self.assertEqual("image/png", response_verify.headers.get("Content-Type"))
        # 发送tpshop登录接口请求
        response_login = self.login_api.login(self.session,url=self.login_url,data={"username": "15500000111",
                                               "password": "123456",
                                               "verify_code": "8888"})
        # 输出tpshop登录的接口结果
        print(response_login.json())
        # 断言tpsho登录响应数据：响应状态码。status,msg
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-1, response_login.json().get("status"))
        self.assertEqual("账号不存在!",response_login.json().get("msg"))

    def test03_password_is_error(self):
        # 发送获取验证码接口请求
        response_verify = self.login_api.get_verify(self.session, url=self.verify_url)
        # 断言验证码
        self.assertEqual("image/png", response_verify.headers.get("Content-Type"))
        # 发送tpshop登录接口请求
        response_login = self.login_api.login(self.session, url=self.login_url, data={"username": "15500000000",
                                                    "password": "1234567",
                                                    "verify_code": "8888"})
        # 输出tpshop登录接口结果
        print(response_login.json())
        # 断言tpshop登录响数据：响应状态码， status， msg
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-2, response_login.json().get("status"))
        self.assertEqual("密码错误!", response_login.json().get("msg"))