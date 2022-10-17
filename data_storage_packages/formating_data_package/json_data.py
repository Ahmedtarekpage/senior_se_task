import json
from data_storage_packages.formating_data_package.storage_format_class import Defualt_formating


class JsonDataClass(Defualt_formating):

    def dump(self, dict_data):
        return json.dumps(dict_data)

    def load(self, serialized_data):
        return json.loads(serialized_data)

    def data_format_type(self):
        return "JSON Data"
