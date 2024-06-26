from ConsoGES import ConsoGES
from SacADosGES import SacADosGES
from SystemeRelationnel import SystemeRelationnel

import matplotlib.pyplot as plt
from itertools import product

"""Main est la classe qui exécute le programme"""

#Méthode exécutant le programme
def main () -> None :

    #Les listes ci-dessous répondent à la Question 2

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
    
    #_____________________________________________________

    #Question 5 - Ensemble des sacs à dos possibles
    listeSacsADos = getSacsADos(alimentation, transport,  logement,  consommation)
    
    #_____________________________________________________

    #Question 9 affichage front de Pareto
    #afficherFrontDePareto(listeSacsADos)

    #_____________________________________________________

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

    #_____________________________________________________

    #Initialisation du système relationnel de Pareto-dominance
    systemeRelationnel_PD = getSR_PD(listeSacsADos)
    #Initialisation du système relationnel lexicographique relatif aux coûts GES
    systemeRelationnel_LexC = getSR_LexC(listeSacsADos)
    #Initialisation du système relationnel lexicographique relatif aux utilités
    systemeRelationnel_LexU = getSR_LexU(listeSacsADos)
    #Initialisation du système relationnel borné
    systemeRelationnel_Borne = getSR_Borne(5.0, listeSacsADos)

    #_____________________________________________________

    #Question 12 - Temps d'exécution : 6min30s - Affiche les propriétés des systèmes relationnels

    #getProprietesSR(systemeRelationnel_PD)
    #print("_______________________________________")

    #getProprietesSR(systemeRelationnel_LexC)
    #print("_______________________________________")

    #getProprietesSR(systemeRelationnel_LexU)
    #print("_______________________________________")

    #getProprietesSR(systemeRelationnel_Borne)
    #print("_______________________________________")

    #_____________________________________________________

    #Question 14

    #Affichage des distances entre systèmes relationnels
    #print("La distance entre le système relationnel de Pareto-dominance et la relation lexicographique relative au coût GES est : " + str(systemeRelationnel_PD.distance(systemeRelationnel_LexC)))
    #print("La distance entre le système relationnel de Pareto-dominance et la relation lexicographique relative à l'utilité est : " + str(systemeRelationnel_PD.distance(systemeRelationnel_LexU)))
    #print("La distance entre la relation lexicographique relative à l'utilité et la relation lexicographique relative au coût GES est : " + str(systemeRelationnel_LexU.distance(systemeRelationnel_LexC)))
    
    
    #float_list correspond à des valeurs de bornes
    float_list = [float(x) for x in range(0, 26, 5)]
    float_list = [x / 2.0 for x in float_list]

    #liste contenant la distance entre le système relationnel lexicographique relatif aux coûts GES et le système relationnel borné (on fait varier la borne)
    distances_SR_Borne_SRLexC = []
    #liste contenant la distance entre le système relationnel lexicographique relatif aux utilités et le système relationnel borné (on fait varier la borne)
    distances_SR_Borne_SRLexU = []
    #liste contenant la distance entre le système relationnel de Pareto-dominance et le système relationnel borné (on fait varier la borne)
    distances_SR_Borne_SRPD = []

    #Distance avec le système relationnel borné en faisant varier la borne
    for B_borne in float_list :
        #On initialise le système relationnel borné avec la borne B_borne
        systemeRelationnel_Borne_Q13 = getSR_Borne(B_borne, listeSacsADos)
        
        #Ajout de la distance entre le système relationnel lexicographique relatif aux coûts GES et le système relationnel borné
        distances_SR_Borne_SRLexC.append(systemeRelationnel_Borne_Q13.distance(systemeRelationnel_LexC))
        #Ajout de la distance entre le système relationnel lexicographique relatif aux utilités et le système relationnel borné
        distances_SR_Borne_SRLexU.append(systemeRelationnel_Borne_Q13.distance(systemeRelationnel_LexU))
        #Ajout de la distance entre le système relationnel de Pareto-dominance et le système relationnel borné
        distances_SR_Borne_SRPD.append(systemeRelationnel_Borne_Q13.distance(systemeRelationnel_PD))

    #Affichage d'un graphique montrant en abscisse les bornes et en ordonnée la distance entre le système relationnel lexicographique relatif aux coûts GES et le système relationnel borné
    #plt.scatter(float_list, distances_SR_Borne_SRLexC)
    #plt.xlabel("Valeur de Borne")
    #plt.ylabel("Distance entre SR_Borne et SR_LexC")
    #plt.title("Distance entre le système relationnel borné et le système relationnel lexicographique relatif aux coûts GES")
    #plt.show()

    #Affichage d'un graphique montrant en abscisse les bornes et en ordonnée la distance entre le système relationnel lexicographique relatif aux utilités et le système relationnel borné
    #plt.scatter(float_list, distances_SR_Borne_SRLexU)
    #plt.xlabel("Valeur de Borne")
    #plt.ylabel("Distance entre SR_Borne et SR_LexU")
    #plt.title("Distance entre le système relationnel borné et le système relationnel lexicographique relatif à l'utilité")
    #plt.show()

    #Affichage d'un graphique montrant en abscisse les bornes et en ordonnée la distance entre le système relationnel de Pareto-dominance et le système relationnel borné
    plt.scatter(float_list, distances_SR_Borne_SRPD)
    plt.xlabel("Valeur de Borne")
    plt.ylabel("Distance entre SR_Borne et SR_PD")
    plt.title("Distance entre le système relationnel borné et le système relationnel de Pareto-dominance")
    plt.show()

    #_____________________________________________________
    
    #Question 16 - Affiche l'utilité optimale des sacs à dos du système relationnel borné en faisant varier la borne
    #afficherUtiliteOptimale(listeSacsADos)
 

