from collections import UserDict
from datetime import datetime
from .classes import Phone
from .input_error import input_error
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def show_birthday(self, name):
        if name in self.data:
            record = self.data[name]
            print(f"{record.name}: Birthdays - {', '.join(str(b) for b in record.birthdays)}")
        else:
            print("Contact not found")
    
    def show_all(self):
        for record in self.data.values():
            print(f"Name: {record.name}")
            print("Phones:")
            for phone in record.phones:
                print(f"- {phone}")
            print("Birthdays:")
            for birthday in record.birthdays:
                print(f"- {birthday}")
            print()

    @input_error
    def change_contact(self, name, new_phone):
        record = self.find(name)
        if not record:
            raise ValueError("Contact not found")
        if len(new_phone) != 10: 
            raise ValueError("Phone number must be exactly 10 digits")
        record.phones = [Phone(new_phone)]
        print(f"Contact updated {name}.")

    def get_birthdays_within_next_week(self):
        
        today = datetime.now().date()

       
        next_week = today + timedelta(days=7)
        birthdays_within_next_week = {}
        for record in self.data.values():
            for birthday in record.birthdays:
                
                birthday_str = str(birthday)
               
                birthday_date = datetime.strptime(birthday_str, '%d.%m.%Y').date()
                
                if today <= birthday_date <= next_week:
                    
                    day_of_week = birthday_date.strftime('%A')
                    
                    birthdays_within_next_week.setdefault(day_of_week, []).append(record.name)

        return birthdays_within_next_week
