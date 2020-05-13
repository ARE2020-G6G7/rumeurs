import random
from matplotlib import pyplot as plt
import numpy as np
import copy

# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'individus réceptives à la rumeurs, dites S.
# Le chiffre 1 correspond à une personne S, tous les individus sont de type S au tout début

#Quand t=0, S et I > 0, A = R = 0
reseau_social = np.array([[3,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]])

#On considère une rumeur politique, très relayée dans les réseaux sociaux selon nos recherches et expériences personnelles

#Taux transmission rumeur
Phi = 0.4
#Proba de changer de rôle
Micro = 0.5
#Proba transition I/A->R(remise en question)
Gamma = 0.3
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
    retourne le monde."""
    A = world
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='tab10')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()

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
    #T1 : int
    T1 = Teta1* 10
    #T2 : int
    T2 = Teta2*10 + T1
    Choix = np.random.choice(10,1,0.1)
    if Choix[0]<T1:
        return 3
    if Choix[0]>=T1 and Choix[0]<T2:
        return 2
    else:
        return 4
def partage(reseau,phi,micro,gamma,Teta1,Teta2):
    """ list[list[int]]*float**6 -> list[list[int]]
        0<phi<1 and 0<micro<1 and 0<gamma<1 and 0<Teta1<1 and 0<Teta2<1
        retourne le monde après une periode t de partage de la rumeur """
    #i : int
    for i in range(0,6):
        #j : int
        for j in range(0,6):
            if reseau[i,j]==1:
                L_phi = np.random.choice(2,1,phi)
                if(L_phi[0]==1):
                    h = fonction_h(reseau,0.5)
                    L_micro = np.random.choice(2,1,micro)
                    if h==True and L_micro[0]==1:
                        reseau[i,j]== Choix(Teta1,Teta2)
            if (reseau[i,j]==2 or reseau[i,j]==3) and i+j!=0:
                L_gamma = np.random.choice(2,1,gamma)
                if(L_gamma[0]==1 ):
                    reseau[i,j]=4
    return reseau

def partage_tour(nbre_tour, reseau, phi,micro,gamma,Teta1,Teta2):
    #twitter : list[list[int]]
    twitter = copy.copy(reseau)
    #i : int
    for i in range(0,nbre_tour):
        twitter = partage(twitter, phi, micro, gamma, Teta1, Teta2)
    return twitter

plot_world(partage(reseau_social, Phi, Micro, Gamma, Teta1, Teta2))
