# Advent of Code 2023


## Day 24 - Part A

### Problème

Trouver l'intersection de 2 droites dans un plan 2D.

## Solution 

Transformer en équation paramétrique de droite.

## Day 24 - Part B

### Problème

Trouver la droite qui est l'intersection de plusieurs droites dans un espace en 3D.

### Solution

Résoudre l'ensemble des équations.
On peut utiliser la librairie [Z3](https://github.com/Z3Prover/z3) qui prend en entrée une liste d'équations et qui donne en résultat les valeurs possibles.

## Day 25

### Problème

Graph non orienté, il faut trouver les 3 liens à couper pour faire 2 graphs distincts.

### Solution

Utiliser l'algorithme de [Stoer Wagner](https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm).
Pour éviter de réimplémenter l'algo, on peut utiliser la fonction `stoer_wagner` de la librairie [NetworkX](https://pypi.org/project/networkx/).
