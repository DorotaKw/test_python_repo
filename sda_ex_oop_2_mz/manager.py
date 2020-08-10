from datetime import date

from IPython.utils.coloransi import value

from sda_ex_oop_2_mz.employee import Employee


class Manager(Employee):

    def __init__(self, name, surname, birthday: date, salary):
        salary = salary * 1.1
        super().__init__(name, surname, birthday, salary)

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self):
        self.salary = value * 1.1

    def who_am_i(self):
        print(f'Nazywam sie manager {self.name} {self.surname} i zarabiam {self.salary} zł')