import pytest

@pytest.fixture()
def browser():
    print('open browser')
    yield
    print('close browser')
@pytest.fixture()
def user():
    return 'username', 'password'
@pytest.fixture()
def login_page(browser):
    pass


def test_login(login_page, user):
    username, password = user
    assert username == 'username'
    assert password == 'password'


