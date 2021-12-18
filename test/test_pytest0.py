# # 函数形式 要求以test开头
# def test_fun():
#     print("我是测试函数")

# 以类的方法运行  类名必须以Test开头
import pytest


class TestDemo:
    @pytest.mark.run(order=2)
    def test_fun3(self):
        print("我是测试函数3")

    @pytest.mark.run(order=1)
    def test_fun4(self):
        print("我是测试函数4")


if __name__ == "__main__":
    pytest.main("-s", r"G:\web自动化\Po计算机-pytest\pytest\test_pytest0.py")
