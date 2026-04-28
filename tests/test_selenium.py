import pytest,time

@pytest.mark.web
def test_selenium(selenium):
    print("开启浏览器")
    selenium.get("https://www.baidu.com")
    print(selenium.title)
    print("关闭浏览器")
    time.sleep(2)