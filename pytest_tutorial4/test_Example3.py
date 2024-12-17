import pytest


@pytest.mark.usefixtures("open_browser")
def test_m6():
    print("Testcase6")


@pytest.mark.usefixtures("open_browser")
def test_m7():
    print("Testcase7")
