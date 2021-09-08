import pytest
from delivery.app import creat_app


@pytest.fixture(scope="module")
def app():
    return creat_app()