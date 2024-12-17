import pytest


@pytest.fixture(scope='package')
def open_browser():
    print("Open the browser")
    yield
    print("close the browser")