# Advent of Code 2023

## Day 25

### Problème

Graph non orienté, il faut trouver les 3 liens à couper pour faire 2 graphs distincts.

### Solution

Utiliser l'algorithme de [Stoer Wagner](https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm).
Pour éviter de réimplémenter l'algo, on peut utiliser la fonction `stoer_wagner` de la librairie [NetworkX](https://pypi.org/project/networkx/).
