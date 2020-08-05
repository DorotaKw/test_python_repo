from sda_ex_oop_1_mz.animal import Animal
from sda_ex_oop_1_mz.cat import Cat
from sda_ex_oop_1_mz.dog import Dog


class Vet:

    def say_cat_hello(cat: Cat):
        print(f"Hello {cat.name}")

    def say_dog_hello(dog: Dog):
        print(f"Hello {dog.name}")

    def say_animal_hello(animal: Animal):
        print(f"Hello {animal.name}")