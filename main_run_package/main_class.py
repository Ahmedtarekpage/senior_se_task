from data_storage_packages.destination_package.default_destination import Def_destination


class MainDataClass:
    def __init__(self, destination: Def_destination):
        """setup the Constructor of the Class → Saving the destination of the data

        Args:
            destination (Def_destination) → The data destination .
        """
        self.__destination = destination

    def put(self, k, v):
        """ Creating new data node.

        Args:
            k (str): Key for reaching data
            v (any): Data stored with the Key
        """
        self.__destination.write_data(k, v)

    def put_batch(self, k_v_list):
        """ Creating multiple nodes.

        Args:
            k_v_list (list[tuple[str, any]]): Key-Value list of the data nodes.
        """
        self.__destination.write_new_batch(k_v_list)

    def get(self, k):
        """ Get data value specified by Key

        Args:
            k (str): Key for reaching data

        Returns:
            any: Retrieved value
        """
        data = self.__destination.read_data()
        return data.get(k, None)

    def limit_offset(self, v=None, limit=-1, offset=0):
        """ Fetching and Searching a Value depends on limits & offset .

        Args:
            v (anything, option): Defaults → None for  bringing  all d else extract Special Data .
            limit (int): Number of d to be retrieved . -1  →  fetch all.
            offset (int): if there is an offsets we want to Skip .

        Returns:
            list[tuple[str, any]]: List of k-v .
        """

        # Reading data
        if offset < 0:
            offset = 0
        d = self.__destination.read_data()
        if limit < 0:
            limit = len(d)
        range_limitations = offset + limit
        if v is not None:
            data_ = dict()
            for k, v in d.items():
                if v == v:
                    data_[k] = v
            d = data_

        if range_limitations > len(d):
            range_limitations = len(d)

        result = []

        items = list(d.items())
        i = offset
        while i < range_limitations and len(result) < limit:
            result.append(items[i])
            i += 1
        return result

    def delete(self, k):
        """Delete a data .

        Args:
            k (str): Key of the data to be deleted.
        """
        self.__destination.delete_data(k)

    def formating(self):
        """Returns data format (Example → JSON) .

        Returns:
            str: Type of Data .
        """
        return self.__destination.formating_data()

    def update(self, k, v):
        """ Update an existing data .

        Args:
            k (str): Key for reaching data.
            v (any): Data value.

        Raises:
            Exception: Exception raises if there is an Key Error.
        """
        data = self.__destination.read_data()
        if k not in data:
            raise Exception("wrong data")
        else:
            self.__destination.write_data(k, v)

    def destination(self):
        """Returns destination (Example → local Storage).

        Returns:
            str: Destination.
        """
        return self.__destination.data_name()
