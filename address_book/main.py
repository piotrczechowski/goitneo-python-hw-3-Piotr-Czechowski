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
            if len(args) < 2:
                print("Invalid command. Please provide both a name and a birthday.")
            else:
                name, birthday = args
                record = book.find(name)
                if record:
                    record.add_birthday(birthday)
        
        elif command == "show-birthday":
            if len(args) < 1:
                print("Invalid command. Please provide a name.")
            else:
                name = args[0]  
                book.show_birthday(name)

        elif command == "birthdays":
            next_week_birthdays = book.get_birthdays_within_next_week()
            for day, birthdays in next_week_birthdays.items():
            
                birthday_names = [str(name) for name in birthdays]
                print(f"{day}: {', '.join(birthday_names)}")

        

        else:
            print("Command not found.")

if __name__ == "__main__":
    main()

'''
#Test users 

# Instantiate the AddressBook
book = AddressBook()

# Create a record for user "John"
john_record = Record("John")

# Add phones to John's record
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Add a birthday for John
john_record.add_birthday("22.06.1990")

# Create a record for user "Amelia"
amelia_record = Record("Amelia")

# Add phones to Amelia's record
amelia_record.add_phone("1234567890")
amelia_record.add_phone("5555555555")

# Add Amelia's record to the address book
book.add_record(amelia_record)

# Add a birthday for Amelia
amelia_record.add_birthday("24.03.2024")
'''