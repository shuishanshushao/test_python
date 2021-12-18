import pytest

version = 25


# 特殊方法 自己手写
@pytest.mark.skipif(version >= 25, reason="00")
class TestDemo:

    # 开始方法
    def setup(self):
        print("开始")

    # 结束方法
    def teardown(self):
        print("结束")

    # 类开始方法
    def setup_class(self):
        print("类开始")

    # 类结束方法
    def teardown_class(self):
        print("类结束")

    def test_fun1(self):
        print("我是测试函数1")

    def test_fun2(self):
        print("我是测试函数2")


if __name__ == "__main__":
    pytest.main("-s", r"G:\web自动化\Po计算机-pytest\pytest\test_pytest0.py")