from datetime import date
from sda_ex_oop_2_mz.employee import Employee
from sda_ex_oop_2_mz.manager import Manager

manager = Manager('Arnold', 'Boczek', date(1964, 5, 3), 1000)
print(manager.salary)
manager.who_am_i()

employee = Employee('Ferdynand', 'Kiepski', date(1954, 10, 10), 1000)
print(employee.salary)
employee.who_am_i()

if __name__ == "__main__":
    pass
