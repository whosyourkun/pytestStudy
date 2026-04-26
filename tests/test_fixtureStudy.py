import datetime, pytest


@pytest.fixture(autouse=True, scope='function')
def allUse():
    '''
    所有用例自动运行此夹具
    :return:
    '''
    print(datetime.datetime.now(), '所有用例均执行')


@pytest.fixture
def f():
    '''
    用例携带此函数的运行此夹具
    :return:
    '''
    # 前置操作
    print(datetime.datetime.now(), '开始被夹具使用')
    yield
    print(datetime.datetime.now(), '结束被夹具使用')

@pytest.fixture
def accept_param():
    '''
    此夹具会自动返回123，使用此夹具的用例需要有接受此返回结果的变量
    :return:
    '''
    print(datetime.datetime.now(), '用例开始执行')
    yield 123
    print(datetime.datetime.now(), '用例执行完毕')


@pytest.fixture
def fixture_useit():
    print(datetime.datetime.now(),'开始被夹具使用')
    yield
    print(datetime.datetime.now(),'结束被夹具使用')

@pytest.fixture
def ff(fixture_useit):
    print(datetime.datetime.now(), '用例开始执行')
    yield
    print(datetime.datetime.now(), '用例结束执行')

def test_1(f):
    pass


@pytest.mark.usefixtures("f")
def test_2():
    pass


def test_3(accept_param):
    print('fixture接收到的参数为：', accept_param)


def test_4(ff):
    pass
