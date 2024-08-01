'''
Модуль класів:
Field, Name, Phone, Birthday, Record
'''
from datetime import datetime

def Errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"ValueError: {e}") 
        except IndexError as e:
            print(f"IndexError: {e}") 
        except AttributeError as e:
            print(f"AttributeError: {e}")
        except TypeError as e:
            print(f"TypeError: {e}")
    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
	pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
            if not len(value) == 10 or not value.isdigit():
                raise ValueError(f"The phone number {value} is not correct")
            self.value = value

    def __ne__(self, phone):
        return self.value != phone.value

    def __eq__(self, phone):
        return self.value == phone.value
    
class Birthday(Field):
    # реалізація класу
    def __init__(self, value):
        try:
            if datetime.strptime(value or "", "%d.%m.%Y"):
                self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    # реалізація класу
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @Errors
    def add_phone(self, phone: str) -> bool:
        phone = Phone(phone)
        if phone.value:
            for iphone in self.phones:
                if phone == iphone:
                    raise IndexError(f"Phone number {phone.value} is already in the database")
            self.phones.append(phone)
            return True

    @Errors
    def remove_phone(self, phone: str) -> None:
        phone = Phone(phone)
        for iphone in self.phones:
            if iphone == phone:
                self.phones.remove(iphone)

    @Errors
    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        isedit = False
        phone_new = Phone(new_phone)
        phone_old = Phone(old_phone)
        for iphone in self.phones:
            if iphone == phone_old:
                iphone = phone_new
                return True
        
        if not isedit: 
            raise IndexError(f"There is no such number {phone_old.value} on the list.")

    @Errors
    def find_phone(self, phone: str) -> Phone:
        phone = Phone(phone)
        for iphone in self.phones:
            if iphone == phone:
                return iphone
                
    @Errors           
    def add_birthday(self, birthday: str) -> bool:
        ibirthday = Birthday(birthday)
        if ibirthday.value:
            self.birthday = ibirthday.value
            return True

    @Errors
    def __str__(self) -> str:
        if self.birthday is None: 
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"