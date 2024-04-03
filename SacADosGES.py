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

    def __str__(self) -> str:
        return "Le sac à dos est composé de : " + "\n" + self.consommation.__str__() + "\n" + self.alimentation.__str__() + "\n" + self.transport.__str__() + "\n" + self.logement.__str__()
    