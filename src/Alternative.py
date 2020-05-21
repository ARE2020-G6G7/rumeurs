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
    """ list[list[int]]*Number -> bool
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
    """ Number^2 -> int
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
    """ list[list[int]]*Number^5 -> list[list[int]]
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
    """int*list[list[int]]*Number^5 -> list[list[int]]
        nbre_tour>=1 and 0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
        retourne l'état du réseau après plusieurs tours de simulations """
    #twitter : list[list[int]]
    twitter = copy.copy(reseau)
    #i : int
    for i in range(0,nbre_tour):
        twitter = partage(twitter, phi, micro, gamma, Teta1, Teta2)
    return twitter

def Viralite(reseau):
    """ list[list[int]]-> Number
        retourne un indice pour déterminer la viralité de la rumeur dans le réseau social """
    # nbre_de_S: int
    nbre_de_S = 0
    # tot: int
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
    """list[list[int]]->int
    retourne la taille des personnes touchés par la rumeur
    """
    # nbre_de_S: int
    nbre_de_S = 0
    # tot: int
    tot = 0
    #L : list[int]
    for L in reseau:
        #i : int
        for i in range(0, len(L)):
            tot = tot + 1
            if(L[i]==1):
                nbre_de_S = nbre_de_S + 1
    return tot - nbre_de_S

#La Profondeur est proportionnel au temps passé dans l'expérience
#La Largeur est difficillement représentable dans cette simulation

def Taille_de_A(reseau):
    """list[list[int]]->int
    retourne la taille des personnes A croyant mais ne partageant pas la rumeur."""
    # nbre_de_A: int
    nbre_de_A = 0
    # L: list[int]
    for L in reseau:
        # i: int
        for i in range(0, len(L)):
            if(L[i]==2):
                nbre_de_A = nbre_de_A + 1
    return nbre_de_A

def Taille_de_I(reseau):
    """list[list[int]]->int
    retourne la taille des personnes I croyant et partageant la rumeur."""
    # nbre_de_I: int
    nbre_de_I = 0
    # L: list[int]
    for L in reseau:
        # i: int
        for i in range(0, len(L)):
            if(L[i]==3):
                nbre_de_I = nbre_de_I + 1
    return nbre_de_I

def Taille_de_R(reseau):
    """list[list[int]]->int
    retourne la taille des personnes R ne croyant pas et ne partageant pas la rumeur."""
    # nbre_de_R: int
    nbre_de_R = 0
    # L: list[int]
    for L in reseau:
        # i: int
        for i in range(0, len(L)):
            if(L[i]==4):
                nbre_de_R = nbre_de_R + 1
    return nbre_de_R

