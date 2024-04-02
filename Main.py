from ConsoGES import ConsoGES

class Main :

    def main () -> None :
        alimentation = [ConsoGES(2.2, 5, "Alimentation très carnée"), 
                        ConsoGES(1.2, 7, "Alimentation modérément carnée"),
                        ConsoGES(0.9, 6, "Alimentation végétarienne"),
                        ConsoGES(0.4, 4, "Alimentation végétalienne")]
        
        transport = [ConsoGES(3.0, 4, "Voiture thermique 5000km par année et personne"), 
                        ConsoGES(2.1, 6, "Voiture thermique 1000km par année et personne"),
                        ConsoGES(1.6, 5, "Voiture électrique 5000km par année et personne"),
                        ConsoGES(0.3, 3, "Mobilité douce")]
        
        logement = [ConsoGES(3.0, 7, "Logement mal isolé 60m^2"), 
                        ConsoGES(0.2, 6, "Logement très bien isolé 40m^2 modérément carnée")]
        
        consommation = [ConsoGES(2.5, 10, "Consommation importante de bien et services"), 
                        ConsoGES(1.3, 6, "Consommation sobre de bien et services")]

Main.main()