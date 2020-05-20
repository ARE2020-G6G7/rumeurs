from random import *
from matplotlib import pyplot as plt
import numpy as np
import copy

# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'individus réceptives à la rumeurs, dites S.
# Le chiffre 1 correspond à une personne S, tous les individus sont de type S au tout début

#Quand t=0, S et I > 0, A = R = 0
reseau_social = [[3,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

#On considère une rumeur politique, très relayée dans les réseaux sociaux selon nos recherches et expériences personnelles

#Taux transmission rumeur
Phi = 0.2
#Proba de changer de rôle
Micro = 0.2
#Proba transition I/A->R(remise en question)
Gamma = 0.005
#Proba transition S->A
Teta1 = 0.2
#Proba transition S->I
Teta2 =0.7

#S = individu Susceptible, confronté à la rumeur, représenté par 1 dans le réseau social
#A = Individu croyant/ne partangeant pas la rumeur, représenté par 2 dans le réseau social
#I = Individu croyant/partageant la rumeur, représenté par un 3 dans le réseau social
#R = Individu non-Croyant/ne partageant pas la rumeur, représenté par 4 dans le réseau social

#Visulisation du réseau social
def plot_world(world):
    """list[list[int]]->Image
    retourne un modèle graphique du monde"""
    A = world
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='viridis')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()
#Individu S = Mauve
#Individu A = Bleu
#Individu I = Vert
#Individu R = Jaune

def fonction_h(reseau,biais):
    """ list[list[int]]*int -> bool
        0<biais<1
        retourne Vrai si le biais de confirmation est atteint sinon Faux """
    #tot : int
    tot = 0
    #nbre_I : int
    nbre_I = 0
    #L : list[int]
    for L in reseau:
        #i : int
        for i in L:
            if i==3:
                nbre_I += 1
            tot += 1
    if nbre_I/tot>=biais:
        return True
    else:
        return False
#FAIRE UNE FONCTION QUI MANIPULE L'ALEATOIRE ET QUI RETOURNE SOIT 2 3 OU 4 SELON LE CHIFFRE QUI TOMBE ET LES PROBAS TETA1 et TETA2
def choix(Teta1,Teta2):
    """ int**2 -> int
        1>Teta1>0 and 1>Teta2>0
        retourne 2,3 ou 4 en fonction des probas Teta1 et Teta2 , suite à un choix aléatoire  """
    #T1 : int
    T1 = Teta1
    #T2 : int
    T2 = Teta2 + T1
    Choix = random()
    if Choix<=T1:
        return 2
    if Choix>T1 and Choix<=T2:
        return 3
    else:
        return 4


def partage(reseau,phi,micro,gamma,Teta1,Teta2):
    """ list[list[int]]*float**6 -> list[list[int]]
        0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
        retourne le monde après une periode t de partage de la rumeur """
    #LR : list[list[int]]
    LR = []
    #Ligne : int
    for Ligne in range(0,6):
        LR.append([])
        #L1 : list[int]
        L1 = LR[Ligne]
        #L2 : list[int]
        L2 = reseau[Ligne]
        #Colonne : int
        for Colonne in range(0,6):
            L1.append(L2[Colonne])
            if L2[Colonne]==1:
                #L_phi : list[int]
                L_phi = random()
                if(L_phi<=phi):
                    #h : bool
                    h = fonction_h(reseau,0.5)
                    #L_micro : list[int]
                    L_micro = random()
                    if L_micro<=micro or h==True:
                        L1[Colonne]=choix(Teta1,Teta2)
            else:
                if (L2[Colonne]==2 or L2[Colonne]==3) and Ligne+Colonne!=0:
                    #L_gamma : list[int]
                    L_gamma = random()
                    if(L_gamma<=gamma):
                        L1[Colonne]=4
    return LR

def partage_tour(nbre_tour, reseau, phi,micro,gamma,Teta1,Teta2):
    """int*list[list[int]]*float**6 -> list[list[int]]
        nbre_tour>=1 and 0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
        retourne l'état du réseau après plusieurs tours de simulations """
    #twitter : list[list[int]]
    twitter = copy.copy(reseau)
    #i : int
    for i in range(0,nbre_tour):
        twitter = partage(twitter, phi, micro, gamma, Teta1, Teta2)
    return twitter

def Viralite(reseau):
    """ list[list[int]]-> int
        retourne un indice pour déterminer la viralité de la rumeur dans le réseau social """
    nbre_de_S = 0
    tot = 0
    #L: list[int]
    for L in reseau:
        #i : int
        for i in L:
            tot =+ 1
            if(L[i]==1):
                nbre_de_S =+ 1
    return (tot - nbre_de_S)/tot

def Taille(reseau):
    nbre_de_S = 0
    tot = 0
    #L : list[int]
    for L in reseau:
        #i : int
        for i in L:
            tot =+ 1
            if(L[i]==1):
                nbre_de_S =+ 1
    return tot - nbre_de_S

#La Profondeur est proportionnel au temps passé dans l'expérience
#La Largeur est difficillement représentable dans cette simulation


test = partage_tour(50,reseau_social, Phi, Micro, Gamma, Teta1, Teta2)
plot_world(test)
