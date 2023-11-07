
# class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # a function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
