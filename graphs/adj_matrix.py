from typing import Optional

# Adjacency matrix implementation in Python


class Graph:
    def __init__(self, num_vertex: int):
        self.adj_matrix = [[-1] * num_vertex for _ in range(num_vertex)]
        self.num_vertex = num_vertex
        self.vertices = {}
        self.vertices_list = [0] * num_vertex

    def set_vertex(self, vertex: int, id):
        if 0 <= vertex <= self.num_vertex:
            self.vertices[id] = vertex
            self.vertices_list[vertex] = id

    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adj_matrix[frm][to] = cost
        self.adj_matrix[to][frm] = cost

    def get_edges(self):
        edges = []
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                if self.adj_matrix[i][j] != -1:
                    edges.append(
                        (self.vertices_list[i], self.vertices_list[j], self.adj_matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adj_matrix


G = Graph(6)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')
G.set_vertex(5, 'f')

print(G.vertices)  # {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
print(G.vertices_list)  # ['a', 'b', 'c', 'd', 'e', 'f']

G.set_edge('a', 'e', 10)
G.set_edge('a', 'c', 20)
G.set_edge('c', 'b', 30)
G.set_edge('b', 'e', 40)
G.set_edge('e', 'd', 50)
G.set_edge('f', 'e', 60)

print(G.get_edges())

print(G.get_matrix())
