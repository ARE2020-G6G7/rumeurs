# Fichier Python sur les rumeurs
import pyplot as plt
# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'utilisateurs avec des relation qui reste à définir.
# Pour créer ce monde, on choisit d'utiliser une fonction reseau_social() qui prend en paramètre un entier taille et qui renvoit une liste composé d'entiers représentant les utilisateurs caractérisés par un numéro allant de 0 à taille-1.
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
            Lbis.append(0)
        L.append(Lbis)
    return L

#Visulisation du réseau social 
def plot_world(world):
    A = world
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='tab10')
    plt.tick_params(top=True, bottom=True, right=True, left=True, labelleft=False, labelbottom=False)
    plt.show()

#Applicaiton d'une des formules, les valeurs de S et I varient avec le temps, Sigma, B et Micro sont stables
def nbre_individu_S_0(B,Sigma,I,Micro,S):
    return B-Sigma*S*I-Micro*S
