import yaml
from config import configPath


def readYaml(filename = 'testcase.yaml'):
    f = open(configPath.dataPath+f'/{filename}')
    s = f.read()
    data = yaml.safe_load(s)
    return data
