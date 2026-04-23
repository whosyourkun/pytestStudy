import pytest


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

    @pytest.mark.xfial
    def test_builtInMarkXpass(self):
        assert 1 == 1

    @pytest.mark.xfail
    def test_builtInMarkXfial(self):
        assert 1 == 2