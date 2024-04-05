from ConsoGES import ConsoGES
from SacADosGES import SacADosGES

from itertools import combinations, chain

#class Main :

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
    print(len(listeSacsADos))

    nouvelle_listeSacsADos = filtre(0.0, listeSacsADos)

    print(len(nouvelle_listeSacsADos))



#getSacADos prend une liste de consoGES concernant l'alimentation, le transport, le logement et la consommation de biens et services
#getSacADos renvoie une liste contenant l'ensemble des sacs à dos pouvant être conçus à partir des listes données en paramètres
def getSacsADos(alimentation, transport, logement, consommation):
    listeSacsADos = [SacADosGES(ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""), ConsoGES(0.0, 0, ""))]

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

#Générer partiellement via Google Bard car le même raisonnement avec une boucle for ne fonctionnait pas à cause d'un problème d'indexation
#La méthode filtre copie la liste de sacs à dos pour ne pas la modifier puis la parcourt grâce à une boucle while tout en supprimant les sacs à dos non valide
def filtre(B_borne, listeSacsADos) :
    nouvelle_liste = listeSacsADos.copy()
    
    i = 0
    while i < len(nouvelle_liste):
        e = nouvelle_liste[i]
        if not e.estValide(B_borne):
            nouvelle_liste.pop(i)
        #Le else est crucial sinon on a un problème d'indexation
        else:
            i += 1
    return nouvelle_liste

main()