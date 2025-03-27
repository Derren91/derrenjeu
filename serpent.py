import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Taille des blocs
taille_bloc = 20
vitesse = 15

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Serpent")

horloge = pygame.time.Clock()

# Police pour le score
police_score = pygame.font.SysFont("comicsansms", 35)

def afficher_score(score):
    valeur = police_score.render("Score: " + str(score), True, bleu)
    fenetre.blit(valeur, [0, 0])

def jeu():
    game_over = False
    game_close = False

    x1 = largeur / 2
    y1 = hauteur / 2

    x1_change = 0
    y1_change = 0

    corps_serpent = []
    longueur_serpent = 1

    # Position aléatoire de la pomme
    pomme_x = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
    pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0

    while not game_over:

        while game_close:
            fenetre.fill(noir)
            message = pygame.font.SysFont("comicsansms", 50).render("Perdu! Appuyez sur Q-Quitter ou C-Continuer", True, rouge)
            fenetre.blit(message, [largeur / 6, hauteur / 3])
            afficher_score(longueur_serpent - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_bloc
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_bloc
                    x1_change = 0

        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, vert, [pomme_x, pomme_y, taille_bloc, taille_bloc])
        corps_serpent.append([x1, y1])
        if len(corps_serpent) > longueur_serpent:
            del corps_serpent[0]

        for bloc in corps_serpent[:-1]:
            if bloc == [x1, y1]:
                game_close = True

        for bloc in corps_serpent:
            pygame.draw.rect(fenetre, blanc, [bloc[0], bloc[1], taille_bloc, taille_bloc])

        afficher_score(longueur_serpent - 1)
        pygame.display.update()

        if x1 == pomme_x and y1 == pomme_y:
            pomme_x = round(random.randrange(0, largeur - taille_bloc) / 20.0) * 20.0
            pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 20.0) * 20.0
            longueur_serpent += 1

        horloge.tick(vitesse)

    pygame.quit()
    quit()

jeu()