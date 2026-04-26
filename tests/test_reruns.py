import random

import pytest


@pytest.mark.ut
def test_reruns():
    a = random.randint(1,10)
    assert a >= 5