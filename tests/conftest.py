import pytest

from zgw_consumers_oas.schema_loading import _cache, lock


@pytest.fixture()
def schema_cache():
    yield
    with lock:
        _cache.clear()
