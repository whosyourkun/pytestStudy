import time

import pytest,os

if __name__ == '__main__':
    pytest.main(['./tests/test_allure.py',
                 '-vs',
                 '--alluredir=temps',
                 '--clean-alluredir'])
    time.sleep(1)
    if os.listdir("./temps"):
        print('生成测试报告')
        os.system(f"allure generate -o ./reports -c ./temps")
    else:
        print('未生成测试报告 ')
    # if os.listdir('./temps'):
    #     print(os.listdir('./temps'))
