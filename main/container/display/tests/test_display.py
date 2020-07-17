import pytest
from app.display import Display


@pytest.fixture
def i_display():
    return Display()


class TestDisplay():
    @pytest.mark.parametrize(
        'input_word', [
            ('hello'),
            (123),
            (456.7),
            ({'foo': 'bar'}),
            ([8, 9, '0'])
        ]
    )
    def test_show(self, i_display, input_word):
        assert input_word == i_display.show(input_word)
