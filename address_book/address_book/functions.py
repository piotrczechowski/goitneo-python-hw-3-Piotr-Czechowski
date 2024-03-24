from collections import UserDict
from datetime import datetime
from .classes import Phone

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

    def change_contact(self, name, new_phone):
        record = self.find(name)
        if record:
            record.phones = [Phone(new_phone)]
            return "Contact updated."
        else:
            return "Contact not found."

    def get_birthdays_per_week(self, name):
        # Data structure to store birthdays for each day of the week
        birthdays_per_week = {
            'Monday': [], 
            'Tuesday': [], 
            'Wednesday': [],
            'Thursday': [], 
            'Friday': [], 
            'Saturday': [], 
            'Sunday': []
        }
        
        # Iterate over each record in the address book
        for record in self.data.values():
            # Iterate over each birthday in the record
            for birthday in record.birthdays:
                # Convert birthday to date and time object
                birthday_date = datetime.strptime(birthday.value, '%d.%m.%Y')
                
                # Calculate the day of the week for the birthday
                day_of_week = birthday_date.strftime('%A')
                
                # Adjust birthday to Monday if it falls on the weekend
                if day_of_week in ['Saturday', 'Sunday']:
                    day_of_week = 'Monday'
                
                # Store the birthday on the corresponding day of the week
                birthdays_per_week[day_of_week].append(birthday.value)
        
        return birthdays_per_week
       
