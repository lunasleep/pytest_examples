import time

import pytest


@pytest.fixture(autouse=True)
def mock_sleep(mocker):
    return mocker.patch.object(time, "sleep")
