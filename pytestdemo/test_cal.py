import calculator


# def add(a,b):
#     return a+b

class TestCal():

    def setup(self):
        print('开始')

    def test_add(self):
        calc = calculator()
        assert calc.add(1 + 1) == 2

    def teardown(self):
        print('结束')
