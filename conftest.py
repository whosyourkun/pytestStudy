import datetime
import pytest

@pytest.fixture(autouse=True,scope='session')
def fixture_session():
    print(datetime.datetime.now(), 'session开始使用')
    yield
    print(datetime.datetime.now(), 'session结束使用')