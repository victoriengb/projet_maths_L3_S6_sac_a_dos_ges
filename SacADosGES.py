from ConsoGES import ConsoGES

class SacADosGES :
    """Un sac à dos GES représente les biens et services consommés par une personne"""

    #objet ConsoGES correspondant aux consommations possibles
    consommation = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux alimentations possibles
    alimentation = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux transports possibles
    transport = ConsoGES(0.0, 0, "")
    #objet ConsoGES correspondant aux logements possibles
    logement = ConsoGES(0.0, 0, "")

    #Constructeur de la classe SacADosGES qui prend des paramètres ConsoGES liés aux différents postes de consommation
    def __init__(self, consommation, alimentation, transport, logement) -> None:
        self.consommation = consommation
        self.alimentation = alimentation
        self.transport = transport
        self.logement = logement

    #Méthode renvoyant le coût GES total du sac
    def getCoutGES(self) -> float :
        return round(self.consommation.getCoutGES() + self.alimentation.getCoutGES() + self.transport.getCoutGES() + self.logement.getCoutGES(), 1)

    #Méthode renvoyant l'utilité totale du sac
    def getUtilite(self) -> int :
        return self.consommation.getUtilite() + self.alimentation.getUtilite() + self.transport.getUtilite() + self.logement.getUtilite()
    
    #Détermine si le sac est valide, i.e, son coût GES est inférieur à la borne passée en paramètre ou s'il est invalide
    def estValide(self, B_borne) -> bool :
        return self.getCoutGES() <= B_borne
    
    #Renvoie une description textuelle de l'objet
    def __str__(self) -> str:
        return "Le sac à dos est composé de : " + "\n" + self.consommation.__str__() + "\n" + self.alimentation.__str__() + "\n" + self.transport.__str__() + "\n" + self.logement.__str__()
    