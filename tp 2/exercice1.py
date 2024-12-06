class Chien():
    def __init__(self,name,race,age):
        self.name=name
        self.race=race
        self.age=age
    def aboyer(self):
        print(f"Woof {self.name}")




chien1 = Chien("ch1",10,"ra1")

chien1.aboyer()