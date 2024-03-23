
from input_error import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and phone number."    
    name, phone = args
    contacts[name] = phone
    return "Contact added."