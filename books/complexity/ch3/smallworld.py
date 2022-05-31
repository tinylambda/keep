import networkx as nx
import numpy as np
from books.complexity.ch2.graph_new import flip


def adjacent_edges(nodes, halfk):
    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i + 1, i + halfk + 1):
            v = nodes[j % n]
            yield u, v


if __name__ == "__main__":
    nodes = range(3)
    for edge in adjacent_edges(nodes, 1):
        print(edge)

    def make_ring_lattice(n, k):
        G = nx.Graph()
        nodes = range(n)
        G.add_nodes_from(nodes)
        G.add_edges_from(adjacent_edges(nodes, k // 2))
        return G

    lattice = make_ring_lattice(10, 4)
    print(lattice)

    def rewire(G, p):
        nodes = set(G)
        for u, v in G.edges():
            if flip(p):
                choices = nodes - {u} - set(G[u])
                new_v = np.random.choice(list(choices))
                G.remove_edge(u, v)
                G.add_edge(u, new_v)
