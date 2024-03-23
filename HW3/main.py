from modules.parse_input import parse_input
from modules.add_contact import add_contact
from modules.change_contact import change_contact
from modules.show_all import show_all
from modules.show_phone import show_phone



def main():
    contacts = {}
    
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()
