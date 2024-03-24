from address_book.classes import Record
from address_book.functions import AddressBook
from address_book.parse_input import parse_input
from address_book.classes import Phone


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Invalid input format. Please try again.")
            continue
        
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            name = args[0]
            record = Record(name)
            for phone in args[1:]:
                record.add_phone(phone)
            book.add_record(record)
            
        
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Please provide name and new phone number.")
            else:
                name, new_phone = args
                result = book.change_contact(name, new_phone)
                
        
        elif command == "phone":
            name = args[0]
            record = book.find(name)
            if record:
                record.show_phones()
            else:
                print("Contact not found.")
        
        elif command == "delete":
            name = args[0]
            if book.find(name):
                book.delete(name)
                print('Contact deleted successfully.')
            else: 
                print("Contact not found")

        elif command == "all":
            book.show_all()

        elif command == "add-birthday":
            name, birthday = args
            record = book.find(name)
            if record:
                record.add_birthday(birthday)
        else:
            print("Command not found.")

if __name__ == "__main__":
    main()

'''
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
'''
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