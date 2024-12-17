import pytest


@pytest.mark.parametrize("num,res",[(1,10),(2,20),(3,30),(4,50),(5,50)])
def test_calc(num,res):
    assert  num * 10  == res