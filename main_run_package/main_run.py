# Software Engineer : Ahmed Tarek Morsy
# Mail : Ahmedtprofile@gmail.com
# Task For : Y42 Company
# Date Created : 15 / 10 / 2022
# collaborator : oltjona dyrmishi


from os import unlink
from colorama import Fore
from data_storage_packages.formating_data_package.json_data import JsonDataClass
from main_run_package.main_class import MainDataClass
from data_storage_packages.destination_package.local_storage import local_Storage


def main_run():
    limit, offset = 1, 2
    print(Fore.BLUE, "Storing Data 🔄")
    ds.put("k", 1)
    ds.put_batch([("k", 1),
                  ("k2", 2),
                  ("k3", "string")])
    print(Fore.GREEN, "limit =", Fore.RED, f"{limit}\n", Fore.GREEN,
          "offset =", Fore.RED, f"{offset}")
    print()

    print(Fore.GREEN, "All data Items 📊 → ", Fore.RED, ds.limit_offset())
    print(Fore.GREEN, "Data time with Limit & offset",
          Fore.RED, ds.limit_offset(limit=limit, offset=offset))
    print(Fore.GREEN, "======== Data Has Been Stored Successfully ✅ ========")

    print(Fore.BLUE, "Getting Data ")
    print(Fore.RED, "k2 :", ds.get("k2"))
    print(Fore.GREEN, "======== Data Extracted Successfully ✅ ========")

    print(Fore.BLUE, "Updating Data")
    ds.update("k2", 10)
    print(Fore.GREEN, "new Value of K2 :", Fore.RED, ds.get("k2"))
    print(Fore.GREEN, "======== Data Updated Successfully ✅ ========")
    print(Fore.RED, "Error in Updating Data")

    print(Fore.GREEN, "Trying to Update non-Key Data")
    # Updating data with Error Value
    try:
        ds.update("Error_value", 1000)
    except Exception:
        print(Fore.RED, "You are Updating a non-key data .")
        print(Fore.GREEN, "======== We Ignored the Error of Updating Non Key Data Successfully ========")

        print(Fore.BLUE, "Deleting Data")
        ds.delete("k3")
        print(Fore.GREEN, "Trying to Get k3 data after deleting : ",
              Fore.RED, ds.get("k3"))
        print(Fore.GREEN, "======== Data Deleted Successfully ✅ ========")



def unlinking(file):
    unlink(file)


if __name__ == "__main__":
    print(Fore.BLUE, "Welcome to SE-Task Program For Y42 Company 💻")
    print("===============================================")
    data_formating = JsonDataClass()
    destination = local_Storage(data_formating, "data.json")
    ds = MainDataClass(destination)
    print(Fore.GREEN, "Data Format → ", Fore.RED, f"{ds.formating()} 🗒️\n", Fore.GREEN, "Desitnation → ",
          Fore.RED, f"{ds.destination()} 🗒️ ")
    print(Fore.BLUE, "=====================================================")
    print(Fore.BLUE, "Running the Main Code ... 🔄 ")
    main_run()
    unlinking("data.json")
