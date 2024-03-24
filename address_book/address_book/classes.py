from collections import UserDict
import re
from .input_error import input_error


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
        self.value = value
    
    def __str__(self):
         return str(self.value)
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthdays = []

   
    @input_error
    def add_phone(self, phone):
        if len(phone) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        else:    
            self.phones.append(Phone(phone))
            print("Contact added successfully.")
        
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]
    
    @input_error
    def add_birthday(self, birthday):
        if not isinstance(birthday, str) or not re.match(r'^\d{2}\.\d{2}\.\d{4}$', birthday):
            raise ValueError("Birthday must be in the format DD.MM.YYYY")
        else:
            self.birthdays.append(Birthday(birthday))
            print ("Date of birth added.")
        
    @input_error
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
    
