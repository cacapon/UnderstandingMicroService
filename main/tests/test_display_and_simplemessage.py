import pytest
from app.display_and_simplemessage import DisplayAndSimpleMessage


@pytest.fixture
def i_display_and_simplemessage():
    return DisplayAndSimpleMessage()


class TestDisplayAndSimpleMessage():
    def test_display_and_simplemessage(self, i_display_and_simplemessage):
        assert 'hello world.' == i_display_and_simplemessage.ShowSimpleMessage()
