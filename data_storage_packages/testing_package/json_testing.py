import pytest
from data_storage_packages.formating_data_package.json_data import JsonDataClass


@pytest.fixture
def json_format():
    return JsonDataClass()


@pytest.fixture
def dict_data():
    dic = {"k": 1,
           "k2": 2,
           "k3": 3,
           "k4": "string"}
    return dic


@pytest.fixture
def dump_data():
    return '{"k": 1,' \
           ' "k2": 2,' \
           ' "k3": 3,' \
           ' "k4": "string"}'


def test_dump(dict_data, dump_data, json_format):
    real = json_format.dump(dict_data)
    expected = dump_data
    assert real == expected


def test_load(dict_data, dump_data, json_format):
    real = json_format.load(dump_data)
    expected = dict_data
    assert real == expected
