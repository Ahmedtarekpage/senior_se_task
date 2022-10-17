    - `local_storage.py :` : Serializing data into local storage
    - `ftp_storage.py :` : it's a Mock data "Designed for being an example" for FTP Storage
    - `default_destination.py :` : A Class used to make instance from abstract methods for ounSerializing data by the dormat you want
![serialication](https://i.ibb.co/2dZgVhT/1-Qaau-Fe77-Rsk7-Ye-ULrh-Utxw.gif)
- **Functions :**
    - read_data() : Retrieve(Backing Up) data into Python from Dictionary datatype by ounSerializing data
    - write_data() : for writing data as a new node of data, using key & value
    - write_new_batch() : writing multiple data 
    ### Example : 
    #### instead of sending Query like this (General Example)
    ```sql
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) VALUES("67ef590kalk4568901thbn7190akioe1", 1, 25, 10, 1.00, 10.00);
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) VALUES("67ef590kalk4568901thbn7190akioe1", 2, 16, 1, 1.59, 1.59);
    ```
    #### sending Query like this [Batch] (General Example)
    ```sql
        INSERT INTO EJB3.OrderLine (OrderId, LineNumber, ProductId, Quantity, Price, ExtendedPrice) 
        VALUES  [("67ef590kalk4568901thbn7190akioe1", 1, 25, 10, 1.00, 10.00)
        , ("67ef590kalk4568901thbn7190akioe1", 2, 16, 1, 1.59, 1.59)]
    ```
    - data_name(): returning the data destination 
    - delete_data(): deleting data by Accesing using the Key 
    - formating_data(): returning the data type 

    in this File defining methods as **abstract method** for using it as a template for the storage 

