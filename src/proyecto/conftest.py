import pytest
from django.conf import settings

# Example: add any global fixtures or pytest hooks here.
# pytest-django already provides 'db', 'client', etc.
# This is an example fixture you may want to use project-wide.

@pytest.fixture(scope="session", autouse=False)
def django_test_settings():
    """
    Optional: tweak settings for test session if necessary.
    Enabled only if you need to modify settings programatically.
    """
    # Example (uncomment if needed):
    # settings.DEBUG = False
    yield
