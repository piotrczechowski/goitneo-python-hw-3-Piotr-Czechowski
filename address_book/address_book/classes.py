from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        super().__init__(value)

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

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

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
    
