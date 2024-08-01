
'''
Модуль обробки команд
'''

import re
from colorama import Fore, Style
from .AddressBook import AddressBook
from .ClassModule import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"ValueError: {e}"
        except KeyError as e:
            return f"KeyError: {e}"
        except IndexError as e:
            return f"IndexError: {e}"
        except AttributeError as e:
            return f"AttributeError: {e}"
        except TypeError as e:
            return(f"TypeError: {e}")
    return inner

@input_error
def add_contact(args, book: AddressBook) -> str:
    if len(args) != 2: raise ValueError("Enter the argument for the command.")
    name, phone, *_ = args
    record = book.find(name)
    message = "No contact"
    if record and phone:
        if record.add_phone(phone):
            message = "Contact updated."
        else:
            message = "Contact not updated."

    if record is None and phone:
        record = Record(name)
        book.add_record(record)
        if record.add_phone(phone):
            message = "Contact added"
        else:
            book.delete(name)
            message = "Contact not added"
    return message

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    if len(args) != 3: raise ValueError("Enter the argument for the command.")
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None: 
        raise KeyError("Contact does not exist.")
    if old_phone and new_phone:
        if not record.edit_phone(old_phone, new_phone):
            return "Phone not updated."
    return "Phone updated."

@input_error
def find_contact(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact does not exist.")
    return record

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    if len(args) != 2: raise ValueError("Enter the argument for the command.")
    name, birthday, *_ = args
    record = book.find(name)
    if record is None: 
        raise KeyError("Contact does not exist.")
    if not record.add_birthday(birthday):
        return "Birthday not added."
    return "Birthday added."

@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None: 
        raise KeyError("Contact does not exist.")
    
    return f"Birthday {name}: {record.birthday}"

    
