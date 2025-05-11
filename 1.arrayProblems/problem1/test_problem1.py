
from problem1 import anagram, anagram2
import pytest

@pytest.mark.parametrize(
    argnames="s1,s2,expected",
    argvalues=[
        ('go go go','gggooo',True),
        ("abc", "cba", True),
        ("hi man", "hi     man", True),
        ("aabbcc", "aabbc", False),
        ("123", "12 ",False),
    ]
)    
def test__anagram(s1,s2,expected):
    """
    Test the anagram function.
    Args:
        s1 (str): First string.
        s2 (str): Second string.
        expected (bool): Expected result.
    """
    assert anagram(s1,s2) == expected
    assert anagram2(s1,s2) == expected