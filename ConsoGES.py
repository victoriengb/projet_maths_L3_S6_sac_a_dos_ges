class ConsoGES :
    """ConsoGES est une classe qui représente un bien ou service produisant du Gaz à effet de serre (GES)"""

    #coutGES est un réel représentant le coût en GES de l'objet
    coutGES = 0.0

    #utilité est un entier représentant le niveau d'utilité de l'objet pour celui qui le consomme
    utilite = 0

    #description est la chaîne de caractères décrivant l'objet
    description = ""

    #Constructeur de la classe
    def __init__(self, coutGES, utilite, description) -> None :
        self.coutGES = coutGES
        self.utilite = utilite
        self.description = description

    #Renvoie le coût GES de l'objet ConsoGES
    def getCoutGES(self) -> float :
        return self.coutGES
    
    #Renvoie l'utilité de l'objet ConsoGES
    def getUtilite(self) -> int :
        return self.utilite

    #Renvoie une description textuelle de l'objet
    def __str__(self) -> str:
        return self.description + " a une utilité de : " + str(self.utilite) + " et un coût GES de : " + str(self.coutGES)