from collections import UserDict
import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            return "invalid"
        except TypeError:
            return "Invalid command. Please provide name and phone number()."
    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
         return str(self.value)



class Birthday(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not re.match(r'^\d{2}\.\d{2}\.\d{4}$', value):
            raise ValueError("Birthday must be in the format DD.MM.YYYY")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthdays = []

    @input_error
    def add_phone(self, phone):
        try:
            if len(phone) != 10:
                raise ValueError("Phone number must be exactly 10 digits")
            else:    
                self.phones.append(Phone(phone))
                print("Contact added successfully.")
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)
                break
    
    def add_birthday(self, birthday):
        self.birthdays.append(Birthday(birthday))
        
    def add_birthday_contact(self, name, birthday):
        if name in self.data:
            self.data[name].add_birthday_contact(birthday)
            print("birthday added")
        else:
            raise ValueError('Contact not found')

    def show_birthday(self, name):
        if name in self.data:
            if self.name[name].birthdays:
                print(f"{name}: Birthdays - {', '.join(str(b) for b in self.data[name].birthdays)}")
            else:
                print(f"{name}: No birthdays recorded.")
        else:
            print("Contact not found")
    

    def find_phone(self, phone):
        return phone in [str(p) for p in self.phones]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}: Birthday date: {'; '.join(str(b) for b in self.birthdays)}"
    
