from ConsoGES import ConsoGES
from SacADosGES import SacADosGES
from SystemeRelationnel import SystemeRelationnel

import matplotlib.pyplot as plt

"""Main est la classe qui exécute le programme"""

#Méthode exécutant le programme
def main () -> None :
    #Liste des postes d'alimentation possibles dans le programme
    alimentation = [ConsoGES(2.2, 5, "Alimentation très carnée"), 
                    ConsoGES(1.2, 7, "Alimentation modérément carnée"),
                    ConsoGES(0.9, 6, "Alimentation végétarienne"),
                    ConsoGES(0.4, 4, "Alimentation végétalienne")]
    
    #Liste des postes de transport possibles dans le programme 
    transport = [ConsoGES(3.0, 4, "Voiture thermique 5000km par année et personne"), 
                    ConsoGES(2.1, 6, "Voiture thermique 1000km par année et personne"),
                    ConsoGES(1.6, 5, "Voiture électrique 5000km par année et personne"),
                    ConsoGES(0.3, 3, "Mobilité douce")]
    
    #Liste des postes de logement possibles dans le programme
    logement = [ConsoGES(3.0, 7, "Logement mal isolé 60m^2"), 
                    ConsoGES(0.2, 6, "Logement très bien isolé 40m^2 modérément carnée")]
    
    #Liste des postes de consommation de biens et services possibles dans le programme
    consommation = [ConsoGES(2.5, 10, "Consommation importante de bien et services"), 
                    ConsoGES(1.3, 6, "Consommation sobre de bien et services")]
    
    listeSacsADos = getSacsADos(alimentation, transport,  logement,  consommation)

    #Question 9 affichage front de Pareto
    #afficherFrontDePareto(listeSacsADos)

    #TEST getSR_PD
    #print(getSR_PD(listeSacsADos).R_relationBinaire[0][0].__str__() + "\n" + getSR_PD(listeSacsADos).R_relationBinaire[0][1].__str__())
    
    #TEST getSR_LexC
    #print(getSR_LexC(listeSacsADos).R_relationBinaire[0][0].__str__() + "\n" + getSR_LexC(listeSacsADos).R_relationBinaire[0][1].__str__())

    #TEST getSR_LexU
    #print(getSR_LexU(listeSacsADos).R_relationBinaire[0][0].__str__() + "\n" + getSR_LexU(listeSacsADos).R_relationBinaire[0][1].__str__())

    #TEST getSR_Borne
    #print(getSR_Borne(5.0, listeSacsADos).R_relationBinaire[0][0].__str__() + "\n" + getSR_Borne(5.0, listeSacsADos).R_relationBinaire[0][1].__str__())

    #TEST filtre
    #nouvelle_listeSacsADos = filtre(0.0, listeSacsADos)

    #Question 12
    #systemeRelationnelPD = getSR_PD(listeSacsADos)
    #getProprietesSR(systemeRelationnelPD)
    
    #getProprietesSR(getSR_Borne(5.0, listeSacsADos))
    print(getSR_Borne(5.0, listeSacsADos).estTotale())

#Question 5
#getSacADos prend une liste de consoGES concernant l'alimentation, le transport, le logement et la consommation de biens et services
#getSacADos renvoie une liste contenant l'ensemble des sacs à dos pouvant être conçus à partir des listes données en paramètres
def getSacsADos(alimentation, transport, logement, consommation):
    listeSacsADos = [SacADosGES(ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""))]

    #Chaque usage de append est positionné dans la boucle la plus interne concernant les éléments consoGES ajoutés dans le sac à dos
    #e.g : lorsqu'on append un élément de consommation, on le met dans la boucle for concernant les éléments c de consommation
    #cela permet d'éviter les doublons
    for a in alimentation :
        listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), a, ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, "")))

        for t in transport :
            listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), t, ConsoGES(0.0, 0, "")))
            listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), a, t, ConsoGES(0.0, 0, "")))

            for l in logement :
                listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), l))
                listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), a, ConsoGES(0.0, 0, ""), l))
                listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), t, l))
                listeSacsADos.append(SacADosGES(ConsoGES(0.0, 0, ""), a, t, l))

                for c in consommation :
                    #(consommation, alimentation, transport, logement)
                    listeSacsADos.append(SacADosGES(c, ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, "")))
                    listeSacsADos.append(SacADosGES(c, a, ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, "")))
                    listeSacsADos.append(SacADosGES(c, ConsoGES(0.0, 0, ""), t, ConsoGES(0.0, 0, "")))
                    listeSacsADos.append(SacADosGES(c, ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), l))

                    listeSacsADos.append(SacADosGES(c, a, t, ConsoGES(0.0, 0, "")))
                    listeSacsADos.append(SacADosGES(c, a, ConsoGES(0.0, 0, ""), l))
                    listeSacsADos.append(SacADosGES(c, ConsoGES(0.0, 0, ""), t, l))

                    listeSacsADos.append(SacADosGES(c, a, t, l))             
    
    return list(listeSacsADos)

