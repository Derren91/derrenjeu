import pygame
import sys
import random

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 600, 600
taille_case = largeur // 3

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de Morpion (XO)")

# Police pour le texte
police = pygame.font.SysFont("comicsansms", 50)

# Grille de jeu
grille = [[" " for _ in range(3)] for _ in range(3)]
joueur_actuel = "X"
mode_ia = True  # Activer/désactiver l'IA


def dessiner_grille():
    """Dessine la grille du jeu."""
    fenetre.fill(blanc)
    for i in range(1, 3):
        # Lignes horizontales
        pygame.draw.line(fenetre, noir, (0, i * taille_case), (largeur, i * taille_case), 5)
        # Lignes verticales
        pygame.draw.line(fenetre, noir, (i * taille_case, 0), (i * taille_case, hauteur), 5)


def dessiner_symboles():
    """Dessine les symboles X et O sur la grille."""
    for ligne in range(3):
        for colonne in range(3):
            if grille[ligne][colonne] == "X":
                # Dessiner un X
                pygame.draw.line(fenetre, rouge,
                                 (colonne * taille_case + 20, ligne * taille_case + 20),
                                 ((colonne + 1) * taille_case - 20, (ligne + 1) * taille_case - 20), 5)
                pygame.draw.line(fenetre, rouge,
                                 (colonne * taille_case + 20, (ligne + 1) * taille_case - 20),
                                 ((colonne + 1) * taille_case - 20, ligne * taille_case + 20), 5)
            elif grille[ligne][colonne] == "O":
                # Dessiner un O
                pygame.draw.circle(fenetre, bleu,
                                   (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2),
                                   taille_case // 2 - 20, 5)


def verifier_victoire(joueur):
    """Vérifie si le joueur donné a gagné."""
    # Vérifier les lignes
    for ligne in grille:
        if ligne.count(joueur) == 3:
            return True

    # Vérifier les colonnes
    for col in range(3):
        if grille[0][col] == joueur and grille[1][col] == joueur and grille[2][col] == joueur:
            return True

    # Vérifier les diagonales
    if grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur:
        return True
    if grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur:
        return True

    return False


def afficher_message(message):
    """Affiche un message au centre de l'écran."""
    texte = police.render(message, True, noir)
    fenetre.fill(blanc)
    fenetre.blit(texte, (largeur // 2 - texte.get_width() // 2, hauteur // 2 - texte.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(3000)


def ia_jouer():
    """L'IA joue en choisissant la première case vide disponible."""
    for ligne in range(3):
        for colonne in range(3):
            if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = "O"
                return


def jeu_xo():
    global joueur_actuel
    jeu_en_cours = True

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and joueur_actuel == "X":
                # Obtenir la position de la souris
                x, y = event.pos
                ligne = y // taille_case
                colonne = x // taille_case

                # Vérifier si la case est vide
                if grille[ligne][colonne] == " ":
                    grille[ligne][colonne] = joueur_actuel

                    # Vérifier si le joueur actuel a gagné
                    if verifier_victoire(joueur_actuel):
                        afficher_message(f"Le joueur {joueur_actuel} a gagné!")
                        jeu_en_cours = False
                        break

                    # Vérifier si la grille est pleine
                    if all(cell != " " for row in grille for cell in row):
                        afficher_message("Match nul!")
                        jeu_en_cours = False
                        break

                    # Changer de joueur
                    joueur_actuel = "O"

        # Si c'est au tour de l'IA de jouer
        if joueur_actuel == "O" and jeu_en_cours and mode_ia:
            ia_jouer()

            # Vérifier si l'IA a gagné
            if verifier_victoire("O"):
                afficher_message("L'IA a gagné!")
                jeu_en_cours = False
                break

            # Vérifier si la grille est pleine
            if all(cell != " " for row in grille for cell in row):
                afficher_message("Match nul!")
                jeu_en_cours = False
                break

            # Changer de joueur
            joueur_actuel = "X"

        # Dessiner la grille et les symboles
        dessiner_grille()
        dessiner_symboles()
        pygame.display.update()

    # Réinitialiser le jeu
    pygame.time.wait(2000)
    pygame.quit()


# Lancer le jeu
jeu_xo()