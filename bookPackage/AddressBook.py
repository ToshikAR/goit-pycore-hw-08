__all__= ['AddressBook']
'''
class Address Book
'''

from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record) -> None:
        self.data[record.name.value] = record
    
    def find(self, name: str) -> None:
        if name in self.data:
            return self.data.get(name)

    def delete(self, name) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> str:
        today = datetime.today()
        days = 7
        text = ''

        for data in self.data:
            birthday_str = self.data[data].birthday
            if birthday_str is None: continue
            birthday_date_this_year = datetime.strptime(birthday_str, "%d.%m.%Y").replace(year=today.year)
            if birthday_date_this_year < today:
                birthday_date_this_year = birthday_date_this_year.replace(year=today.year + 1)

            birthday_days =  (birthday_date_this_year - today).days  
            if birthday_days in range(0, days):
                text += f"{data}'s birthday is {birthday_date_this_year.strftime("%d.%m.%Y") }, {birthday_days} days left\n"
                
        return text

    def __str__(self) -> str:
        text = "{:^48}\n".format('Address Book')
        text += "{:^39}\n".format('-'*53)
        base_format = '{:<13} | {:<11} | {:<11}'
        text += f"{base_format.format('Contact name','Birthday','Phones', )}\n"
        text += f"{base_format.format('-'*13 , '-'*11, '-'*23)}\n"

        for idata in self.data:
            icont, idate, iitem  = idata, self.data[idata].birthday,  '; '.join(p.value for p in self.data[idata].phones)
            if idate is None: idate = ' '
            text += f"{base_format.format(icont, idate, iitem)}\n"
        return text

