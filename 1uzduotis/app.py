import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import deque

def generate_random_graph(nodes, edges):
    """
    Sugeneruoja atsitiktini grafa su nurodytu mazgu ir jungciu skaiciumi.
    :param nodes: Mazgu (virsuniu) skaicius grafe.
    :param edges: Jungciu (briaunu) skaicius grafe.
    :return: Sugeneruotas grafas kaip NetworkX objektas.
    """
    graph = nx.Graph()  # Sukuriamas tuscias grafas
    graph.add_nodes_from(range(nodes))  # Pridedami mazgai su numeriu nuo 0 iki nodes-1

    # Atsitiktinių jungčių generavimas
    while graph.number_of_edges() < edges:
        u, v = random.sample(range(nodes), 2)  # Parenkamos dvi atsitiktines virsunes
        graph.add_edge(u, v, weight=random.randint(1, 10))  # Pridedama jungtis su atsitiktiniu svoriu

    return graph

def visualize_comparison(graph, bfs_path=None, dfs_path=None, title="Paieškos vizualizacija"):
    """
    Vizualizuoja pradinį grafą ir parodo BFS bei DFS kelius salia palyginimui.
    :param graph: Grafas, kuri reikia vizualizuoti.
    :param bfs_path: Kelias, rastas naudojant BFS.
    :param dfs_path: Kelias, rastas naudojant DFS.
    :param title: Grafko pavadinimas.
    """
    plt.figure(figsize=(18, 6))

    pos = nx.spring_layout(graph, seed=42)  #fiksuotas kad nebutu

    # 1. Pradinis grafas
    plt.subplot(1, 3, 1)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    plt.title("Pradinis grafas")

    # 2. BFS kelias
    plt.subplot(1, 3, 2)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    if bfs_path:
        bfs_edges = [(bfs_path[i], bfs_path[i+1]) for i in range(len(bfs_path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=bfs_edges, edge_color='green', width=3)
    plt.title("BFS Kelias")

    # 3. DFS kelias
    plt.subplot(1, 3, 3)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    if dfs_path:
        dfs_edges = [(dfs_path[i], dfs_path[i+1]) for i in range(len(dfs_path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=dfs_edges, edge_color='red', width=3)
    plt.title("DFS Kelias")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def bfs(graph, start, goal):
    """
    Plotis-pirmyn paieškos (BFS) algoritmo realizacija.
    :param graph: Grafas, kuriame vykdoma paieška.
    :param start: Pradinis mazgas.
    :param goal: Tikslinis mazgas.
    :return: Rastasis kelias ir aplankytu mazgų skaičius.
    """
    visited = set()
    queue = deque([(start, [start])])
    nodes_visited = 0

    while queue:
        current, path = queue.popleft()
        nodes_visited += 1

        if current == goal:
            return path, nodes_visited

        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_visited

def dfs(graph, start, goal):
    """
    Gylis-pirmyn paieškos (DFS) algoritmo realizacija.
    :param graph: Grafas, kuriame vykdoma paieška.
    :param start: Pradinis mazgas.
    :param goal: Tikslinis mazgas.
    :return: Rastasis kelias ir aplankytų mazgų skaičius.
    """
    visited = set()
    stack = [(start, [start])]
    nodes_visited = 0

    while stack:
        current, path = stack.pop()
        nodes_visited += 1

        if current == goal:
            return path, nodes_visited

        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_visited

def evaluate_algorithms(graph, start, goal):
    """
    Atlieka BFS ir DFS algoritmų įvertinimą su pateiktu grafu.
    :param graph: Grafas, kuriame vykdoma paieška.
    :param start: Pradinis mazgas.
    :param goal: Tikslinis mazgas.
    """
    print(f"Paieškos nuo {start} iki {goal} rezultatai:\n")

    # BFS algoritmo vykdymas
    bfs_path, bfs_nodes = bfs(graph, start, goal)
    print(f"BFS kelias: {bfs_path}")
    print(f"BFS aplankyti mazgai: {bfs_nodes}\n")

    # DFS algoritmo vykdymas
    dfs_path, dfs_nodes = dfs(graph, start, goal)
    print(f"DFS kelias: {dfs_path}")
    print(f"DFS aplankyti mazgai: {dfs_nodes}\n")

    # Vizualizacija šalia palyginimui
    visualize_comparison(graph, bfs_path, dfs_path, title=f"BFS ir DFS palyginimas ({start} → {goal})")

def main():
    """
    Pagrindine funkcija, vykdanti paieškos algoritmus su trimis skirtingais duomenų rinkiniais.
    """
    for i in range(3):
        print(f"========== Grafas {i + 1} ==========")
        graph = generate_random_graph(20, 40)
        start, goal = random.sample(range(20), 2)
        evaluate_algorithms(graph, start, goal)
        print("====================================\n")

if __name__ == "__main__":
    main()
