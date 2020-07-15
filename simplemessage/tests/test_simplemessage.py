import pytest
from app.simplemessage import SimpleMessage


@pytest.fixture
def i_simplemessage():
    return SimpleMessage()


class TestSimpleMessage():
    def test_simplemessage(self, i_simplemessage):
        assert 'hello world.' == i_simplemessage.simplemessage()
