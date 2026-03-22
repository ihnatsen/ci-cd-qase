import pytest
from qase.pytest import qase
from calculater import *

@qase.id(87)
def test_add():
    assert 2 == my_sum(1, 1)
