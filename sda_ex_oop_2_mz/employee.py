from datetime import date

from sda_ex_oop_2_mz.person import Person


class Employee(Person):

    def __init__(self, name, surname, birthday: date, salary):
        birthday = self.check_date(birthday)
        super().__init__(name, surname, birthday)
        self._salary = salary

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        value = self.check_date(value)
        self._birthday = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @staticmethod
    def check_date(value: date) -> date:
        if value > date(year=2020, month=12, day=31) or \
                value < date(year=1900, month=1, day=1):
            value = date(0, 0, 0)
        return value

    # @staticmethod
    # def check_birthday(value: int) -> int:
    # if value < 1900 | value > 2020:
    #    return 0
    # else:
    #  return value

    def who_am_i(self):
        print(f'Nazywam sie {self.name} {self.surname} i zarabiam {self.salary} zł')






