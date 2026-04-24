import pytest
from config import configPath
from until import readCSV


def func_add(a, b):
    return a + b


class TestStudy:

    @pytest.mark.ut
    def test_definedMark(self):
        assert 1 == 1

    @pytest.mark.skip
    def test_builtInMarkSkip(self):
        assert 1 == 1

    @pytest.mark.skipif(True, reason="Skip test")
    def test_builtInMarkSkipIf(self):
        assert 1 == 1

    @pytest.mark.xfail
    def test_builtInMarkXpass(self):
        assert 1 == 1

    @pytest.mark.xfail
    def test_builtInMarkXfial(self):
        assert 1 == 2

    @pytest.mark.ddt
    @pytest.mark.parametrize("a,b,c", readCSV.readCSV(f"{configPath.dataPath}/data.csv"))
    def test_ddt(self, a, b, c):
        res = func_add(a, b)
        assert res == c
