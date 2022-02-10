# TP 3
## Le problème du voyageur de commerce
### Package Python nécessaires
- tqdm
- matplotlib
- numpy
- pandas
### Détails du projet
Le problème du voyageur de commerce est un problème d'optimisation qui consiste à déterminer, étant donné une liste de villes et les distances entre toutes les paires de villes, le plus court chemin qui passe par chaque ville et une seule fois.
Afin de résoudre ce problème, j'ai décidé ici d'utiliser un algorithme génétique. L'approche de ce problème avec un algorithme génétique peut être décrit de la façon suivante:
- **Gène**: une ville (représenté comme des coordonnées (x,y))
- **Individu**: un itinéraire qui satisfait les conditions plus haut
- **Population**: collection d'individus
- **Parent**: Deux itinéraires qui sont combinés afin de créer un nouvel itinéraire
- **Génération**: une collection de parents qui sont utilisés pour créer notre prochaine population (et donc crée notre prochaine génération d'itinéraires)
- **Fitness**: une fonction qui nous permet de dire à quel point notre itinéraire est bon et donc dans notre cas à quel point il est court
- **Mutation**: pour introduire de la variation dans notre population en échangeant deux villes dans notre itinéraire de façon aléatoire
- **Élitisme**: une manière de prendre nos meilleurs individus dans la prochaine génération.


L'algorithme génétique va suivre les étapes suivantes:
1. Création de la population 
2. Déterminer la fonction fitness
3. Sélectionner la génération
4. Reproduction
5. Mutation
6. Répéter

### Lancement du projet
Lancer le script tsp.py et se laisser guider.
Sinon essayer un nombre de villes à 25, taille de la population à 100, taille de l'élite à 20, taux de mutation à 0.01 et nombre de générations à 500.
