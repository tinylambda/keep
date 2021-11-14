import logging
import sys
import networkx as nx

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    G = nx.Graph()
    logging.info('add one node at a time: %s', G)
    G.add_node(1)

    logging.info('add nodes from any iterable container: %s', G)
    G.add_nodes_from([2, 3])

    logging.info('add nodes along with node attributes: %s', G)
    G.add_nodes_from([
        (4, {'color': 'red'}),
        (5, {'color': 'green'}),
    ])

    logging.info('nodes from one graph can be incorporated into another: %s', G)
    H = nx.path_graph(10)
    G.add_nodes_from(H)

    logging.info('add one edge at a time: %s', G)
    G.add_edge(1, 2)

    logging.info('unpack edge tuple: %s', G)
    e = (2, 3)
    G.add_edge(*e)

    logging.info('add a list of edges: %s', G)
    G.add_edges_from([(1, 2), (1, 3)])

    logging.info('final" %s', G)