#Question 5
#Générer partiellement via Google Bard car le même raisonnement avec une boucle for ne fonctionnait pas à cause d'un problème d'indexation
#La méthode filtre copie la liste de sacs à dos pour ne pas la modifier puis la parcourt grâce à une boucle while tout en supprimant les sacs à dos non valide
def filtre(B_borne, listeSacsADos) :
    #définir une nouvelle liste permet de ne pas modifier celle passée en paramètre
    nouvelle_liste = listeSacsADos.copy()
    
    i = 0
    #Tant qu'on n'a pas entièrement parcouru la liste on retire les sacs non valides
    while i < len(nouvelle_liste):
        e = nouvelle_liste[i]
        #On ne modifie pas la valeur de i dans le if sinon on obtient un problème d'indexation
        if not e.estValide(B_borne):
            nouvelle_liste.pop(i)
        #Le else est crucial sinon on a un problème d'indexation
        else:
            i += 1
    return nouvelle_liste

#Question 8
#getSR_PD prend en entrée une liste de sacs à dos et renvoie un Système relationnel représentant la relation de Pareto dominance existant entre les divers sacs à dos
#Dans ce programme, la liste de sacs à dos est générée grâce à la méthode getSacsADos créée auparavant
def getSR_PD(listeSacsADos) -> SystemeRelationnel :

    #Déclaration du système relationnel
    systemeRelationnelPD = SystemeRelationnel(listeSacsADos, [])

    #les deux boucles for imbriquées permettent de considérer tous les couples de sacs à dos possibles
    for e1 in systemeRelationnelPD.A_ensembleDesElementsDuSysteme :
        for e2 in systemeRelationnelPD.A_ensembleDesElementsDuSysteme :
            #Le test conditionnel correspond à la définition de la Pareto-dominance
            if (e1.getCoutGES() < e2.getCoutGES() and e1.getUtilite() >= e2.getUtilite()) or (e1.getCoutGES() <= e2.getCoutGES() and e1.getUtilite() > e2.getUtilite()) :
                systemeRelationnelPD.R_relationBinaire.append((e1, e2))
    return systemeRelationnelPD

#Question 9
#Usage de Matplotlib généré par Google Bard
#Affiche les sacs à dos non Pareto-dominés avec le coût GES en abscisse et l'utilité en ordonnée
def afficherFrontDePareto(listeSacsADos) -> (None) :
    #Obtention du système relationnel de Pareto-dominance
    systemeRelationnelPD = getSR_PD(listeSacsADos)

    #Déclaration de la liste contenant les sacs non Pareto dominés
    sacsNonDomines = []
    #On parcourt l'ensemble des sacs appartenant au Système relationnel
    for e in systemeRelationnelPD.A_ensembleDesElementsDuSysteme :
        #On considère que chaque sac du Système est par défaut non Pareto-dominés
        sacsNonDomines.append(e)
        #On parcourt les couples appartenant à la relation binaire de Pareto-dominance
        for couplePD in systemeRelationnelPD.R_relationBinaire :
            #Si un sac est Pareto-dominé, on le retire des sacs non Pareto-dominés
            if e == couplePD[1] and e in sacsNonDomines :
                sacsNonDomines.remove(e)
    #On initialise la liste contenant les valeurs de coûts GES des sacs non Pareto-dominés
    listeCoutsGES = [sac.getCoutGES() for sac in sacsNonDomines]
    #On initialise la liste contenant les valeurs d'utilité des sacs non Pareto-dominés
    listeUtilites = [sac.getUtilite() for sac in sacsNonDomines]

    #On crée le graphe et on l'affiche
    plt.scatter(listeCoutsGES, listeUtilites)
    plt.xlabel("Coût GES")
    plt.ylabel("Utilité")
    plt.title("Front de Pareto")
    plt.show()

