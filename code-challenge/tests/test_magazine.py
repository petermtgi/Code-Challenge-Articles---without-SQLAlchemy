import pytest
from lib.models.magazine import Magazine

def test_create_and_find_magazine():
    mag = Magazine.create("Test Mag", "TestCat")
    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Test Mag"
    assert found.category == "TestCat"