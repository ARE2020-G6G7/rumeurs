# Fichier Python sur les rumeurs
import pyplot as plt
# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'individus réceptives à la rumeurs, dites S.
# Pour créer ce monde, on choisit d'utiliser une fonction reseau_social() qui prend en paramètre un entier taille et qui renvoit une liste de liste de 0 afin de créer un monde spatial par la suite(à voir)
# Le chiffre 1 correspond à une personne S, tous les individus sont de type S au tout début

#Quand t=0, S = B, A = I = R = 0
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
            if(i==0 and j==0):
                Lbis.append(3)
            else:
                Lbis.append(1)
        L.append(Lbis)
    return L


def comptage(world,categorie_individus):
    """list[list[int]]*int->int
    retourne le nombre d'individus appartenant à une catégorie."""
    if(categorie_individus==-1):
        #res: int
        res = 0
        #i: list[int]
        for i in world:
            #j:int
            for j in i:
                res = res + 1
        return res
    else:
        #res: int
        res = 0
        #i: list[int]
        for i in world:
            #j:int
            for j in i:
                if j==categorie_individus:
                    res = res + 1
        return res

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
def nbre_individu_S_1(B,S,I,Micro,Phi):
    """Number^5->Number
    retourne le nombre d'individus S susceptible à la rumeur."""
    return B-Phi*S*I-Micro*S

    #A = Individu croyant/ne partangeant pas la rumeur, représenté par 2 dans le réseau social
def nbre_individu_A_2(Teta1,gamma,phi,micro,h,S,A,I):
    """Number^8->Number
    retourne le nombre d'individus A croyant mais ne partageant pas la rumeur."""
    return Teta1*phi*S*I - gamma*A + h - micro*A
    #I = Individu croyant/partageant la rumeur, représenté par un 3 dans le réseau social
def nbre_individu_I_3(Teta2,gamma,phi,micro,h,S,I):
    """Number^7->Number
    retourne le nombre d'individus I croyant et partageant la rumeur."""
    return Teta2*phi*S*I - gamma*I - h + micro*I
    #R = Individu non-Croyant/ne partageant pas la rumeur, représenté par 4 dans le réseau social
def nbre_individu_R_4(Teta1,Teta2,gamma,phi,micro,S,A,I,R):
    """Number^9->Number
    retourne le nombre d'individus R ne croyant pas et ne partageant pas la rumeur."""
    return (1-Teta1-Teta2)*phi*S*I+gamma*(A+I)-micro*R
    #Fonction qui determine le nombre d'individus devant garder le silence
def fonction_h(c,d,I):
    """Number^3->Number
    retourne le nombre d'individus devant garder le silence."""
    return c*I/(d+I)
#On considère une rumeur politique, très relayée dans les réseaux sociaux selon nos recherches et expériences personnelles

Phi = 0.4
Micro = 0.5
Gamma = 0.3
Teta1 = 0.2
Teta2 =0.7
d= 1

def actualisation_reseau(c):
    S = 35
    A = 0
    I = 1
    R = 0
    print("Début de la simulation")
    print("")
    for t in range(0,5):
        if(t==0):
            print("A t=0, S=35, A=0, I=1, R=0, ")
            print(" ")
        else:
            print("A t =" + str(t))
            S_mem = S+ nbre_individu_S_1(36,S,I,0.5,0.4)
            print("Nombre de S =" + str(S_mem))
            A_mem = A + nbre_individu_A_2(0.2,0.3,0.4,0.5,fonction_h(c,I,1),S,A,I)
            print("Nombre de A=" + str(A_mem))
            I_mem = I + nbre_individu_I_3(0.7,0.3,0.4,0.5,fonction_h(c,I,1),S,I)
            print("Nombre de I="+ str(I_mem))
            R_mem = R + nbre_individu_R_4(0.2,0.7,0.3,0.4,0.5,S,A,I,R)
            print("Nombre de R=" + str(R_mem))
            print("")
            S = S_mem
            A = A_mem
            I = I_mem
            R = R_mem
    print("Fin de simulation")

