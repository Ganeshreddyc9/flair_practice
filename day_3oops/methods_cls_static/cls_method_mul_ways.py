from datetime import datetime


class Date:

    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod

    def from_string(cls, date_string):
        year , month , day = map(int,date_string.split('-'))
        return cls(year , month , day)

    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"



regular_date = Date(2023,1,1)
print(regular_date.display())

#using alternative constructor( @classmethod)
date_string = '2023-12-21'
alternative_date = Date.from_string(date_string)
print("Alternative Date:", alternative_date.display())