#Question 10
#getSR_LexU prend en entrée une liste de sacs à dos et renvoie un Système relationnel représentant la relation lexicographiqueU existant entre les divers sacs à dos
#Dans ce programme, la liste de sacs à dos est générée grâce à la méthode getSacsADos créée auparavant
def getSR_LexU(listeSacsADos) -> SystemeRelationnel :

    #Déclaration du système relationnel
    systemeRelationnelLexU = SystemeRelationnel(listeSacsADos, [])

    #les deux boucles for imbriquées permettent de considérer tous les couples de sacs à dos possibles
    for e1 in systemeRelationnelLexU.A_ensembleDesElementsDuSysteme :
        for e2 in systemeRelationnelLexU.A_ensembleDesElementsDuSysteme :
            #Le test conditionnel correspond à la définition de la relation lexicographiqueU
            if (e1.getUtilite() > e2.getUtilite()) or (e1.getUtilite() == e2.getUtilite() and e1.getCoutGES() < e2.getCoutGES()) :
                systemeRelationnelLexU.R_relationBinaire.append((e1, e2))
    return systemeRelationnelLexU

#Question 10
#getSR_LexU prend en entrée une liste de sacs à dos et renvoie un Système relationnel représentant la relation lexicographiqueC existant entre les divers sacs à dos
#Dans ce programme, la liste de sacs à dos est générée grâce à la méthode getSacsADos créée auparavant
def getSR_LexC(listeSacsADos) -> SystemeRelationnel :

    #Déclaration du système relationnel
    systemeRelationnelLexC = SystemeRelationnel(listeSacsADos, [])

    #les deux boucles for imbriquées permettent de considérer tous les couples de sacs à dos possibles
    for e1 in systemeRelationnelLexC.A_ensembleDesElementsDuSysteme :
        for e2 in systemeRelationnelLexC.A_ensembleDesElementsDuSysteme :
            #Le test conditionnel correspond à la définition de la relation lexicographiqueU
            if (e1.getCoutGES() < e2.getCoutGES()) or (e1.getCoutGES() == e2.getCoutGES() and e1.getUtilite() > e2.getUtilite()) :
                systemeRelationnelLexC.R_relationBinaire.append((e1, e2))
    return systemeRelationnelLexC

#Question 11
#getSR_Borne prend en entrée une borne B_borne (flotant) et une liste de sacs à dos et renvoie un Système relationnel représentant la relation bornée de borne B_borne existant entre les divers sacs à dos
#Dans ce programme, la liste de sacs à dos est générée grâce à la méthode getSacsADos créée auparavant
def getSR_Borne(B_borne, listeSacsADos) -> SystemeRelationnel :
    #Déclaration du système relationnel
    systemeRelationnelBorne_B = SystemeRelationnel(listeSacsADos, [])

    #les deux boucles for imbriquées permettent de considérer tous les couples de sacs à dos possibles
    for e1 in systemeRelationnelBorne_B.A_ensembleDesElementsDuSysteme :
        for e2 in systemeRelationnelBorne_B.A_ensembleDesElementsDuSysteme :
            #Le test conditionnel correspond à la définition de la relation bornée de borne B
            if (e1.getCoutGES() <= B_borne and e2.getCoutGES() > B_borne) or (e1.getCoutGES() <= B_borne and e2.getCoutGES() <= B_borne and e1.getUtilite() > e2.getUtilite()) :
                systemeRelationnelBorne_B.R_relationBinaire.append((e1, e2))
    return systemeRelationnelBorne_B

#Question 12
#getProprieteSR prend en entrée un système relationnel et affiche ses propriétés sur la console
def getProprietesSR(systemeRelationnel) -> None:
    if(systemeRelationnel.estReflexive()) :
        print("Le système relationnel est réflexif")

    if(systemeRelationnel.estSymetrique()) :
        print("Le système relationnel est symétrique")

    if(systemeRelationnel.estTransitive()) :
        print("Le système relationnel est transitif")

    if(systemeRelationnel.estNegativementTransitive()) :
        print("Le système relationnel est négativement transitif")

    if(systemeRelationnel.estAntisymetrique()) :
        print("Le système relationnel est antisymétrique")

    if(systemeRelationnel.estAsymetrique()) :
        print("Le système relationnel est asymétrique")
    
    if(systemeRelationnel.estTotale()) :
        print("Le système relationnel est total")

main()