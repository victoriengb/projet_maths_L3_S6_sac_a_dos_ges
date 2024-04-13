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
            if not ((e[1], e[0]) in self.R_relationBinaire) :
                estSymetrique = False
                return estSymetrique
        return estSymetrique
    
    #Générer via Google Bard car ma version avait une très mauvaise complexité
    def estTransitive(self) -> bool :
        #Passage d'une liste de tuple à un ensemble - généré par Google Bard probablement pour des raisons de complexité dans les opération
        relation_set = set(self.R_relationBinaire)

        #Parcours des tuples de la relation
        for a, b in self.R_relationBinaire:
            #Parcours des éléments de l'ensemble sur lequel porte la relation
            for c in self.A_ensembleDesElementsDuSysteme:
                #Contrôle si la transitivité est brisée
                if (a, b) in relation_set and (b, c) in relation_set and (a, c) not in relation_set:
                    #Si oui on retourne faux, i.e, la relation n'est pas transitive
                    return False

        #Si non on retourne vrai, i.e, la relation est transitive
        return True

        """
        Fait par moi

        estTransitive = True
        for a in self.A_ensembleDesElementsDuSysteme :
            for b in self.A_ensembleDesElementsDuSysteme :
                for c in self.A_ensembleDesElementsDuSysteme :
                    if (a, b) in self.R_relationBinaire and (b, c) in self.R_relationBinaire and not (a, c) in self.R_relationBinaire :
                        estTransitive = False
                        return estTransitive
        """

    #Générer via Google Bard car ma version avait une très mauvaise complexité
    def estNegativementTransitive(self) -> bool :
        
        #Passage d'une liste de tuple à un ensemble - généré par Google Bard probablement pour des raisons de complexité dans les opération
        relation_set = set(self.R_relationBinaire)

        #Parcours des tuples de la relation
        for a, b in self.R_relationBinaire:
            #Parcours des éléments de l'ensemble sur lequel porte la relation
            for c in self.A_ensembleDesElementsDuSysteme:
                #Contrôle si la transitivité négative est brisée
                if (a, b) not in relation_set and (b, c) not in relation_set and (a, c) in relation_set :
                    #Si oui on retourne faux, i.e, la relation n'est pas négativement transitive
                    return False
        #Si non on retourne vrai, i.e, la relation est négativement transitive
        return True
    
        """
        Fait par moi
        estNegativementTransitive = True
        for a in self.A_ensembleDesElementsDuSysteme :
            for b in self.A_ensembleDesElementsDuSysteme :
                for c in self.A_ensembleDesElementsDuSysteme :
                    if (a, b) not in self.R_relationBinaire and (b, c) not in self.R_relationBinaire and (a, c) in self.R_relationBinaire :
                        estNegativementTransitive = False
                        return estNegativementTransitive
        return estNegativementTransitive
        """
    
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

    def estTotale(self) -> bool :
        estTotale = True
        for e1 in self.A_ensembleDesElementsDuSysteme :
            for e2 in self.A_ensembleDesElementsDuSysteme :
                if (e1 != e2 and ((e1, e2) not in self.R_relationBinaire) and ((e2, e1) not in self.R_relationBinaire)) :
                    estTotale = False
                    return estTotale
        return estTotale
    
    #Question 13
    #Renvoie la distance séparant deux systèmes relationnels
    #la formule pour déterminer la distance entre deux systèmes relationnels est définie dans l'énoncé du projet
    def distance(self, systemeRelationnel2) -> float :
        distance = 0.0
        if(isinstance(systemeRelationnel2, SystemeRelationnel)) :
            for e in self.R_relationBinaire :
                if(not e[0].__eq__(e[1]) and (e not in systemeRelationnel2.R_relationBinaire)) :
                    distance += 0.5
            for e in systemeRelationnel2.R_relationBinaire :
                if(not e[0].__eq__(e[1]) and (e not in self.R_relationBinaire)) :
                    distance += 0.5
        return distance
    
    def __str__(self) -> str:
        return "Le système relationnel est composé de la relation binaire : " + str(self.R_relationBinaire)
    
        #Ancienne description textuelle : trop détaillée
        #return "Le système relationnel est composé des éléments : " + str(self.A_ensembleDesElementsDuSysteme) + " et de la relation binaire : " + str(self.R_relationBinaire)