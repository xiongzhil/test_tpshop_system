import time
import unittest
from script.test_tpshop_loin import TestTpshopLogin
from HTMLTestRunner_PY3 import HTMLTestRunner
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestTpshopLogin))
# 定义测试报告的路径和名称
report = "./report/tpshop{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
with open(report, "wb")as f:
    # 初始化runner
    runner = HTMLTestRunner(f,verbosity=1, description="这是一个测试报告", title="tpshop报告")
    # 使用runner运行测试套件，生成测试报告
    runner.run(suite)
