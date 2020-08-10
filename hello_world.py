from datetime import date
from sda_ex_oop_2_mz.employee import Employee
from sda_ex_oop_2_mz.manager import Manager

    manager = Manager('Jan', 'Kowalski', date(1992, 10, 10), 4500)
    print(manager.salary)
    manager.who_am_i()

    employee = Employee('Jan', 'Kowalski', date(1992, 10, 10), 2500)
    print(employee.salary)
    employee.who_am_i()

if __name__ == "__main__":

