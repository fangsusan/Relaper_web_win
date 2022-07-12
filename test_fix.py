
import pytest
"""
fixture装饰器
"""


@pytest.fixture()
def add(request):
    print("fixture拿到的原始参数是：",request.param)
    sum = request.param[0] + request.param[1]
    yield sum

@pytest.mark.usefixtures('aa')
def test_b(aa):
    print("hellop")

@pytest.mark.parametrize("add",[(1,3),(4,7)],indirect=True)
def test_a(add):
    print("-------执行test_a测试用例-------")
    print(f"fixture返回的参数和是：{add}")


