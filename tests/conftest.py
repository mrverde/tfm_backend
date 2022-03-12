import pytest
from app import app


@pytest.fixture(scope='session')
def app(request):

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture()
def client(app):
    return app.test_client()
