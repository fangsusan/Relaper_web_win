import allure
import pytest
import yaml


@allure.feature("TestDome测试类")
class TestDemo:

    @allure.step("开发环境嘛")
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是：",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是：",env["dev"])

    @allure.story("打印环境名称")
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))
