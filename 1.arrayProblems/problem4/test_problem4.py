import pytest
from problem4 import large_cont_sum

@pytest.mark.parametrize(
    argnames= "arr, expected",
    argvalues=[
        ([1,2,-1,3,4,-1],9),
        ([1,2,-1,3,4,10,10,-10,-1],29),
        ([-1,1],1)
    ]
)
def test__large_cont_sum(arr:list, expected:int):
     assert large_cont_sum(arr) == expected
