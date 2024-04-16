class SystemeRelationnel :
    """La classe modélise des systèmes relationnels et offre des méthodes permettant de connaître leurs propriétés"""

    A_ensembleDesElementsDuSysteme = []
    R_relationBinaire = [()]
    #R_relationBinaire = {()}
    
    def __init__(self, A_ensembleDesElementsDuSysteme, R_relationBinaire) -> None :
        self.A_ensembleDesElementsDuSysteme = A_ensembleDesElementsDuSysteme
        self.R_relationBinaire = R_relationBinaire
    
    #Permet de vérifier si un couple de sac à dos appartient à la relation binaire sans passer par l'opérateur d'appartenance in pour raison de complexité et de logique
    #En effet, l'opérateur in utilise la méthode __eq__ de la classe SacADosGES, ce qui ne donne pas le résultat attendu et est très vorace en terme de complexité
    def contientCoupleSacs(self, sac1, sac2) -> bool :
        for e in self.R_relationBinaire :
            if(e[0].estIdentique(sac1) and e[1].estIdentique(sac2)) :
                return True
        return False
    
    def estReflexive(self) -> bool :
        estReflexive = True

        for e in self.A_ensembleDesElementsDuSysteme :
            if not self.contientCoupleSacs(e, e) :
                estReflexive = False
                return estReflexive
        return estReflexive
    
    def estSymetrique(self) -> bool :
        estSymetrique = True
        for e in self.R_relationBinaire :
            if not self.contientCoupleSacs(e[1], e[0]) :
                estSymetrique = False
                return estSymetrique
        return estSymetrique
    
    #Générer via Google Bard car ma version avait une très mauvaise complexité
    def estTransitive(self) -> bool :
        #Parcours des tuples de la relation - La syntaxe de la boucle for (et seulement elle) est inspirée d'un code de Google Bard
        for a, b in self.R_relationBinaire:
            #Parcours des éléments de l'ensemble sur lequel porte la relation
            for c in self.A_ensembleDesElementsDuSysteme:
                #Contrôle si la transitivité est brisée
                if self.contientCoupleSacs(a, b) and self.contientCoupleSacs(b, c) and not self.contientCoupleSacs(a, c) :
                    #Si oui on retourne faux, i.e, la relation n'est pas transitive
                    return False

        #Si non on retourne vrai, i.e, la relation est transitive
        return True

    #Générer via Google Bard car ma version avait une très mauvaise complexité
    def estNegativementTransitive(self) -> bool :
        
        #Parcours des tuples de la relation
        for a, b in self.R_relationBinaire:
            #Parcours des éléments de l'ensemble sur lequel porte la relation
            for c in self.A_ensembleDesElementsDuSysteme:
                #Contrôle si la transitivité négative est brisée
                if not self.contientCoupleSacs(a, b) and not self.contientCoupleSacs(b, c) and self.contientCoupleSacs(a, c) :
                    #Si oui on retourne faux, i.e, la relation n'est pas négativement transitive
                    return False
        #Si non on retourne vrai, i.e, la relation est négativement transitive
        return True
    
    def estAntisymetrique(self) -> bool :
        estAntisymetrique = True
        for e in self.R_relationBinaire :
            if not e[0].estIdentique(e[1]) and self.contientCoupleSacs(e[1], e[0]) :
                estAntisymetrique = False
                return estAntisymetrique
        return estAntisymetrique

    def estAsymetrique(self) -> bool :
        estAsymetrique = True
        for e in self.R_relationBinaire :
            if (self.contientCoupleSacs(e[1], e[0])) :
                estAsymetrique = False
                return estAsymetrique
        return estAsymetrique

    def estTotale(self) -> bool :
        estTotale = True
        for e1 in self.A_ensembleDesElementsDuSysteme :
            for e2 in self.A_ensembleDesElementsDuSysteme :
                if(not e1.estIdentique(e2) and not self.contientCoupleSacs(e1, e2) and not self.contientCoupleSacs(e2, e1)):
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
                if(not e[0].__eq__(e[1]) and (not systemeRelationnel2.contientCoupleSacs(e[0], e[1]))) :
                    distance += 0.5
            for e in systemeRelationnel2.R_relationBinaire :
                if(not e[0].__eq__(e[1]) and (not self.contientCoupleSacs(e[0], e[1]))) :
                    distance += 0.5
        
        return distance
    
    def __str__(self) -> str:
        return "Le système relationnel est composé de la relation binaire : " + str(self.R_relationBinaire)
    
        #Ancienne description textuelle : trop détaillée
        #return "Le système relationnel est composé des éléments : " + str(self.A_ensembleDesElementsDuSysteme) + " et de la relation binaire : " + str(self.R_relationBinaire)