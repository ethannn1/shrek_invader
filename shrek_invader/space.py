import pygame  # necessaire pour charger les images et les sons
import random


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self,vitesse=1) :
        self.position = 0
        self.image = pygame.image.load("shrek.png")
        self.sens = ""
        self.score = 0
        self.tir_etat = False
        self.vitesse = vitesse
    def deplacer(self):
        if self.sens == "gauche" and self.position >= 0:
            self.position -= self.vitesse
        elif self.sens == "droite" and self.position + self.image.get_size()[0] <= 800:
            self.position += self.vitesse
    
    def marquer(self):
        self.score += 1
    
    
class Balle:
    def __init__(self, player,vitesse=1):
        self.tireur = player
        self.depart = player.position
        self.hauteur = 500
        self.image = pygame.image.load("ane.jpg")
        self.vitesse = vitesse
        
    def bouger(self):
        self.hauteur -= self.vitesse
    
    def toucher(self, ennemi):
        if ennemi.depart <= self.depart <= ennemi.depart + ennemi.image.get_size()[0] and ennemi.hauteur >= self.hauteur:
            return True
        elif ennemi.depart <= self.depart + self.image.get_size()[0] <= ennemi.depart + ennemi.image.get_size()[0] and ennemi.hauteur >= self.hauteur:
            return True
        return False
    

class Ennemi:
    
    NbEnnemis = 0
    
    def __init__(self):
        self.type = random.randint(1, 2)
        if self.type==1:
            self.image = pygame.image.load("mechant1.png")
        else:
            self.image = pygame.image.load("mechant2.jpg")
        self.depart = random.randint(0, 800 - self.image.get_size()[0])
        self.hauteur = 0
        self.vitesse = 0.1
        self.est_mort = False
        
    def avancer(self):
        self.hauteur += self.vitesse
        
    def disparaitre(self):
        Ennemi.NbEnnemis -= 1
        self.est_mort = True
    