import pytest
import func


class TestFuncAdd:
    def test_IntInt(self):
        assert func.funcAdd(3, 4) == 7

    def test_ListList(self):
        assert func.funcAdd([1, 2], [3, 4]) == [1, 2, 3, 4]

    def test_IntIntFail(self):
        assert func.funcAdd(2, 5) == 9

    def test_IntIntAnotherFail(self):
        assert func.funcAdd(4, 4) == 16

