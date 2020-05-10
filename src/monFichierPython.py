# Fichier Python sur les rumeurs
import pyplot as plt
# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'individus réceptives à la rumeurs, dites S.
# Pour créer ce monde, on choisit d'utiliser une fonction reseau_social() qui prend en paramètre un entier taille et qui renvoit une liste de liste de 0 afin de créer un monde spatial par la suite(à voir)
# Le chiffre 0 correspond à une personne N, tous les individus sont de type N au tout début

def reseau_social(taille):
    """int->list[list[int]]
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

# Première version de la fonction partage()
def partage(Tuple, Teta1, Teta2, Gamma, Phi, B, Micro, c, d):
    """tuple[list[list[int]]*int^5]*float^4*int*float*int^2->tuple[list[list[int]]*int^5]
    retourne le réseau social prenant compte du partage d'une rumeur."""
    # RS: list[list[int]], S: int, A: int, I: int, R: int, h: int
    RS, S, A, I, R, h = Tuple
    
    # S1: int
    S1 = nbre_individu_S_1(B,Phi,I,Micro,S)
    # i: int
    i = 0
    # j: int
    j = 0
    while (i<S1 and j<B):
        if (RS[j]==0):
            RS[j]=1
            i = i + 1
        j = j + 1
    
    # A1: int
    A1 = nbre_individu_A_2(Teta1,gamma,phi,micro,h,S,I,A)
    i = 0
    j = 0
    while (i<A1 and j<B):
        if (RS[j]==1):
            RS[j]=2
            i = i + 1
        j = j + 1
    
    # I1: int
    I1 = nbre_individu_I_3(Teta2,gamma,phi,micro,h,S,I)
    i = 0
    j = 0
    while (i<I1 and j<B):
        if (RS[j]==1):
            RS[j]=3
            i = i + 1
        j = j + 1
    
    # R1: int
    R1 = nbre_individu_R_4(Teta1,Teta2,gamma,phi,micro,S,A,I,R)
    i = 0
    j = 0
    while (i<1 and j<B):
        if (RS[j]==1):
            RS[j]=4
            i = i + 1
        j = j + 1
    
    # h1: int
    h1 = fonction_h(c,d,I)
    
    return (RS, S, A, I, R, h)

#Visulisation du réseau social
def plot_world(world):
    """list[list[int]]->Image
    retourne le monde."""
    A = world
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='tab10')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()

#Application des formules et définitions des termes, les valeurs de S,A ,I et R varient avec le temps; Teta1, Teta2, Gamma, Phi, B et Micro sont stables tout le long de la simulation
    #S = individu Susceptible, confronté à la rumeur, représenté par 1 dans le réseau social
def nbre_individu_S_1(B,Phi,I,Micro,S): #(B,Sigma,I,Micro,S):
    """int*float*int*float*int->int
    retourne le nombre d'individus S susceptible à la rumeur."""
    return int(B-Phi*S*I-Micro*S) #B-Sigma*S*I-Micro*S

    #A = Individu croyant/ne partageant pas la rumeur, représenté par 2 dans le réseau social
def nbre_individu_A_2(Teta1,gamma,phi,micro,h,S,I,A): #(Teta1,gamma,phi,micro,h,S,A):
    """float^4*int^4->int
    retourne le nombre d'individus A croyant mais ne partageant pas la rumeur."""
    return int(Teta1*phi*S*I - gamma*A + h - micro*A)

    #I = Individu croyant/partageant la rumeur, représenté par un 3 dans le réseau social
def nbre_individu_I_3(Teta2,gamma,phi,micro,h,S,I):
    """float^4*int*3->int
    retourne le nombre d'individus I croyant et partageant la rumeur."""
    return int(Teta2*phi*S*I - gamma*I - h + micro*I)

    #R = Individu non-Croyant/ne partageant pas la rumeur, représenté par 4 dans le réseau social
def nbre_individu_R_4(Teta1,Teta2,gamma,phi,micro,S,A,I,R):
    """float^5*int^4->int
    retourne le nombre d'individus R ne croyant pas et ne partageant pas la rumeur."""
    return int((1-Teta1-Teta2)*phi*S*I+gamma*(A+I)-micro*R)

    #Fonction h qui determine le nombre d'individus devant garder le silence
def fonction_h(c,d,I):
    """int^3->int
    retourne le nombre d'individus devant garder le silence."""
    return int(c*I/(d+I))

plot_world(reseau_social(9))
