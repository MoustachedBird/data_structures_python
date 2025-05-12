import pytest
from problem7 import uni_char

@pytest.mark.parametrize(
    argnames="s,expected",
    argvalues=[
        ('', True),
        ('goo', False),
        ('abcdefg', True)
    ]
)
def test__uni_char(s,expected):
    assert uni_char(s) == expected
