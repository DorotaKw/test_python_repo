from sda_ex_oop_1_mz.cat import Cat
from sda_ex_oop_1_mz.dog import Dog
from datetime import date
from sda_ex_oop_2_mz.employee import Employee
from sda_ex_oop_2_mz.manager import Manager


def cat_creator() -> list:
    cats = []
    cat1 = Cat("Panda")
    cat2 = Cat("Filemon")
    cat1.eat_mouse()
    cats.append(cat1)
    cats.append(cat2)
    return cats


def dog_creator() -> list:
    dogs = []
    dog1 = Dog("Reksio")
    dog2 = Dog("Azor")
    dogs.append(dog1)
    dogs.append(dog2)
    return dogs


def animal_creator(animals: list):
    cat1 = Cat("Panda")
    cat2 = Cat("Filemon")
    dog1 = Dog("Reksio")
    dog2 = Dog("Azor")
    animals.append(cat1)
    animals.append(cat2)
    animals.append(dog1)
    animals.append(dog2)


def main():
    dogs = dog_creator()
    for dog in dogs:
        print(dog.make_sound())
    cats = cat_creator()
    for cat in cats:
        print(cat.make_sound())
        cat.eat_mouse()
    animals = []
    animal_creator(animals)
    for animal in animals:
        print(animal.make_sound())
    cat.move()
    manager = Manager('Jan', 'Kowalski', date(1992, 10, 10), 4500)
    print(manager.salary)
    manager.who_am_i()

    employee = Employee('Jan', 'Kowalski', date(1992, 10, 10), 2500)
    print(employee.salary)
    employee.who_am_i()

if __name__ == "__main__":
    main()
