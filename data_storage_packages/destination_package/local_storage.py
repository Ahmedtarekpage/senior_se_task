from data_storage_packages.formating_data_package.storage_format_class import Defualt_formating
from data_storage_packages.destination_package.default_destination import Def_destination


class local_Storage(Def_destination):
    def __init__(self, formating: Defualt_formating, filepath: str):
        """With your desired data format, create a file storage destination.

        Args:
            formating (Defualt_formating) →  Data Format used → for thwe data serialization.
            filepath (str) → The filepath to be used for write/read data.
        """
        super().__init__(formating)
        self.__path = filepath
        open(filepath, "a")

    def write_new_batch(self, k_v_list):
        data = self.read_data()
        for key, value in k_v_list:
            data[key] = value
        self.__save(data)

    def write_data(self, key, value):
        data = self.read_data()
        data[key] = value
        self.__save(data)


    def read_data(self):
        data = {}
        with open(self.__path, "r+") as store:
            serialized = store.read()
            if len(serialized) > 0:
                data = self._format.load(serialized)
        return data

    def delete_data(self, k):
        data = self.read_data()
        if k in data:
            data.pop(k)
        self.__save(data)

    def __save(self, data):
        """Writedown data  file.

        Args:
            data (dict) → object of data
        """
        with open(self.__path, "w") as storage:
            storage.write(self._format.dump(data))


    def data_name(self):
        return "Local Storage"

    def formating_data(self):
        return self._format.data_format_type()
