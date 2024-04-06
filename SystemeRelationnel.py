class SystemeRelationnel :
    """La classe modélise des systèmes relationnels et offre des méthodes permettant de connaître leurs propriétés"""

    A_ensembleDesElementsDuSysteme = []
    R_relationBinaire = [()]

    def __init__(self, A_ensembleDesElementsDuSysteme, R_relationBinaire) -> None :
        self.A_ensembleDesElementsDuSysteme = A_ensembleDesElementsDuSysteme
        self.R_relationBinaire = R_relationBinaire
    
    def estReflexive(self) -> bool :
        estReflexive = True

        for e in self.A_ensembleDesElementsDuSysteme :
            if not ((e, e) in self.R_relationBinaire) :
                estReflexive = False
                return estReflexive
        return estReflexive
    
    def estSymetrique(self) -> bool :
        estSymetrique = True
        for e in self.R_relationBinaire :
            if not ((e[1], [0]) in self.R_relationBinaire) :
                estSymetrique = False
                return estSymetrique
        return estSymetrique
    
    def estTransitive(self) -> bool :
        estTransitive = True
        for a in self.A_ensembleDesElementsDuSysteme :
            for b in self.A_ensembleDesElementsDuSysteme :
                for c in self.A_ensembleDesElementsDuSysteme :
                    if (a, b) in self.R_relationBinaire and (b, c) in self.R_relationBinaire and not (a, c) in self.R_relationBinaire :
                        estTransitive = False
                        return estTransitive
        return estTransitive
    
    def estNegativementTransitive(self) -> bool :
        estNegativementTransitive = True
        for a in self.A_ensembleDesElementsDuSysteme :
            for b in self.A_ensembleDesElementsDuSysteme :
                for c in self.A_ensembleDesElementsDuSysteme :
                    if (a, b) not in self.R_relationBinaire and (b, c) not in self.R_relationBinaire and (a, c) in self.R_relationBinaire :
                        estNegativementTransitive = False
                        return estNegativementTransitive
        return estNegativementTransitive
    
    def estAntisymetrique(self) -> bool :
        estAntisymetrique = True
        for e in self.R_relationBinaire :
            if ((e[1], [0]) in self.R_relationBinaire) and (e[0] != e[1]) :
                estAntisymetrique = False
                return estAntisymetrique
        return estAntisymetrique
    
    def estAsymetrique(self) -> bool :
        estAsymetrique = True
        for e in self.R_relationBinaire :
            if ((e[1], [0]) in self.R_relationBinaire) :
                estAsymetrique = False
                return estAsymetrique
        return estAsymetrique

    def __str__(self) -> str:
        return "Le système relationnel est composé de la relation binaire : " + str(self.R_relationBinaire)
    
        #Ancienne description textuelle : trop détaillée
        #return "Le système relationnel est composé des éléments : " + str(self.A_ensembleDesElementsDuSysteme) + " et de la relation binaire : " + str(self.R_relationBinaire)