import pytest
from app.calc import Calc


@pytest.fixture
def i_calc():
    return Calc()


class TestCalc():
    def test_calc(self, i_calc):
        assert 55 == i_calc.calc()
