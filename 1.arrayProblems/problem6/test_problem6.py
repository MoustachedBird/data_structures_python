import pytest
from problem6 import compress

@pytest.mark.parametrize(
    argnames= "s,expected",
    argvalues= [
        ('', ''),
        ('AABBCC', 'A2B2C2'),
        ('AAABCCDDDDD', 'A3B1C2D5')
    ]
)

def test__compress(s, expected):
    assert compress(s) == expected