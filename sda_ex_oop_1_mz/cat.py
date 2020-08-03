from sda_ex_oop_1_mz.animal import Animal


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.eat = 0

    def make_sound(self) -> str:
        return f"{self.name} miau"

    def eat_mouse(self) ->None:
        self.eat += 1
        print(f"{self.name} zjadł {self.eat} myszy")

