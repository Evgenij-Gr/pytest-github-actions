import pytest
import func


class TestFuncAdd:
    def test_IntInt(self):
        assert func.funcAdd(3, 4) == 7

    def test_ListList(self):
        assert func.funcAdd([1, 2], [3, 4]) == [1, 2, 3, 4]

