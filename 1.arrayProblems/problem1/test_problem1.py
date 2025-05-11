
from problem1 import anagram
import pytest

@pytest.mark.parametrize(
    argnames="s1,s2",
    argvalues=[
        ('go go go','gggooo',True),
        ("abc", "cba", True),
        ("hi man", "hi     man", True),
        ("aabbcc", "aabbc", False),
        ("123", "12 ",False),
    ]
)    
def test_anagram():
    assert anagram([1, 2, 3, 4, 5]) == 15