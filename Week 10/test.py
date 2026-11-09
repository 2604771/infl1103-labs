from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

#supplier Info
apple = Supplier("S001", "Apple", "orders@apple.example")              
#PhysicalProduct
macbook = PhysicalProduct("P001", "MacBook Air", 1000.00, 10, 2.0, apple)
#DigitalProduct
macos = DigitalProduct("D001", "macOS", 0.00, 100, 12000, apple)

macbook.display_information()                                          
macos.display_information()

print(macbook.get_supplier() is macos.get_supplier())                 
print(macbook is macos)                                                 

del apple #Remove apple supplier name and just print the macbook display                                            
macbook.display_information()