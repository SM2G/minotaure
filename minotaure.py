import os
import random
os.system('clear')

hauteur = 30
largeur = 100
mon_labyrinthe = []
ma_colonne = 0
ma_ligne = 0
symbole_mur = 'M'
symbole_sol = ' '

def poser_une_dalle(ma_colonne, ma_ligne):
    hasard = random.choice([symbole_sol, symbole_mur, symbole_sol])
    if ma_ligne == 0 or ma_colonne == largeur - 1 or ma_ligne == hauteur - 1:
        dalle = (ma_colonne, ma_ligne, symbole_mur)
    else:
        dalle = (ma_colonne, ma_ligne, hasard)
    return dalle

def afficher_une_ligne(ma_ligne):
    ligne_en_cours = symbole_mur
    for i in mon_labyrinthe:
        if i[1] == ma_ligne:
            ligne_en_cours = ligne_en_cours + str(i[2])
    print(ligne_en_cours)

def afficher_le_labytinthe():
    for i in range(hauteur):
        afficher_une_ligne(i)

for ma_ligne in range(hauteur):
    dalle = poser_une_dalle(ma_colonne, ma_ligne)
    mon_labyrinthe.append(dalle)
    for ma_colonne in range(largeur):
        dalle = poser_une_dalle(ma_colonne, ma_ligne)
        mon_labyrinthe.append(dalle)
        ma_colonne = ma_colonne + 1
    ma_ligne = ma_ligne + 1
    ma_ligne = 0

afficher_le_labytinthe()
