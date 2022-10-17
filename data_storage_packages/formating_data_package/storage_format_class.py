from abc import ABC as Abstract, abstractmethod


class Defualt_formating(Abstract):
    @abstractmethod
    def dump(self, dict_data: dict):
        """ Data is transformed into a string before being stored.

        Args:
            dict_data (dict): Data representation with a dictionary.
        """
        pass

    @abstractmethod
    def load(self, serialized_data) -> dict:
        """ data loaded into a Python Dictionary object as serialised strings.

        Args:
            serialized_data (str): Serialized data.

        Returns:
            dict: Data representation with a dictionary.
        """
        pass

    @abstractmethod
    def data_format_type(self):
        """ Returns type of the Data.

        Returns:
            str: typr of Data Format
        """
        pass
