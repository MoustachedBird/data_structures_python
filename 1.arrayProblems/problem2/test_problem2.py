from problem2 import pair_sum
import pytest



@pytest.mark.parametrize(
    argnames="s1,s2,expected",
    argvalues=[
        ([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10,6),
        ([1,2,3,1],3,1),
        ([1,3,2,2],4,2)
    ]
)
def test__pair_sum(s1,s2,expected):
    assert pair_sum(s1,s2) == expected