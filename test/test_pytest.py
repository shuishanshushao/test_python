# # 函数形式 要求以test开头
# def test_fun():
#     print("我是测试函数")

# 以类的方法运行  类名必须以Test开头
import pytest


class TestDemo:
    # 单个参数参数化
    @pytest.mark.parametrize("name", ["1", "2"])
    def test_fun1(self, name):
        print("我是测试函数1")
        print(name)

    # 多个参数参数化
    @pytest.mark.parametrize("name, age", [["zhang", 1], ["wang", 2]])
    def test_fun2(self, name, age):
        print("我是测试函数2")
        print("{}年龄{}".format(name, age))