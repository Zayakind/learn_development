import pytest

from asd.chapter_one.hash_table import HashTable


@pytest.fixture()
def hash_table():
    return HashTable(17, 2)


def test_put_hash(hash_table):
    hash_table.put("15")
    assert hash_table.slots[(id("15") % 17)]


def test_find_hash(hash_table):
    hash_table.put("15")
    assert hash_table.find("15")
