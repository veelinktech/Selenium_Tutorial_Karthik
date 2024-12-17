import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity
def test_method4():
    assert (10 > 5) is True


@pytest.mark.
def test_testcase3():
    t = "Python"
    assert t.upper() == "PYTHON"
