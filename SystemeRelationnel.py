class SystemeRelationnel :
    """La classe modélise des systèmes relationnels et offre des méthodes permettant de connaître leurs propriétés"""

    #La classe SystemeRelationnel a été créée en réponse à la question 6
    A_ensembleDesElementsDuSysteme = []
    R_relationBinaire = [()]
    
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
    
    #Question 7
    #Indique si le système relationnel est réflexif
    def estReflexive(self) -> bool :
        #On considère le système relationnel comme étant réflexif par défaut
        estReflexive = True

        #On parcourt les éléments présents dans l'ensemble A. NB : Le système relationnel SR = (A, R_Relation_binaire)
        for e in self.A_ensembleDesElementsDuSysteme :
            #Si un élément n'est pas en relation avec lui-même
            if not self.contientCoupleSacs(e, e) :
                #Il n'est pas réflexif
                estReflexive = False
                return estReflexive
        #Si tous les éléments sont en relation avec eux-mêmes, le système relationnel est réflexif
        return estReflexive
    
    #Question 7
    #Indique si le système relationnel est symétrique
    def estSymetrique(self) -> bool :
        #On considère le système relationnel comme étant symétrique par défaut
        estSymetrique = True
        #On parcourt les couples appartenant à la relation binaire
        for e in self.R_relationBinaire :
            #Si la propriété de symétrie n'est pas respectée
            if not self.contientCoupleSacs(e[1], e[0]) :
                #Le système relationnel n'est pas symétrique
                estSymetrique = False
                return estSymetrique
        #Si tous les couples de la relation binaire vérifient la propriété de symétrie alors le système relationnel est symétrique
        return estSymetrique
    
    #Question 7
    #Générer via Google Gemini car ma version avait une très mauvaise complexité
    #Indique si le système relationnel est transitif
    def estTransitive(self) -> bool :
        #Parcours des tuples de la relation - La syntaxe de la boucle for (et seulement elle) est inspirée d'un code de Google Gemini
        for a, b in self.R_relationBinaire:
            #Parcours des éléments de l'ensemble sur lequel porte la relation
            for c in self.A_ensembleDesElementsDuSysteme:
                #Contrôle si la transitivité est brisée
                if self.contientCoupleSacs(a, b) and self.contientCoupleSacs(b, c) and not self.contientCoupleSacs(a, c) :
                    #Si oui on retourne faux, i.e, la relation n'est pas transitive
                    return False

        #Si non on retourne vrai, i.e, la relation est transitive
        return True

    #Question 7
    #Générer via Google Gemini car ma version avait une très mauvaise complexité
    #Indique si le système relationnel est négativement transitif
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
    
    #Question 7
    #Indique si le système relationnel est antisymétrique
    def estAntisymetrique(self) -> bool :
        #On considère le système relationnel comme étant antisymétrique par défaut
        estAntisymetrique = True
        #On parcourt les couples appartenant à la relation binaire
        for e in self.R_relationBinaire :
            #Si la propriété d'antisymétrie n'est pas respectée
            if not e[0].estIdentique(e[1]) and self.contientCoupleSacs(e[1], e[0]) :
                #Le système relationnel n'est pas antisymétrique
                estAntisymetrique = False
                return estAntisymetrique
        #Si tous les couples de la relation binaire vérifient la propriété d'antisymétrie alors le système relationnel est antisymétrique
        return estAntisymetrique

    #Question 7
    #Indique si le système relationnel est asymétrique
    def estAsymetrique(self) -> bool :
        #On considère le système relationnel comme étant asymétrique par défaut
        estAsymetrique = True
        #On parcourt les couples appartenant à la relation binaire
        for e in self.R_relationBinaire :
            #Si la propriété d'asymétrie n'est pas respectée
            if (self.contientCoupleSacs(e[1], e[0])) :
                #Le système relationnel n'est pas asymétrique
                estAsymetrique = False
                return estAsymetrique
        #Si tous les couples de la relation binaire vérifient la propriété d'asymétrie alors le système relationnel est asymétrique
        return estAsymetrique

    #Question 7
    #Indique si le système relationnel est complet
    def estTotale(self) -> bool :
        #On considère le système relationnel comme étant complet par défaut
        estTotale = True
        #La double boucle for permet de déterminer tous les couples de sacs à dos possibles avec les éléments de l'ensemble A. NB : Le système relationnel SR = (A, R_Relation_binaire)
        for e1 in self.A_ensembleDesElementsDuSysteme :
            for e2 in self.A_ensembleDesElementsDuSysteme :
                #Si la propriété de complétude n'est pas respectée
                if(not e1.estIdentique(e2) and not self.contientCoupleSacs(e1, e2) and not self.contientCoupleSacs(e2, e1)):
                    #Le système relationnel n'est pas complet
                    estTotale = False
                    return estTotale
        #Si la propriété de complétude est vérifiée le système relationnel est complet
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