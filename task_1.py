from enum import StrEnum
import networkx as nx
import matplotlib.pyplot as plt


class City(StrEnum):
    Kyiv = "Kyiv"
    Kharkiv = "Kharkiv"
    Dnipro = "Dnipro"
    Odesa = "Odesa"
    Uman = "Uman"
    Lviv = "Lviv"
    IvanoFrankivsk = "Ivano-Frankivsk"

CITIES = {
    City.Kyiv: [0, 0],
    City.Kharkiv: [1, 0],
    City.Dnipro: [2, -1],
    City.Uman: [0, -1],
    City.Odesa: [0, -2],
    City.Lviv: [-1, 0],
    City.IvanoFrankivsk: [-2, -1],
}

DISTANCES = {
    (City.Kyiv, City.Kharkiv): 489,
    (City.Kyiv, City.Dnipro): 501,
    (City.Kyiv, City.Uman): 231,
    (City.Kyiv, City.Lviv): 547,
    (City.Kyiv, City.IvanoFrankivsk): 611,
    (City.Uman, City.Dnipro): 417,
    (City.Uman, City.Odesa): 272,
    (City.Uman, City.Lviv): 530,
    (City.Uman, City.IvanoFrankivsk): 532,
    (City.Kharkiv, City.Dnipro): 221,
    (City.Dnipro, City.Odesa): 453,
    (City.Lviv, City.IvanoFrankivsk): 135,
}

def draw_graph(g: nx.DiGraph):
    pos = CITIES
    weights = nx.get_edge_attributes(g, 'weight')
    nx.draw(g, pos, node_size=5000, node_color="lightblue", alpha=0.7)
    nx.draw_networkx_labels(g, pos, font_size=8)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, font_size=8)
    plt.show()

def print_centrality(label: str, properties: dict[City, float]):
    print(label)
    list = sorted([(value, city) for city, value in properties.items()], reverse=True)
    for value, city in list:
        print(f"{city}: {value:.3f}")

def print_properties(g: nx.DiGraph):
    print(f"Number of nodes: {g.number_of_nodes()}")
    print(f"Number of edges: {g.number_of_edges()}")
    print_centrality("\nDegreee centrality:", nx.degree_centrality(g))
    print_centrality("\nCloseness centrality:", nx.closeness_centrality(g))
    print_centrality("\nBetweenness centrality:", nx.betweenness_centrality(g))

def build_city_graph():
    g = nx.DiGraph()
    g.add_nodes_from(CITIES.keys())
    for (city1, city2), distance in DISTANCES.items():
        g.add_edge(city1, city2, weight=distance)
        g.add_edge(city2, city1, weight=distance)
    return g

def main():
    plt.figure(figsize=(13, 8))
    g = build_city_graph()
    print_properties(g)
    draw_graph(g)


if __name__ == "__main__":
    main()
