from pytest_socket import disable_socket


def pytest_runtest_setup():
    """Disable external network requests from tests"""
    disable_socket()