actualisation_reseau(141)

def partage(Tuple, Teta1, Teta2, Gamma, Phi, B, Micro, c, d):
    """tuple[list[int],int,int,int,int,int]*Number*Number*Number*Number*int*Number*int*int->tuple[list[list[int]],int,int,int,int,int]
    retourne un tuple composé du réseau social prenant compte du partage d'une rumeur et des nombres d'individus dans chaque groupe pour la durée d'un tour."""
    # RS: list[list[int]], S: int, A: int, I: int, R: int, h: int
    RS, S, A, I, R, h = Tuple
    
    # S1: int
    S1 = int(nbre_individu_S_1(B,S,I,Micro,Phi))
    # i: int
    i = 0
    # RS_S: list[list[int]]
    RS_S = []
    # y: int
    for y in range(0,len(RS)):
        # L: list[int]
        L = RS[y]
        # x: int
        for x in range(0,len(L)):
            if (i<S1 and L[x]==0):
                L[x]=1
                i = i + 1
        RS_S.append(L)
            
    
    # A1: int
    A1 = int(nbre_individu_A_2(Teta1,Gamma,Phi,Micro,h,S,A,I))
    i = 0
    # RS_A: list[list[int]]
    RS_A = []
    for y in range(0,len(RS_S)):
        # L: list[int]
        L = RS_S[y]
        # x: int
        for x in range(0,len(L)):
            if (i<A1 and L[x]==1):
                L[x]=2
                i = i + 1
        RS_A.append(L)
    
    # I1: int
    I1 = int(nbre_individu_I_3(Teta2,Gamma,Phi,Micro,h,S,I))
    i = 0
    # RS_I: list[list[int]]
    RS_I = []
    for y in range(0,len(RS_A)):
        # L: list[int]
        L = RS_A[y]
        # x: int
        for x in range(0,len(L)):
            if (i<I1 and L[x]==1):
                L[x]=3
                i = i + 1
        RS_I.append(L)
    
    # R1: int
    R1 = int(nbre_individu_R_4(Teta1,Teta2,Gamma,Phi,Micro,S,A,I,R))
    # i: int
    i = 0
    # RS_R: list[list[int]]
    RS_R = []
    for y in range(0,len(RS_I)):
        # L: list[int]
        L = RS_I[y]
        # x: int
        for x in range(0,len(L)):
            if (i<R1 and L[x]==1):
                L[x]=4
                i = i + 1
        RS_R.append(L)
    
    # h1: int
    h1 = int(fonction_h(c,d,I))

    # L: list[list[int]]
    L=[]
    # b: int
    for b in range(0,len(RS_R)):
        #Lbis : list[int]
        Lbis = []
        #Lter : list[int]
        Lter = RS_R[b]
        #a : int
        for a in range(0,len(RS_R)):
            Lbis.append(Lter[a])
        L.append(Lbis)
    
    return (L, S1, A1, I1, R1, h1)

partage((reseau_social(10),35,0,1,0,fonction_h(1,0,1)), 0.2, 0.7, 0.3, 0.4, 100, 0.5, 1, 1)

def partage_tour(Tuple, Teta1, Teta2, Gamma, Phi, B, Micro, c, d, tour):
    """tuple[list[int],int,int,int,int,int]*Number*Number*Number*Number*int*Number*int*int*int->tuple[list[list[int]],int,int,int,int,int]
    retourne un tuple composé du réseau social prenant compte du partage d'une rumeur et des nombres d'individus dans chaque groupe pour la durée d'un tour."""
    # T: tuple[list[int],int,int,int,int,int]
    T = Tuple
    # i: int
    for i in range(0,tour):
        T = partage(T, Teta1, Teta2, Gamma, Phi, B, Micro, c, d)
    return T

partage_tour((reseau_social(10),35,0,1,0,fonction_h(1,0,1)), 0.2, 0.7, 0.3, 0.4, 100, 0.5, 1, 1, 5)