import math
 
 
class Graphe():
 
    def __init__(self, noeuds):
        self.matriceAdj = noeuds.copy()
 
    def Afficher(self, src, dist):
        print("les chemins les plus courts allant de ", src, " est : ")
        for noeud in range(len(self.matriceAdj)):
            print((noeud+1), "\t", dist[noeud])
 
    def minDistance(self, dist, S, T):
 
        # Initialiser la distance minimale pour le nœud
        min = math.inf
        min_index = -1
 
        for v in T:
            if dist[v-1] < min:
                min = dist[v-1]
                min_index = v-1
 
        # supprimer de T et ajouter dans S
        T.remove(min_index+1)
        S.append(min_index+1)
        return min_index
 
    def dijkstra(self, src):
 
        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src-1] = 0
        precedence[src-1] = src-1
        S = []
        T = [(i+1) for i in range(len(self.matriceAdj))]
 
        while len(S) < len(self.matriceAdj):
 
            # Choisir un sommet u qui n'est pas dans l'ensemble S et
            # qui a une valeur de distance minimale
            u = self.minDistance(dist, S, T)
 
            # relaxation des sommets
            for v in range(len(self.matriceAdj)):
                if (self.matriceAdj[u][v] > 0) and (dist[v] > (dist[u] + self.matriceAdj[u][v])):
                    dist[v] = dist[u] + self.matriceAdj[u][v]
                    precedence[v] = u
        self.Afficher(src, dist)
 
 
# Test
# les sommets sont numérotés à partir de 1
matriceAdj = [[0, 2, 4, 0, 0, 0],
              [0, 0, 1, 0, 7, 0],
              [0, 0, 0, 3, 0, 0],
              [0, 0, 0, 0, 2, 5],
              [0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0],
              ]
g = Graphe(matriceAdj)
g.dijkstra(1)