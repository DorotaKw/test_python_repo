from sda_ex_oop_1_mz.animal import Animal
from sda_ex_oop_2_mz.canidae import Canidae
from sda_ex_oop_2_mz.mammal import Mammal


class Dog(Animal, Mammal, Canidae):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> str:
        return f"{self.name} hau"
