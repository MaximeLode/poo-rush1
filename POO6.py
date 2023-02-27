class Animal:
    def __init__(self,age, prenom):
        self.age = age
        self.prenom = prenom
        print("l'age de l'animal",self.age,"ans")
    def viellir(self):
        self.grandir = self.age + 1
        print("l'age de l'animal",self.grandir,"ans")
    def nommer(self,afficher):
        self.afficher = afficher
        print("L'animal se nomme",self.afficher)

init = Animal(0,"")
init.viellir()
init.nommer("Luna")