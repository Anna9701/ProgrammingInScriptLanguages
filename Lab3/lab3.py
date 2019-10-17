import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

def show_graph(graph, colors_map = None):
    if colors_map is None:
        colors_map = {}
    values = [colors_map.get(node, 0.25) for node in graph.nodes()]
    nx.draw(graph, cmap=plt.get_cmap('magma'), node_color=values, with_labels=True, font_color='white')
    plt.draw()
    plt.show()

def exercise1():
    graph = nx.Graph()
    graph.add_edges_from(
        [(1, 2), (1, 5), (2, 1), (2, 5), (2, 3),
         (2, 4), (3, 2), (3, 4), (4, 2), (4, 5), (4, 3), (5, 4), (5, 1), (5, 2)])
    show_graph(graph)

def exercise2():
    node_1 = Node(1)
    node_2 = Node(2, node_1)
    node_3 = Node(3, node_2)
    node_4 = Node(4, node_2, node_3)
    node_5 = Node(5, node_1, node_2, node_4)

    node_1.add__neighbours(node_2, node_5)
    node_2.add__neighbours(node_5, node_4, node_3)
    node_3.add__neighbours(node_4)
    node_4.add__neighbours(node_5)

    my_graph = Graph(node_1, node_2, node_3, node_4, node_5)
    my_graph.Bfs(node_1)
    input("Press Enter to continue...")

WHITE = "White"
GRAY = "Gray"
BLACK = "Black"

class Graph:
    def __init__(self, *elements):
        self.nodes = list(elements)

    def add(self, node):
        self.nodes += [node]

    def __str__(self):
        for node in self.nodes:
            print(node)

    def draw_graph(self):
        graph = nx.Graph()
        colors_val_map = { }
        for node in self.nodes:
            for neighbour in node.adj:
                graph.add_edge(node.label, neighbour.label)
            if node.color == WHITE:
                colors_val_map[node.label] = 0.9
            elif node.color == GRAY:
                colors_val_map[node.label] = 0.5
            else:
                colors_val_map[node.label] = 0.33
        show_graph(graph, colors_val_map)

    def Bfs(self, start):
        self.draw_graph()
        start.color = GRAY
        self.draw_graph()
        start.d = 0
        queue = [start]
        while len(queue) > 0:
            u = queue.pop(0)
            for neighbour in u.adj:
                if neighbour.color == WHITE:
                    self.draw_graph()
                    neighbour.color = GRAY
                    self.draw_graph()
                    neighbour.d = u.d + 1
                    neighbour.pi = [u]
                    queue.append(neighbour)
            u.color = BLACK
            self.draw_graph()

class Node:
    def __init__(self, label, *neighbours):
        self.d = sys.maxsize
        self.color = WHITE
        self.pi = []
        self.adj = list(neighbours)
        self.label = str(label)

    def add__neighbours(self, *neighbours):
        self.adj += neighbours

    def __str__(self):
        return "Node: " + self.label + " " + self.color + " neighbours: " + str(len(self.adj))



#exercise1()
#input("Press Enter to continue...")
exercise2()