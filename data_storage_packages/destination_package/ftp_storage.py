from data_storage_packages.destination_package.default_destination import Def_destination
import ftplib
from os import unlink


class FTPClass(Def_destination):

    def __init__(self, formating, address, username, password, filename):
        """Creating FTP Destination setting with preferred data format.
        Args:
            formating (BaseDataFormat) → data serialization data format.
            address (str)  → host address 
            username (str) → Username 
            password (str) → Password 
            filename (str) → The filepath for W/R into file
        Raises:
            NotImplementedError: For Telling that it's a Mock
        """
        super().__init__(formating)
        self.host = address
        self.username = username
        self.password = password
        self.filename = filename

        raise NotImplementedError("MOCK")

    def __connect(self):
        """
        FTP Connecting 

        Returns:
            FTP object
        """
        return ftplib.FTP(self.host, self.username, self.password)


    def write_data(self, k, v):
        data = self.read_data()
        data[k] = v
        self.__saving(data)
        pass

    def write_new_batch(self, k_v_list: list):
        data = self.read_data()
        for key, value in k_v_list:
            data[key] = value
        self.__saving(data)


    def read_data(self):
        ftp = self.__connect()
        file_str = ""
        ftp.retrlines(self.filename, lambda x: file_str + f"{x}\n")
        ftp.close()
        data = self._format.load(file_str)
        return data


    def delete_data(self, key):
        data = self.read_data()
        if key in data:
            data.pop(key)
        self.__saving(data)

    def data_name(self):
        return "FTP"

    def __saving(self, data_dict):
        """ Writedown data to specified file at FTP server .

        Args:
            data_dict (dict): Data object
        """
        dumping_data = self._format.dump(data_dict)
        with open("backup.tmp", "w") as f:
            f.write(dumping_data)
        with open("backup.tmp", "r") as f:
            ftp = self.__connect()
            ftp.storlines(f"STOR {self.filename}", f)
        unlink("backup.tmp")


    def formating_data(self):
        self._format.data_format_type()
