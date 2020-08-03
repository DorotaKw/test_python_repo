from sda_ex_oop_1_mz.animal import Animal


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> str:
        return f"{self.name} hau"
