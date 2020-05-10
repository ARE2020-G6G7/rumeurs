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
    """Tuple[list[int],int,int,int,int,int]*float*float*float*float*int*float*int*int->tuple[list[list[int]],int,int,int,int,int]
    retourne un tuple composé du réseau social prenant compte du partage d'une rumeur et des nombres d'individus dans chaque groupe pour la durée d'un tour."""
    # RS: list[list[int]], S: int, A: int, I: int, R: int, h: int
    RS, S, A, I, R, h = Tuple
    
    # S1: int
    S1 = nbre_individu_S_1(B,Phi,I,Micro,S)
    # i: int
    i = S1
    # RS_S: list[list[int]]
    RS_S = []
    # y: int
    for y in range(0,len(RS)):
        # L: list[int]
        L = RS[y]
        # x: int
        for x in range(0,len(L)):
            if (i!=0 and L[x]==0):
                L[x]=1
            i = i - 1
        RS_S.append(L)
            
    
    # A1: int
    A1 = nbre_individu_A_2(Teta1,Gamma,Phi,Micro,h,S,I,A)
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
    I1 = nbre_individu_I_3(Teta2,Gamma,Phi,Micro,h,S,I)
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
    R1 = nbre_individu_R_4(Teta1,Teta2,Gamma,Phi,Micro,S,A,I,R)
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
    h1 = fonction_h(c,d,I)

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
    """float^4*int^3->int
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
