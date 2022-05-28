import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from utils import decorate, savefig

np.random.seed(87)
colors = sns.color_palette('pastel', 5)
sns.set_palette(colors)


if __name__ == '__main__':
    G = nx.DiGraph()

    G.add_node('Alice')
    G.add_node('Bob')
    G.add_node('Chuck')

    print(G.nodes())

    G.add_edge('Alice', 'Bob')
    G.add_edge('Alice', 'Chuck')
    G.add_edge('Bob', 'Alice')
    G.add_edge('Bob', 'Chuck')

    print(list(G.edges()))

    nx.draw_circular(G, node_color='C0', node_size=2000, with_labels=True)
    plt.axis('equal')
    savefig('figs/chap02-1')

    # start a new graph
    plt.clf()

    positions = dict(
        Albany=(-74, 43),
        Boston=(-71, 42),
        NYC=(-74, 41),
        Philly=(-75, 40),
    )
    # Undirected Graph
    G = nx.Graph()
    G.add_nodes_from(positions)
    print(G.nodes)

    drive_times = {
        ('Albany', 'Boston'): 3,
        ('Albany', 'NYC'): 4,
        ('Boston', 'NYC'): 4,
        ('NYC', 'Philly'): 2,
    }
    G.add_edges_from(drive_times)
    print(G.edges)
    nx.draw(
        G,
        positions,
        node_color='C1',
        node_shape='s',
        node_size=2500,
        with_labels=True,
    )
    nx.draw_networkx_edge_labels(
        G,
        positions,
        edge_labels=drive_times,
    )
    plt.axis('equal')
    savefig('figs/chap02-2')

    plt.clf()

    def all_pairs(nodes):
        for i, u in enumerate(nodes):
            for j, v in enumerate(nodes):
                if i > j:
                    yield u, v

    def make_complete_graph(n):
        G = nx.Graph()
        nodes = range(n)
        G.add_nodes_from(nodes)
        G.add_edges_from(all_pairs(nodes))
        return G

    complete = make_complete_graph(10)
    print(complete.number_of_nodes())
    nx.draw_circular(
        complete,
        node_color='C2',
        node_size=1000,
        with_labels=True,
    )
    savefig('figs/chap02-3')
    plt.clf()

    print(list(complete.neighbors(0)))

    def reachable_nodes(G, start):
        seen = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in seen:
                seen.add(node)
                stack.extend(G.neighbors(node))
        return seen

    print(reachable_nodes(complete, 0))

    def flip(p):
        return np.random.random() < p

    def random_pairs(nodes, p):
        for edge in all_pairs(nodes):
            if flip(p):
                yield edge

    def make_random_graph(n, p):
        G = nx.Graph()
        nodes = range(n)
        G.add_nodes_from(nodes)
        G.add_edges_from(random_pairs(nodes, p))
        return G

    np.random.seed(10)
    random_graph = make_random_graph(10, 0.3)
    print(len(random_graph.edges))
    print(random_graph.number_of_edges())

    nx.draw_circular(
        random_graph,
        node_color='C3',
        node_size=1000,
        with_labels=True,
    )
    savefig('figs/chap02-4')
    plt.clf()

    print(reachable_nodes(random_graph, 0))

    def is_connected(G):
        start = next(iter(G))
        reachable = reachable_nodes(G, start)
        return len(reachable) == G.number_of_nodes()

    print(is_connected(complete))
    random_graph = make_random_graph(10, 0.1)
    print(is_connected(random_graph))

    def prob_connected(n, p, iters=100):
        tf = [is_connected(make_random_graph(n, p)) for i in range(iters)]
        return np.mean(tf)

    print(prob_connected(10, 0.23, iters=10000))

    n = 10
    pstar = np.log(n) / n
    ps = np.logspace(-2.5, 0, 11)
    ys = [prob_connected(n, p, 1000) for p in ps]
    for p, y in zip(ps, ys):
        print(p, y)

    plt.axvline(pstar, color='gray')
    plt.plot(ps, ys, color='green')
    decorate(xlabel='Prob of edge (p)', ylabel='Prob connected', xscale='log')
    savefig('figs/chap02-5')
    plt.clf()

    ns = [300, 100, 30]
    ps = np.logspace(-2.5, 0, 11)
    sns.set_palette('Blues_r', 4)
    for n in ns:
        print(n)
        pstar = np.log(n) / n
        plt.axvline(pstar, color='gray', alpha=0.3)
        ys = [prob_connected(n, p) for p in ps]
        plt.plot(ps, ys, label='n=%d' % n)

    decorate(
        xlabel='Prob of edge (p)',
        ylabel='Prob connected',
        xscale='log',
        xlim=[ps[0], ps[-1]],
        loc='upper left',
    )
    savefig('figs/chap02-6')
    plt.clf()
