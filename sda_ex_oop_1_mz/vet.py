from sda_ex_oop_1_mz.animal import Animal
from sda_ex_oop_1_mz.cat import Cat
from sda_ex_oop_1_mz.dog import Dog


class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat):
        print(f"Hello {cat.name}")

    @staticmethod
    def say_dog_hello(dog: Dog):
        print(f"Hello {dog.name}")

    @staticmethod
    def say_animal_hello(animal: Animal):
        print(f"Hello {animal.name}")