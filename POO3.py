class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        somme = self.nombre1 + self.nombre2
        print(somme)
initialisation = Operation(4, 5)
initialisation.addition()
initialisation2 = Operation( 8, 9)
initialisation2.addition()
