import pytest


@pytest.mark.usefixtures("open_browser")
def test_m4():
    print("Testcase4")


@pytest.mark.usefixtures("open_browser")
def test_m5():
    print("Testcase5")
