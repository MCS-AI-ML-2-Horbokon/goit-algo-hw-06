from task_1 import City, build_city_graph
from collections import deque
import networkx as nx


def edge_distance(g: nx.DiGraph, start: City, end: City) -> float:
    infinity = float("inf")
    if end not in g[start]:
        return infinity

    return g[start][end].get("weight", infinity)

def bfs(g: nx.DiGraph, start: City) -> list[City]:
    queue = deque([start])
    visited: set[City] = set()
    visited_in_order: list[City] = list()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue

        visited.add(current)
        visited_in_order.append(current)
        neighbors = nx.neighbors(g, current)
        neighbors_by_distance = sorted(neighbors, key=lambda city: edge_distance(g, current, city))
        for city in neighbors_by_distance: # Append in order
            if city not in visited:
                queue.append(city)

    return visited_in_order

def dfs(g: nx.DiGraph, start: City) -> list[City]:
    stack = deque([start])
    visited: set[City] = set()
    visited_in_order: list[City] = list()
    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        visited_in_order.append(current)
        neighbors = nx.neighbors(g, current)
        neighbors_by_distance = sorted(neighbors, key=lambda city: edge_distance(g, current, city), reverse=True)
        for city in neighbors_by_distance: # Append in reversed order
            if city not in visited:
                stack.append(city)

    return visited_in_order

def main():
    g = build_city_graph()
    bfs_visited = bfs(g, City.Kharkiv)
    dfs_visited = dfs(g, City.Kharkiv)
    print([city.value for city in bfs_visited]) # In order of appearance
    print([city.value for city in dfs_visited])


if __name__ == "__main__":
    main()
