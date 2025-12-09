from task_1 import City, build_city_graph
from task_2 import edge_distance
import networkx as nx


def dijkstra(g: nx.DiGraph, start: City):
    cities: list[City] = nx.nodes(g)
    unvisited = set(cities)
    distances = {city: float("inf") for city in cities}
    distances[start] = 0
    while unvisited:
        current = min(unvisited, key=lambda city: distances[city])
        neighbors = nx.neighbors(g, current)
        for city in neighbors:
            distance = edge_distance(g, current, city) + distances[current]
            if distances[city] > distance:
                distances[city] = distance

        unvisited.remove(current)

    return distances

def print_distances(distances: dict[City, float]):
    cities_by_distance = sorted((distance, city) for city, distance in distances.items())
    _, start = cities_by_distance[0]
    print(f"\nDistances from {start.value}:")
    for distance, city in cities_by_distance:
        print(f"    to {city}: {distance} km")

def main():
    g = build_city_graph()
    print_distances(dijkstra(g, City.Kharkiv))
    print_distances(dijkstra(g, City.Lviv))
    print_distances(dijkstra(g, City.Odesa))


if __name__ == "__main__":
    main()
