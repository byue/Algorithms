import matplotlib.pyplot as plt
import networkx as nx

def draw_mst(graph, mst):
    pos = nx.spring_layout(graph, k=2, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=12)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(mst, pos, node_color='lightblue', edge_color='red', node_size=500, font_size=12)
    edge_labels_mst = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels_mst)
    plt.show()