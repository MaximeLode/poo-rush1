class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print("je suis", self.prenom, self.nom)
init = Personne("Doe", "John") 
init.SePresenter()
init2 = Personne("Dupond", "Jean")
init2.SePresenter()
    