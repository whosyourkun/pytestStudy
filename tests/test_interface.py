from until import readYaml
import pytest,jsonpath_ng,requests

@pytest.mark.interface
def test_request():
    info = readYaml.readYaml('test_api.yaml')
    print(info['name'])

    check_method = jsonpath_ng.parse('$..method')
    check_url = jsonpath_ng.parse('$..url')
    check_status_code = jsonpath_ng.parse('$..status_code')

    try:
        if check_method.find(info) and check_url.find(info) and check_status_code.find(info):
            print(check_method.find(info)[0].value, check_url.find(info)[0].value)
            response = requests.request(check_method.find(info)[0].value, check_url.find(info)[0].value)
            assert response.status_code == check_status_code.find(info)[0].value
        else:
            print('check info error')
            raise Exception('check info error')
    except Exception as e:
        print(e)