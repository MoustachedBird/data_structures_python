import pytest
from problem3 import finder,finder2

@pytest.mark.parametrize(

    argnames="arr1,arr2,expected",
    argvalues=[
        ([5,5,7,7],[5,7,7],5),
        ([1,2,3,4,5,6,7],[3,7,2,1,4,6],5),
        ([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1],6),
        ([10],[10],None),
        ([],[],None),
    ]
)

def test__finder(arr1,arr2,expected):
    """
    Test the finder function.
    Args:
        arr1 (list): First array.
        arr2 (list): Second array.
        expected (int or None): Expected result.
    """
    assert finder(arr1,arr2) == expected    
    assert finder2(arr1,arr2) == expected
