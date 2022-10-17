import pytest
from os import unlink
from os.path import exists
import json
from data_storage_packages.formating_data_package.json_data import JsonDataClass
from data_storage_packages.destination_package.local_storage import local_Storage

file_name = "my_json.json"


@pytest.fixture
def local_file_storage():
    if exists(file_name):
        unlink(file_name)
    return local_Storage(JsonDataClass(), file_name)


@pytest.fixture
def data():
    return [("k1", 1),
            ("k2", 2),
            ("k3", "string")]


@pytest.fixture
def data_dump():
    return '{"k": 1,' \
           ' "k2": 2, ' \
           '"k3": "string"}'


def test_writing_batch(local_file_storage, data):
    fs = local_file_storage
    fs.write_new_batch(data)

    saved_data = {}
    with open(file_name) as f:
        saved_data = json.load(f)

    for key, val in data:
        assert saved_data[key] == val


def test_writing(local_file_storage, data):
    fs = local_file_storage
    data = data[0]
    fs.write_data(*data)

    with open(file_name) as f:
        assert json.load(f)[data[0]] == data[1]


def test_reading(local_file_storage, data_dump):
    fs = local_file_storage
    with open(file_name, "w") as f:
        f.write(data_dump)

    data_dict = fs.read_data()
    assert data_dict == json.loads(data_dump)


def test_delete(local_file_storage, data_dump):
    fs = local_file_storage
    with open(file_name, "w") as f:
        f.write(data_dump)

    fs.delete_data("k")
    expected = json.loads(data_dump)
    expected.pop("k")

    assert fs.read_data() == expected


def unlinking_module():
    unlink(file_name)
