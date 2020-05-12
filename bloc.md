## Travail effectué 

=> Description hebdomadaire du travail effectué (variez les auteurs !)

### Semaine 1(6 - 12/04)
Pour répondre au feedback laissé suite à la remise de la présentation du projet, certains éléments de réponse se trouvent dans le """carnet de bord""" que j'ai envoyé le 31 mars à M.Prost. 
- A travers la question de "comment limiter au maximum", nous nous sommes fixé pour objectif de trouver la méthode de communication qui peut propager le plus d'intox afin de déterminer la méthode de communication qui restreint l'utilisation de ce phénomène dans ce canal d'information. Nous avons rapidement réalisé qu'Internet est la source de la plupart des affaires traitant de fake news.

- Nous avions initialement prévu de comparer plusieurs méthodes de communication, telles que la télévision, la radio, Internet et le bouche à oreille. Cependant, nous pensons qu'il vaut mieux garder Internet et les réseaux sociaux. En effet, le développement de ce phénomène se fait principalement à travers les réseaux sociaux qui favorise la diffusion généralisée de ces rumeurs.

- Nous comptions nous fier sur les études et données envoyées dans le "carnet de bord", qui contient différentes infographies et statisques permettant de dresser et définir certains coefficient et chiffres intéressants pour notre étude. Elle se focalisera du coup sur un seul réseau social dans le quel on considère un groupe d'individus se partageant des tweets, des informations,etc...  
Afin de déterminer le coefficient de propagation, nous nous intéressons à trois paramètres: la rationalité des fake news, la situation actuelle et la crédulité du public concerné. Certains d'entre eux sont extraits d'articles scientifiques publiés par des chercheurs du MIT:
 https://science.sciencemag.org/content/359/6380/1146. 
Ce sont des paramètres que  l'on fixe au début de la simultation et qui tendent à évoluer au fur à mesure du phénomène.

- En effet, les objectifs et la démarche ne cohèrent pas avec les objectifs de l'UE. Nos recherches doivent mener à la determination de coefficient de propagation en fonction de différents facteurs afin de dresser ces simulations. 

### Semaine 2
Le papier scientifique publié par les chercheurs du MIT (B) se revèle être très enrichissant et interessant pour notre projet, notamment quant à la quantification des caractéristiques d'une rumeur. On se place ici dans le réseau social Twitter pour le contexte.

En particulier, l'étude a classé et catégorisé les centres d'intérêt qui ont généré le plus d'interaction et de communication avec des Fake News. La politique et les légendes urbaines sont les thèmes impliqués dans ces rumeurs et se propagent à plus de gens en moins de temps. En effet, démystifier ces nouvelles n'est pas si facile, car elle doit être prudente face à de multiples sources, notamment pour la politique (si elle existe).

Aussi, le papier décrit le terme de "Rumor Cascades" qui correspond au parcours de la rumeur, de sa création/publication jusqu'au momne toù elle n'est pas plus propagée, en passant par un long processus de (re)partage entre utilisateurs. 

Ce phénomène se caractérise par 4 paramètres : Depth/Profondeur (La taille de l'enchainement des retweets/partages, appelé "node" dans le papier,  par des individus uniques), Size/Taille (le nombre total de personnes qui auront recu au moins une fois la nouvelle sur leur fil d'actualité), Breadth/Largeur (le nombre de node de la meme profondeur) et la viralité.

### Semaine 3
https://www-sciencedirect-com.accesdistant.sorbonne-universite.fr/science/article/pii/S0020025520302565?#sec0008
Un autre papier scientifique a attiré notre attention. Il présente un modèl de réseau social et de propagation de fake news basés autour de différentes équations et utilise notamment des notions plus complexes comme la théorie des bifurcations, la bifurcation  de Hopf...
Ce qui est intéressant ici, c'est le réseau social et les personnes qui l'utilisent.
L'étude catégorise les personnes recepetives aux rumeurs (S) sous 3 statuts : 
- Les personnes inintéressées par la rumeur, qui n'y croient pas et ne la (re)partagent pas (R)
- Les personnes concernées par la rumeur, ils croient en la rumeur et repartagent celle-ci (I)
- Les personnes croyants en la rumeur mais qui ne la partage pas (A)

Ces statuts sont amenés à changer au fur et à mesure de la simulation
Ce sont des vecteurs de l'informations. 
Notre réseau social sera constitué de N personnes et l'ensembles des individus I,S,R et A constitutent ce réseau. Au début de la simulation leur nombre est supérieur ou égal à 0.  

Aussi, nous avons trouver des formules intéressantes à mettre en place pour nos simulations, qui font appel à différentes equations différentielles et à des taux de chance de propagation.
Nous avons décider de les fixer arbitrairement suivant différents critères. Déjà, le type de rumeur, si elle est d'ordre politique, d'une legende urbaine etc... afin de déterminer si elle sera très partagées ou non. La véracité de la rumeur, si elle est facilement réfutable ou pas, si elle contient assez de sources et d'arguments solides.


### Semaine 5

L'étude précédente proposait une simulation qui définissait les différents rôles cités ci-dessus (I, S, R, A et N), mais définissait également différents facteurs qui représentent les constantes de simulation. Les facteurs de propagation des rumeurs dans ce modèle sont:

- La probabilité d'être confronté à une rumeur (B)
- Le taux de transmission de la rumeur (φ)
- La probabilite de changer de rôle (μ)
- Le taux de chance d'une transition (γ)
- La proportion d'individus sensibles par rapport aux individus indifférents (θ1)
- La proportion d'individus sensibles par rapport aux individus qui se propagent (θ2)
- La mesure d'efficacité (d)
- Le nombre maximum d'internautes gardant le silence (c)
- Le nombre de transition "debunkeur" (h)

Basé sur le fait du mécanisme de propagation de la rumeur, B , φ, μ, γ, c, d sont tous des constantes positive.
Il est important de preciser qu'au debut de la simulation tout les individus sont "S" sauf un seul qui est "I" car il doit commencer à propager la rumeur.



<a href="index.html"> Retour à la page principale </a>
