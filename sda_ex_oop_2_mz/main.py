from datetime import date

from sda_ex_oop_2_mz.employee import Employee
from sda_ex_oop_2_mz.manager import Manager

employee = Employee('Jan', 'Kowalski', date(1985, 4, 7), 1000)
print(employee.salary)
employee.who_am_i()

manager = Manager('Jan', 'Kowalski', date(1992, 10, 10), 4500)
print(manager.salary)
manager.who_am_i()
