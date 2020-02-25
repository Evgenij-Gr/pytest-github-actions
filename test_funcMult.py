import pytest
import func


class TestFuncMult:
    def test_IntInt(self):
        assert func.funcMult(3, 4) == 12

    def test_ListList(self):
        assert func.funcMult([1, 2], 2) == [1, 2, 1, 2]