import pytest
from app.display_and_calc import DisplayAndCalc


@pytest.fixture
def i_display_and_calc():
    return DisplayAndCalc()


class TestDisplayAndCalc():
    def test_display_and_calc(self, i_display_and_calc):
        assert 55 == i_display_and_calc.ShowCalc()
