from input_error import input_error

@input_error

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and new phone number."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."