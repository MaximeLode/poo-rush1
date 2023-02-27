from random import randint

class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print("x est en coordonnées",self.x,"y est en coordonnées", self.y)
    def afficherX(self):
        print("x =",self.x)
    def afficherY(self):
        print("y =",self.y)
    def ChangerX(self, valeur):
        self.valeur = valeur 
        self.xx = self.x + valeur
        print("x est egal maintenant a", self.xx)
    def ChangerY(self, valeur):
        self.valeur = valeur
        self.yy = self.y * valeur
        print("y est egal maintenant a", self.yy)
init = Point(12, 34)
init.afficherLesPoints()
init.afficherX()
init.afficherY()
init.ChangerX(valeur=randint(1,100))
init.ChangerY(valeur=randint(1,100))