import pytest


def get_data():
    return [["zhang", 1], ["wang", 2]]


# 以类的方法运行  类名必须以Test开头
class TestDemo:
    # 多个参数参数化
    @pytest.mark.parametrize("name, age", get_data())
    def test_fun2(self, name, age):
        print("我是测试函数2")
        print("{}年龄{}".format(name, age))


if __name__ == "__main__":
    pytest.main("-s", r"G:\web自动化\Po计算机-pytest\pytest\test_pytest0.py")
