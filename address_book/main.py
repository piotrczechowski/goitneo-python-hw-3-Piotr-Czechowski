from address_book.classes import *
from address_book.functions import *


# Creation of a new address book 
book = AddressBook()

# Creation of a entry for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("22.06.2222")

irmiona_record = Record('Irmina')
irmiona_record.add_birthday('22.11.2222')

#get_birthdays_per_week(book)


# Add a John entry to the address book
book.add_record(john_record)
book.add_record(irmiona_record)

#list all recortds
for name, record in book.data.items():
    print(record)

book.show_birthday("Irmina")
'''

# Creating and adding a new entry for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Displaying all entries in the contact list
for name, record in book.data.items():
    print(record)

# Find and edit a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone number in John's entry
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

# Deletion: 5555555555

# Deletion Jane's entry
book.delete("Jane")

# Displaying all entries in the contact list after delete operation
for name, record in book.data.items():
    print(record)

'''