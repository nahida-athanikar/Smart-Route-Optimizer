import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, shortest_path=None):
    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title("Smart Route Visualization")
    plt.show()