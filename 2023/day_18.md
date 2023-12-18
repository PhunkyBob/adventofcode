# --- Day 18: Lavaduct Lagoon ---

## Partie 1

## Chargement des données

- Pour chaque coordonées / longueur, je rajoute dans un `set` toutes les cases de la tranchée.

### Calcul de la surface

- Je prends la surface complète que j'étends de 1 de tous les côtés.
- En partant du point le plus en haut à gauche, j'ajoute les cases des 4 directions dans une `queue`. Pour chaque case, si elle ne fait pas partie de la tranchée, je continue. 
- Une fois que je connais le nombre de case en dehors, je soustrais au nombre de cases de la zone. 

Ca aurait été bien plus efficace d'utiliser la même méthode que la Partie 2, mais comme c'est déjà très rapide...

## Partie 2

Il n'est plus possibles de charger les données comme pour la Partie 1 et encore moins de calculer la surface. 

## Chargement des données

- Je stocke dans un `set` la liste de tous les points de la forme géométrique. 

## Calcul de la surface

La [Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula) est un algorithme mathématique pour déterminer l'aire d'un polygone simple dont les sommets sont décrits par leurs coordonnées cartésiennes dans le plan. 

```
def shoelace(points: List[Coord]) -> int:
    n = len(points)
    return (
        abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n))) // 2
    )
```

Le [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) fournit une formule pour l'aire d'un polygone simple avec des coordonnées de sommet entières , en termes de nombre de points entiers à l'intérieur et sur sa frontière.

```
def picks_theorem(points: List[Coord]) -> int:
    return (
        sum(
            abs(points[i][0] - points[(i + 1) % len(points)][0]) + abs(points[i][1] - points[(i + 1) % len(points)][1])
            for i in range(len(points))
        ) // 2  + 1
    )
```
