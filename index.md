# Les rumeurs et leur propagation dans les réseaux sociaux

Les rumeurs sont largement diffusées par nos canaux d'information. Ce sont des infos et des rumeurs créées par (un groupe d')individus. Leur but est de déformer la réalité et de manipuler les croyances, les opinions, un lobby ou les domaines politiques du public attendu. Si elles sont largement diffusées, ces rumeurs peuvent atteindre le plus haut niveau de l'actualité et peuvent être utilisées pour écrire des articles officiels.

 Nos projets de recherche documentaire comprennent l'étude de la propagation de fake news et des facteurs qui facilitent leur diffusion à grande échelle, comparées aux informations véridiques et vérifiées. En particulier, il est nécessaire de simuler un réseau social comme Twitter et de voir comment les informations sont transférées d'une personne à une autre.


## Spreading of Fake-News sociaux
Fake news are widely spread through multiple network, they are created by a group of person who aims to manipulate people's opinions and the reality, to the benefit of a lobby, an ideology,etc... They could be used by official journalists so they can write serious article for well known newspaper.

Our project is to study the spreading of fake news, fin the factor that helps the spread of those news, and compare it to the spreading of real official information. In paticular, we will simulate a social network such as Twitter to see how the information spread in between the ursers.

## Présentation de l'équipe

|F.Zeid| F.Achille | B.Atmane  | K.Jean-Charles |


## Description synthétique du projet
> Notre recherche met en évidence trois thèmes et mots clés principaux: la propagation, l'influence et le debunkage, la lutte contre ces news. Grâce à certaines recherches sur Google, nous pouvons trouver des sources provenant de sites d'actualités bien connus, de travail de chercheurs basés sur des sources fiables et divers blogueurs qui partagent leurs connaissances sur le sujet. Évidemment, le discours de ce dernier porte un peu de méfiance et d'attention. Cela nous permet de révéler les mots clés les plus fréquemment renvoyés dans ces recherches. De plus, nous sommes très chanceux d'avoir rencontré de nombreuses infographies et statistiques sur ce sujet, qui aideront à modéliser la propagation des fake news.



**Problématique :**Pourquoi les fake news se propagent elles plus que les faits réels ?

**Hypothèse principale :**Les fake news touchent des domaines et centres d'intérets qui influencent et concernent le plus de monde.

**Hypothèses secondaires :**La déconstruction et le debunkage ne sont pas assez efficaces ou appliqués à toutes les fake news


**Objectifs :**Expliquer la domination de la rumeur sur la vérité et refléchir à des pistes d'endiguement des fake news. 

**Critère(s) d'évaluation :**Comparer la propagation de la vérité et de la rumeur, jusqu'à son debunkage.

## Présentation structurée des résultats

Présentation du choix de modélisation, des outils, du code et des résultats (tableaux, courbes, animations...) (**avec une analyse critique**).

En ligne, les individus peuvent être divisés en plusieurs catégories :
N(t) : Ensemble des individus
S(t) : Ensemble des individus confrontés aux rumeurs
A(t) : Ensemble des individus croyants à la rumeur mais ne la partageant pas
I(t) : Ensemble des individus croyants à la rumeur et la partageant
R(t) : Ensemble des individus ne croyants pas à la rumeur et qui ne la partagent pas

En ligne, la propagation d’une rumeur est très rapide. C’est pourquoi nous pouvant dire que son évolution est constante. N (t) Deviens donc B, qui est appelé « constante d’immigration ». B est également le nombre de personne susceptible de rencontrer une rumeur, car dans notre cas tout le monde l’est. Leur émigration en fonction du temps est représentée par μ, et le taux de transmissions entre individus susceptible est représenté par φ.
θ1   représente la proportion des individus susceptible aux individus indiffèrent.
θ2  représente la proportion des individus susceptible aux individus indiffèrent.
Y est la proportion des individus des individus indiffèrent et des individus qui propagent les rumeurs qui se remettent en question et qui jugent l’information.
Certains individus doivent garder le silence sur certaines informations, ce qui les forcent à croire l’information mais à ne pas la partager. Les individus qui propagent les rumeurs baisses donc par le facteur h(I) (par unité de temps).
Représente la fonction des gens qui sont forcer de garder le silence.


Ce graphique représente la propagation d’une rumeur en fonction du type d’individus et des formules vu auparavant.


Représentation de la propagation d’une rumeur :

Représente le nombre d’individus susceptibles à une rumeur par unité de temps.

Représente le nombre d’individus indifférents à une rumeur par unité de temps.

Représente le nombre d’individus qui propagent une rumeur par unité de temps.
  
Représente le nombre de personne qui remettent en question la rumeur.


 
Les conditions initiales sont donc :

 
Le nombre total d’individus est donc représenté par N(t) :

 

Les formules qui viennent avec :
	
 
 
 
 
The positive variant set of system (?) :

 

Comme A(t) et R(t) sont indépendants des équa diff de S(t) et I(t), nous pouvons donc changer ce systeme en :

 

Avec  


## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :
https://www-sciencedirect-com.accesdistant.sorbonne-universite.fr/science/article/pii/S0020025520302565?#sec0008

https://science.sciencemag.org/content/359/6380/1146

M. Alcaraz “Pourquoi les fake news se propagent bien plus vite“, les Echos, 11-mar-2018
“https://www.lesechos.fr/2018/03/pourquoi-les-fake-news-se-propagent-bien-plus-vite-986267”

 ”Les fake news en France – Faits et chiffres”, Statista, 9-sept- 2019  “https://fr.statista.com/themes/5481/les-fake-news-en-france/”

C.Asselin, «Fake News : 8 points importants à connaître pour les comprendre et les combattre https://blog.digimind.com/fr/tendances/fake-news-8-points_importants-comprendre-combattre
[Consulté le: 29/03/2020]

**Carte mentale de vos mots-clés, en utilisant** <a href="https://framindmap.org/mindmaps/index.html">Framindmap </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **Voir la bibliographie, les 2 papiers scientifiques ont été trouvé grâce au moteur de recherche de SUper Sorbonne, les autres grâce à Google **

