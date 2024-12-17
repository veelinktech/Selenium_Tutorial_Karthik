import pytest
from selenium import webdriver


@pytest.fixture(params=["Edge", "Firefox", "Chrome"], scope='class')
def all_browser(request):
    if request.param == "Edge":
        web_driver = webdriver.Edge()

    if request.param == "Firefox":
        web_driver = webdriver.Firefox()

    if request.param == "Chrome":
        web_driver = webdriver.Chrome()

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope='class')
def init_Chrome(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_Firefox(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.fixture(scope='class')
def init_Edge(request):
    ed_driver = webdriver.Edge()
    request.cls.driver = ed_driver
    yield
    ed_driver.close()