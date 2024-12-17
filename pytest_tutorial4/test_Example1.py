import pytest


@pytest.mark.usefixtures("open_browser")
def test_m1():
    print("Testcase1")

@pytest.mark.usefixtures("open_browser")
def test_m2():
    print("Testcase2")

@pytest.mark.usefixtures("open_browser")
def test_m3():
    print("Testcase3")
