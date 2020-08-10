from datetime import date

from sda_ex_oop_2_mz.employee import Employee


class Manager(Employee):

    def __init__(self, name, surname, birthday: date, salary):
        salary = salary * 1.2
        super().__init__(name, surname, birthday, salary)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value * 1.2

    def who_am_i(self):
        print(f'Nazywam sie manager {self.name} {self.surname} i zarabiam {self.salary} zł')