def graphe(nbre_tour, reseau, phi,micro,gamma,Teta1,Teta2):
    """int*list[list[int]]*Number^5->NoneType
    H: nbre_tour>=1 and 0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
    affiche les graphes de l'évolution des différentes catégories d'individus et de la viralite en fonction du nombre de tour."""
    #twitter : list[list[int]]
    twitter = copy.copy(reseau)
    # T: list[int]
    T = []
    T.append(Taille(twitter))
    # S: list[int]
    S = []
    S.append(Taille_de_S(twitter))
    # A: list[int]
    A = []
    A.append(Taille_de_A(twitter))
    # I: list[int]
    I = []
    I.append(Taille_de_I(twitter))
    # R: list[int]
    R = []
    R.append(Taille_de_R(twitter))
    # L: list[int]
    L =[]
    # V: list[int]
    V = []
    V.append(Viralite(twitter))
    L.append(0)
    
    #i : int
    for i in range(0,nbre_tour):
        twitter = partage(twitter, phi, micro, gamma, Teta1, Teta2)
        T.append(Taille(twitter))
        S.append(Taille_de_S(twitter))
        A.append(Taille_de_A(twitter))
        I.append(Taille_de_I(twitter))
        R.append(Taille_de_R(twitter))
        L.append(i + 1)
        V.append(Viralite(twitter))

    plt.plot(L, T, label="Individus touchés par la rumeur (A + I + R)")
    plt.plot(L, S, label="Individus S susceptible à la rumeur")
    plt.plot(L, A, label="Individus A croyant mais ne partageant pas la rumeur")
    plt.plot(L, I, label="Individus I croyant et partageant la rumeur")
    plt.plot(L, R, label="Individus R ne croyant pas et ne partageant pas la rumeur")
    plt.title('Evolution des différentes catégories en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(L, V)
    plt.title('Evolution de la viralite en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Viralite')
    plt.grid()
    plt.show()
    
    return None

def compare_reseau(nbre_tour, reseau1, reseau2, phi_1,micro_1,gamma_1,Teta1_1,Teta2_1, phi_2,micro_2,gamma_2,Teta1_2,Teta2_2):
    """list[list[int]]^2*Number^10->NoneType
    H: nbre_tour>=1 and 0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
    affiche des graphes.
    """
    #twitter1 : list[list[int]]
    twitter1 = copy.copy(reseau1)
    # T1: list[int]
    T1 = []
    T1.append(Taille(twitter1))
    # S1: list[int]
    S1 = []
    S1.append(Taille_de_S(twitter1))
    # A1: list[int]
    A1 = []
    A1.append(Taille_de_A(twitter1))
    # I1: list[int]
    I1 = []
    I1.append(Taille_de_I(twitter1))
    # R1: list[int]
    R1 = []
    R1.append(Taille_de_R(twitter1))
    # L: list[int]
    L = []
    L.append(0)
    # V1: list[int]
    V1 = []
    V1.append(Viralite(twitter1))
    
    #i : int
    for i in range(0,nbre_tour):
        twitter1 = partage(twitter1, phi_1, micro_1, gamma_1, Teta1_1, Teta2_1)
        T1.append(Taille(twitter1))
        S1.append(Taille_de_S(twitter1))
        A1.append(Taille_de_A(twitter1))
        I1.append(Taille_de_I(twitter1))
        R1.append(Taille_de_R(twitter1))
        L.append(i + 1)
        V1.append(Viralite(twitter1))
    
    #twitter2 : list[list[int]]
    twitter2 = copy.copy(reseau2)
    # T2: list[int]
    T2 = []
    T2.append(Taille(twitter2))
    # S2: list[int]
    S2 = []
    S2.append(Taille_de_S(twitter2))
    # A2: list[int]
    A2 = []
    A2.append(Taille_de_A(twitter2))
    # I2: list[int]
    I2 = []
    I2.append(Taille_de_I(twitter2))
    # R2: list[int]
    R2 = []
    R2.append(Taille_de_R(twitter2))

    # V2: list[int]
    V2 = []
    V2.append(Viralite(twitter2))
    
    #i : int
    for i in range(0,nbre_tour):
        twitter2 = partage(twitter2, phi_2, micro_2, gamma_2, Teta1_2, Teta2_2)
        T2.append(Taille(twitter2))
        S2.append(Taille_de_S(twitter2))
        A2.append(Taille_de_A(twitter2))
        I2.append(Taille_de_I(twitter2))
        R2.append(Taille_de_R(twitter2))

        V2.append(Viralite(twitter2))

    plt.plot(L, T1, label="Individus touchés par la rumeur (reseau1)")
    plt.plot(L, T2, label="Individus touchés par la rumeur (reseau2)")
    plt.title('Evolution des personnes touchées par la rumeur en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()

    plt.plot(L, S1, label="Individus S susceptible à la rumeur (reseau1)")
    plt.plot(L, S2, label="Individus S susceptible à la rumeur (reseau2)")
    plt.title('Evolution des personnes S susceptible à la rumeur en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()

    plt.plot(L, A1, label="Individus A croyant mais ne partageant pas la rumeur (reseau1)")
    plt.plot(L, A2, label="Individus A croyant mais ne partageant pas la rumeur (reseau2)")
    plt.title('Evolution personnes A croyant mais ne partageant pas la rumeur en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()

    plt.plot(L, I1, label="Individus I croyant et partageant la rumeur (reseau1)")
    plt.plot(L, I2, label="Individus I croyant et partageant la rumeur (reseau2)")
    plt.title('Evolution personnes I croyant et partageant la rumeur en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(L, R1, label="Individus R ne croyant pas et ne partageant pas la rumeur (reseau1)")
    plt.plot(L, R2, label="Individus R ne croyant pas et ne partageant pas la rumeur (reseau2)")
    plt.title('Evolution personnes R ne croyant pas et ne partageant pas la rumeur en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Nombre de personnes')
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(L, V1)
    plt.plot(L, V2)
    plt.title('Evolution de la viralite en fonction du nombre de tour')
    plt.xlabel('Nombre de tour')
    plt.ylabel('Viralite')
    plt.grid()
    plt.show()
    
    return None

test = partage_tour(50,reseau_social, Phi, Micro, Gamma, Teta1, Teta2)
plot_world(test)

graphe(10,reseau_social,0.2,0.2,0.005,0.2,0.7)
compare_reseau(10, reseau_social, reseau_social, 0.2,0.2,0.005,0.2,0.7, 0.5,0.8,0.005,0.7,0.1)