import datetime
import math
class Vehicule:
    def __init__(self, prix, date_immatriculation, marque, nom):
        self.prix = prix
        self.date_immatriculation = date_immatriculation
        self.marque = marque
        self.nom = nom
    
    def __str__(self):
        print("Le prix de base du véhicule est : " + str(self.prix) + "€")
        print("La date d'immatriculation est : " + str(self.date_immatriculation))
        print("La marque du véhicule est : " + str(self.marque))
        print("Le nom du véhicule est : " + str(self.nom)) 

    def get_current_price(self):
        lost = 0
        date_time_obj = datetime.datetime.strptime(self.date_immatriculation, '%Y-%m-%d')
        c = datetime.datetime.now() - date_time_obj
        if c.days >= 30:
            lost = c.days / 30
            lost = round(lost)
            prix = self.prix - (self.prix * 0.002) 
            while lost > 1:
                prix = prix - math.floor((prix * 0.002))
                lost=lost-1 
        else:
            prix=self.prix
        print("La valeur actuelle de votre véhicule est :" + str(prix) + "€")

class Camion(Vehicule):
    def get_current_price(self):
        lost = 0
        date_time_obj = datetime.datetime.strptime(self.date_immatriculation, '%Y-%m-%d')
        c = datetime.datetime.now() - date_time_obj
        if c.days >= 60:
            lost = c.days / 60
            lost = round(lost)
            prix = self.prix - (self.prix * 0.004) 
            while lost > 1:
                prix = prix - math.floor((prix * 0.004))
                lost=lost-1 
        else:
            prix=self.prix
        print("La valeur actuelle de votre véhicule est :" + str(prix) + "€")

class Camion(Vehicule):
    def get_current_price(self):
        lost = 0
        date_time_obj = datetime.datetime.strptime(self.date_immatriculation, '%Y-%m-%d')
        c = datetime.datetime.now() - date_time_obj
        if c.days >= 60:
            lost = c.days / 60
            lost = round(lost)
            prix = self.prix - (self.prix * 0.004) 
            while lost > 1:
                prix = prix - math.floor((prix * 0.004))
                lost=lost-1 
        else:
            prix=self.prix
        print("La valeur actuelle de votre véhicule est :" + str(prix) + "€")

v = Camion(marque="Peugeot", nom="206", date_immatriculation='2020-11-01', prix=2000)
v.get_current_price()

