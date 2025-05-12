import pytest
from problem5 import rev_word

@pytest.mark.parametrize(
    argnames="s,expected",
    argvalues=[
        ('    space before','before space'),
        ('space after     ','after space'),
        ('   Hello John    how are you   ','you are how John Hello'),
        ('1','1')
    ]
)

def test__rev_word(s,expected):
    assert rev_word(s) == expected