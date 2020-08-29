from sda_ex_oop_1_mz.area_checker import AreaChecker
from sda_ex_oop_1_mz.car import Car
from sda_ex_oop_1_mz.cat import Cat
from sda_ex_oop_1_mz.dog import Dog
# from datetime import date
# from sda_ex_oop_2_mz.employee import Employee
# from sda_ex_oop_2_mz.manager import Manager
from sda_ex_oop_1_mz.figures import Rectangle, Circle, Triangle
from sda_ex_oop_1_mz.functions import sum_of_figures
from sda_ex_oop_1_mz.vet import Vet


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
    car = Car()
    car.move()
    Vet.say_cat_hello(cat)
    Vet.say_dog_hello(dog)
    Vet.say_animal_hello(animal)

    rectangle = Rectangle(12.0, 4.0)
    area = rectangle.get_area()
    print(f"Pole trójkąta to: {area}")

    circle = Circle(3.0)
    area_circle = circle.get_area()
    print(area_circle)

    triangle = Triangle(4.0, 3.0)
    area_triangle = triangle.get_area()
    print(area_triangle)
    figures = [rectangle, circle, triangle]
    suma = sum_of_figures(figures)
    print(suma)

    enough = AreaChecker.check_area(200.0, figures)
    print(enough)


if __name__ == "__main__":
    main()
