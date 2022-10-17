from data_storage_packages.formating_data_package.storage_format_class import Defualt_formating
from abc import ABC as Abstract, abstractmethod


class Def_destination(Abstract):
    def __init__(self, format: Defualt_formating):
        """ new destination 

        Args:
            format (Defualt_formating)→ Data for data serialization.
        """
        self._format = format
        super().__init__()

    @abstractmethod
    def read_data(self) -> dict:
        """ Retrieve(Backing Up) data into Python from Dictionary datatype by ounSerializing data

        Returns:
            dict: Python Dictionary of the stored data
        """
        pass

    @abstractmethod
    def write_data(self, key, value):
        """ new node of data, using key & value.

        Args:
            key (str) → for Accesing the Data
            val (any) → Getting the Data
        """
        pass

    @abstractmethod
    def write_new_batch(self, key_val_list: list):
        """ Create multiple data nodes.
        Example → instead of sending 
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) VALUES("67ef590kalk4568901thbn7190akioe1", 1, 25, 10, 1.00, 10.00);
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) VALUES("67ef590kalk4568901thbn7190akioe1", 2, 16, 1, 1.59, 1.59);

        batch will be → 
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) 
        VALUES  [("67ef590kalk4568901thbn7190akioe1", 1, 25, 10, 1.00, 10.00)
        , ("67ef590kalk4568901thbn7190akioe1", 2, 16, 1, 1.59, 1.59)]


        Args:
            key_val_list (list[tuple[str, any]]): Key-Value list of data nodes to be created.
        """
        pass

    @abstractmethod
    def data_name(self):
        """Returns DataStore's destination.

        Returns:
            str: Name.
        """
        pass

    @abstractmethod
    def delete_data(self, key):
        """Delete a node of the data .

        Args:
            key (str): deleting the value through reaching the key.
        """
        pass

    @abstractmethod
    def formating_data(self):
        """Returns formating of the data.

        Returns:
            str: Type of Data Format
        """
        pass
