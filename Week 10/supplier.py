class Supplier:
    def __init__(self,supplier_id:str,name:str,contact_email:str):
        self.__supplier = supplier_id
        self.__name = name 
        self.__contact_email = contact_email

    def display_information(self):
        print(f"ID:{self.__supplier} | Name:{self.__name} | Contact:{self.__contact_email}")