#Question 5
#getSacADos prend une liste de consoGES concernant l'alimentation, le transport, le logement et la consommation de biens et services
#getSacADos renvoie une liste contenant l'ensemble des sacs à dos pouvant être conçus à partir des listes données en paramètres
#L'idée d'utiliser le produit cartésien product vient de ChatGPT
def getSacsADos(alimentation, transport, logement, consommation):

    listeElementSacsADos = list(product(alimentation, transport,  logement,  consommation))

    listeSacsADos = []
    for e in listeElementSacsADos:
        listeSacsADos.append(SacADosGES(e[0], e[1], e[2], e[3]))

    return listeSacsADos
    
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
            if (e1.coutGES < e2.coutGES and e1.utilite >= e2.utilite) or (e1.coutGES <= e2.coutGES and e1.utilite > e2.utilite) :
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
            if (e1.utilite > e2.utilite) or (e1.utilite == e2.utilite and e1.coutGES < e2.coutGES) :
                systemeRelationnelLexU.R_relationBinaire.append((e1, e2))
    return systemeRelationnelLexU

#Question 10
#getSR_LexC prend en entrée une liste de sacs à dos et renvoie un Système relationnel représentant la relation lexicographiqueC existant entre les divers sacs à dos
#Dans ce programme, la liste de sacs à dos est générée grâce à la méthode getSacsADos créée auparavant
def getSR_LexC(listeSacsADos) -> SystemeRelationnel :

    #Déclaration du système relationnel
    systemeRelationnelLexC = SystemeRelationnel(listeSacsADos, [])

    #les deux boucles for imbriquées permettent de considérer tous les couples de sacs à dos possibles
    for e1 in systemeRelationnelLexC.A_ensembleDesElementsDuSysteme :
        for e2 in systemeRelationnelLexC.A_ensembleDesElementsDuSysteme :
            #Le test conditionnel correspond à la définition de la relation lexicographiqueU
            if (e1.coutGES < e2.coutGES) or (e1.coutGES == e2.coutGES and e1.utilite > e2.utilite) :
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
            if (e1.coutGES <= B_borne and e2.coutGES > B_borne) or (e1.coutGES <= B_borne and e2.coutGES <= B_borne and e1.utilite > e2.utilite) :
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

#Question 15 - Renvoie l'utilité maximale d'un sac à dos dont le coût GES est inférieur à la borne

def utiliteMax(B_borne, listeSacsADos) :
    systemeRelationnel_Borne = getSR_Borne(B_borne, listeSacsADos)
    utiliteMax = 0

    for e in systemeRelationnel_Borne.R_relationBinaire :
        if(e[0].utilite > utiliteMax) :
            utiliteMax = e[0].utilite
    return utiliteMax

#Question 16 - Affiche un graphique montrant l'utilité maximale des sacs à dos dont le coût GES est inférieur à une borne qu'on fait varier
def afficherUtiliteOptimale(listeSacsADos) :
    liste_Bornes = [float(x) for x in range(0, 26, 5)]
    liste_Bornes = [x / 2.0 for x in liste_Bornes]

    liste_UtilitesMax = []

    for e in liste_Bornes :
        liste_UtilitesMax.append(utiliteMax(e, listeSacsADos))
    
    plt.scatter(liste_Bornes, liste_UtilitesMax)
    plt.xlabel("Borne")
    plt.ylabel("Utilité Maximale")
    plt.title("Utilité maximale en fonction de la borne")
    plt.show()

#Exécution de la fonction main qui lance l'entièreté du programme
main()