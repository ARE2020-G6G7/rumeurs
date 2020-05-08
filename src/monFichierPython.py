# Fichier Python sur les rumeurs
import pyplot as plt
# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'individus réceptives à la rumeurs, dites S.
# Pour créer ce monde, on choisit d'utiliser une fonction reseau_social() qui prend en paramètre un entier taille et qui renvoit une liste de liste de 0 afin de créer un monde spatial par la suite(à voir)
# Le chiffre 0 correspond à une personne N, tous les individus sont de type N au tout début

def reseau_social(taille):
    """int->list[int]
    retourne une liste représentant un réseau social et ses internautes."""
    # L: list[list[int]]
    L=[]
    # i: int
    for i in range(0,taille):
        #Lbis : list[int]
        Lbis = []
        #j : int
        for j in range(0,taille):
            Lbis.append(1)
        L.append(Lbis)
    return L

def partage()
#Visulisation du réseau social
def plot_world(world):
    A = world
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='tab10')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()

#Application des formules et définitions des termes, les valeurs de S,A ,I et R varient avec le temps; Teta1, Teta2, Gamma, Phi, B et Micro sont stables tout le long de la simulation
    #S = individu Susceptible, confronté à la rumeur, représenté par 1 dans le réseau social
def nbre_individu_S_1(B,Sigma,I,Micro,S):
    return B-Sigma*S*I-Micro*S

    #A = Individu croyant/ne partangeant pas la rumeur, représenté par 2 dans le réseau social
def nbre_individu_A_2(Teta1,gamma,phi,micro,h,S,A):
    return Teta1*phi*S*I - gamma*A + h - micro*A
    #I = Individu croyant/partageant la rumeur, représenté par un 3 dans le réseau social
def nbre_individu_I_3(Teta2,gamma,phi,micro,h,S,I):
    return Teta2*phi*S*I - gamma*I - h + micro*I
    #R = Individu non-Croyant/ne partageant pas la rumeur, représenté par 4 dans le réseau social
def nbre_individu_R_4(Teta1,Teta2,gamma,phi,micro,S,A,I,R):
    return (1-Teta1-Teta2)*phi*S*I+gamma*(A+I)-micro*R
    #Fonction qui determine le nombre d'individus devant garder le silence
def fonction_h(c,d,I):
    return c*I/(d+I)

plot_world(reseau_social(9))
