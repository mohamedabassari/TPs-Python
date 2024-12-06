class Animal:
    def faire_bruit(self) :
        pass
class Chat(Animal):
    def faire_bruit(self):
        print("chat dit myaw myaw")
class Chien(Animal):
    def faire_bruit(self):
        print("chien dit woolf wolf")


ch1=Chat()
CH2=Chien()
ch1.faire_bruit()
CH2.faire_bruit()


        