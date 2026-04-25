import csv
from config import configPath

dataCSV = configPath.dataPath + "/data.csv"


def readCSV(path):
    f = open(path)
    # reader = csv.DictReader(f)
    # print(list(reader))
    reader = csv.reader(f)
    ddt_data = []
    for res in list(reader)[1:]:
        ddt_data.append(list(map(lambda x: int(x), res)))
    f.close()
    return ddt_data


if __name__ == '__main__':
    res = readCSV(dataCSV)
    print(res)
