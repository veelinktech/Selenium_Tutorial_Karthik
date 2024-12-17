import pytest


@pytest.mark.smoke
def test_method1():
    a, b = 5, 10
    assert a + b == 15


@pytest.mark.regression
def test_testcase1():
    name = 'karthik'
    assert name.upper() == 'KARTHIK'


@pytest.mark.smoke
@pytest.mark.regression
def test_method2():
    x, y = 100, 50
    assert x - y == 505


@pytest.mark.smoke
def test_testcase2():
    a, b = 10, 10
    assert a * b == 100


@pytest.mark.sanity
def test_method3():
    st = 'Python'
    assert st.isalpha() == True
