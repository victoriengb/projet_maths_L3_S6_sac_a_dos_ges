from ConsoGES import ConsoGES

class SacADosGES :
    """Un sac à dos GES représente les biens et services consommés par une personne"""

    #La classe SacADos GES a été créée en réponse à la Question 3
    #objet ConsoGES correspondant aux consommations possibles
    consommation = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux alimentations possibles
    alimentation = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux transports possibles
    transport = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux logements possibles
    logement = ConsoGES(0.0, 0, "")

    #coutGES est un réel représentant le coût total en GES du sac
    coutGES = 0.0
    #utilité est un entier représentant le niveau d'utilité total du sac
    utilite = 0

    #Constructeur de la classe SacADosGES qui prend des paramètres ConsoGES liés aux différents postes de consommation
    def __init__(self, alimentation, transport, logement, consommation) -> None:
        self.consommation = consommation
        self.alimentation = alimentation
        self.transport = transport
        self.logement = logement

        self.coutGES = self.getCoutGES()
        self.utilite = self.getUtilite()

    #Question 4
    #Méthode renvoyant le coût GES total du sac
    def getCoutGES(self) -> float :
        return round(self.consommation.getCoutGES() + self.alimentation.getCoutGES() + self.transport.getCoutGES() + self.logement.getCoutGES(), 1)

    #Question 4
    #Méthode renvoyant l'utilité totale du sac
    def getUtilite(self) -> int :
        return self.consommation.getUtilite() + self.alimentation.getUtilite() + self.transport.getUtilite() + self.logement.getUtilite()
    
    #Question 4
    #Détermine si le sac est valide, i.e, son coût GES est inférieur à la borne passée en paramètre ou s'il est invalide
    def estValide(self, B_borne) -> bool :
        return self.getCoutGES() <= B_borne
    
    #Question 13
    #Nouvelle implémentation de la méthode __eq__
    #Indique si le sac à dos appelant la méthode à la même utilité et le même coût GES que le sac à dos donné en paramètre
    def __eq__(self, sac2) -> bool:
        if(isinstance(sac2, SacADosGES)) :
            return self.coutGES == sac2.coutGES and self.utilite == sac2.utilite
    
    #estIdentique vérifie si deux sacs à dos sont exactement les mêmes - Remplace parfois la méthode __eq__ qui peut ne pas avoir le comportement attendu
    def estIdentique(self, sacADos2) :
        if(isinstance(sacADos2, SacADosGES)) :
            return self.alimentation == sacADos2.alimentation and self.consommation == sacADos2.consommation and self.logement == sacADos2.logement and self.transport == sacADos2.transport

    #Renvoie une description textuelle de l'objet
    def __str__(self) -> str:

        return "Le sac à dos à une utilité de : " + str(self.utilite) + " et un coût GES total de : " + str(self.coutGES)
        #Ancienne description textuelle : pas assez informative
        #return "Le sac à dos est composé de : " + "\n" + self.consommation.__str__() + "\n" + self.alimentation.__str__() + "\n" + self.transport.__str__() + "\n" + self.logement.__str__()
    