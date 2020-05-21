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

Afin de modéliser la propagation d'une rumeur, nous nous sommes inspirés du modèle SAIR, un modèle compartimental en épidemiologie, que l'étude chinoise a avancé sur son papier.
On considère un monde composé d'individus réceptives à la rumeurs, dites S. Le réseau social se catégorise en 4 individus :
S = individu Susceptible, confronté à la rumeur, représenté par 1 dans le réseau social
A = Individu croyant/ne partangeant pas la rumeur, représenté par 2 dans le réseau social
I = Individu croyant/partageant la rumeur, représenté par un 3 dans le réseau social
R = Individu non-Croyant/ne partageant pas la rumeur, représenté par 4 dans le réseau social
Quand t=0, S et I > 0, A = R = 0

L'étude décrivait diverses paramètres et variables de la simulation servant à recréer une situation et différentes types d'information.
- La probabilité d'être confronté à une rumeur (B)
- Le taux de transmission de la rumeur (φ)
- La probabilite de changer de rôle (μ)
- Le taux de chance d'une transition I/A vers R (γ)
- Le taux de chance d'une transition S vers A (θ1)
- Le taux de chance d'une transition S vers I (θ2)
- Le taux de chance d'une transition S vers R (1-θ1-θ2)
- Le seuil de cohérence de la rumeur (h) qui est un booléen
Mise à part h, tous les paramètres sont des flottants compris dans l'intervalle entre 0 et 1 non inclus

A la base, nous voulions respecter jusqu'au bout le modèle de l'étude qui présentait notamment diverses équations différentielles, des formules, théroèmes,etc...
Mais notre niveau de et de connaissances et de compréhension n'étant pas assez haut pour saisir l'étude et ses enjeux, et par soucis de simplification du modèle (afin de coder par la suite), nous avons pris une autre direction et chercher un modèle plus clair et visuel pour nous.

Nous partons d'un monde de la forme d'une matrice 6x6 (pour 36 personnes), constitué uniquement d'individus S, sauf un qui sera de type I et qui déclenchera la propagation.
Le programme parcourt la matrice Ligne par Ligne puis Colonne par Colonne et identifie le type de l'individu pointé.

Si il est de type S, il y a une probabilité φ de recevoir l'information. φ va déterminer la rapidité de la simulation, plus φ est proche de 1 plus l'info sera partagé et atteindra plus facilement les individus S du réseau
Si il y a réception de l'information et que l'individu analysé et de type S , il y a une probabilité μ de changer de rôle, cela dépend de la viralité et de la popularité  de l'information, si elle suscite beaucoup d'intérêt dans la réseau social ou pas, ce qui va déterminer si elle crée beaucoup d'engagements au sein du réseau. Si le changement n'a pas lieu, intervient aussi la fonction h, qui sert de seuil de cohérence/confirmation de la rumeur, peut transformer l'individu si elle retourne le booléen True.
Enfin, selon les probas θ1 et θ2, l'individu S est transformé soit en A, en I ou en R.

Si l'individu est de type A ou I, il y'a une probabilité gamma que l'individu se remette en question et change complétement de rôle pour devenir de R ce qui a pour action de ralentir la propagation. C'est un paramètre très puissant qui peut vite chambouler une simulation, c'est pourquoi sa valeur sera maintenu en dessous de 0.1 dans les tests futurs.

La fonction partage retourne l'état du réseau après un tour de partage, une simple fonction partage_tour permet de visualiser l'évolution du réseau après plusieurs tours de simulations et de visualiser la tendance et la réaction des individus à un type d'information précis, sur court ou long terme.

Tout d'abord nous avons commencé notre simulation sur un groupe de 36 personnes avec comme crédibilite d'information:

-Très plausible avec φ=0.2, μ=0.2, γ=0.005, θ1=0.2, θ2=0.7, la simulation nous a donné S=3, R=8, I=15, A=10.
Avec une information qui parait tres plausible nous pouvons voir que le nombre de personnes qui y croit est de 25, parmis ces 25 personnes là seulement 15 personnes y croit et la repartage et enfin 8 personnes n'y croient pas et ne la partage pas.

-Peu plausible avec φ=1, μ=0.5, γ=0.005, θ1=0.1, θ2=0.8, la simulation nous a donné S=3, R=5, I=28, A=0.
Avec une information qui parait peu reele voire impossible, nous pouvons voir que le nombre de personnes qui y croit est de 28 et parmis eux 28 la repartage, seulement 5 personnes n'y croit pas...

-Information Confirmée avec φ=0.5, μ=0.8, γ=0.005, θ1=0.7, θ2=0.1, la simulation nous a donné S=5, R=8, I=3, A=20.
Avec une information confirmée 23 personnes y croit mais parmis ces 23 personnes là seulement 3 la repartage, 8 personnes n'y croit toujour pas.

Grâce à la simulation de 3 situations différentes, nous avons pu observer que les informations vraies et confirmées auront tendance à être crues, mais ne seront partagées que par quelques personnes. Au contraire une information peu plausible et qui parait peu imaginable est beaucoup crues et surtout enormement repartagé par les personnes qui y croit, une information tres plausible mais pas verifiéee est quant à elle beaucoup cru aussi mais seulement un peu plus de la moitie la repartage.

Les gens ont tendance à croire les informations sur Internet, mais plus l'authenticité et la confirmation des informations sont fortes, moins elle ne sera repartage. C'est ainsi que les fake news se propagent de plus en plus vite et affectent de nombreuses personnes.
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
