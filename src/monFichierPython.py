# Fichier Python sur les rumeurs

# Pour modéliser la propagation de rumeurs sur un réseau social, on considère un monde composé d'utilisateurs avec des relation qui reste à définir.
# Pour créer ce monde, on choisit d'utiliser une fonction reseau_social() qui prend en paramètre un entier taille et qui renvoit une liste composé d'entiers représentant les utilisateurs caractérisés par un numéro allant de 0 à taille-1.
def reseau_social(taille):
    """int->list[int]
    retourne une liste représentant un réseau social et ses internautes."""
    # L: list[int]
    L=[]
    # i: int
    for i in range(0,taille):
        L.append(i)
    return L

