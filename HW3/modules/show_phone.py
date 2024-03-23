from input_error import input_error

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide name."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]