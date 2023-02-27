class Personnage:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def Gauche(self):
        self.gauche = self.y + 1
    def Droite(self):
        self.droite = self.y - 1

init = Personnage(10,30)
