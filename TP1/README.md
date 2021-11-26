# TP 1
## Game of life
Le premier game of life est un game of life classique. 

## Game Of Life Prey / Predator ecosystem
Le deuxième est un game of life avec un écosystème proie / prédateur. 
L'herbe est de couleur verte, les moutons de couleur bleu et les loups de couleur rouge.
Les règles sont les suivantes:
- Les loups:
    - Lorsque deux loups sont côte à côte, il y a reproduction
    - Lorsqu'il y a un mouton à côté, le loup le mange
    - Lorsque les deux conditions précédentes sont respectées, le loup choisi de manger
- Les moutons:
    - Lorsque deux moutons sont côte à côte, il y a reproduction
    - Lorsqu'il y a de l'herbe à côté, le mouton en mange
    - Lorsque les deux conditions précédentes sont respectées, le mouton choisi la reproduction

Dans la définition de la fonction on peut choisir la durée de vie des moutons et des loups. S'ils dépassent une de ses durées, ils meurent immédiatement.
Même si un mouton mange de l'herbe, cette dernière ne disparaît pas.      
