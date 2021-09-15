import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'
import time

# lancement des modules inclus dans pygame
pygame.init() 

shrek = [pygame.image.load("shrek0.jpg"),pygame.image.load("shrek1.jpg")]
pygame.display.set_icon(pygame.image.load("shrek.png"))
clock = time.monotonic()
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Shrek Invaders")
# chargement de l'image de fond

font = pygame.font.SysFont('stencil', 100)
font1 = pygame.font.SysFont('stencil', 50)
sound_effect = pygame.mixer.Sound("musique.wav")
musique_trop_cool = pygame.mixer.music.load("super_musique.wav")

# creation du joueur
player = space.Joueur()
fond = pygame.image.load('shrek' + str(player.score % 2) + ".jpg")
tir = space.Balle(player)
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte
vitesse_jeu = 1
vitesse_max = 2
pygame.mixer.music.play(-1)

fichier_score = open("meilleur_score.txt", "r")
meilleur_score = fichier_score.readline()
fichier_score.close()

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    if vitesse_jeu<vitesse_max:
        vitesse_jeu += 0.00005
    tir.vitesse = vitesse_jeu
    player.vitesse = vitesse_jeu
    screen.fill((0,0,0))
    screen.blit(shrek[player.score % 2],(0,0))

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False

       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE and player.tir_etat == False : # espace pour tirer
                player.tir_etat = True
                tir = space.Balle(player)
                
                
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()

        if ennemi.est_mort:
            sound_effect.play()
            del listeEnnemis[listeEnnemis.index(ennemi)]
        
        if ennemi.hauteur >= 600-ennemi.image.get_size()[1]:
            running = False


    if player.tir_etat:
        tir.bouger()
        screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    
    if tir.hauteur <= 0:
        player.tir_etat = False
        tir = space.Balle(player)
    
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    
    player.deplacer()
    screen.blit(player.image,[player.position,500])

    if time.monotonic() - clock>=1/vitesse_jeu:
        clock = time.monotonic()
        listeEnnemis.append(space.Ennemi())

    if player.score>int(meilleur_score):
        meilleur_score=player.score

    screen.blit(font.render(str(player.score), True, (255,0,0)),(0,0))
    screen.blit(font1.render("Meilleur score : "+str(meilleur_score), True, (255, 0, 0)), (320, 0))
    pygame.display.update() # pour ajouter tout changement à l'

fichier_score = open("meilleur_score.txt", "w")
fichier_score.write(str(player.score))
fichier_score.close()
sys.exit()