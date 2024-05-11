from __future__ import annotations
from typing import Union, ItemsView

class Vertex:
    def __init__(self, value: str) -> None:
        self.__value = value

    def __hash__(self) -> int:
        return hash(self.__value)
    
    def __eq__(self, other: Vertex) -> bool:
        return self.__value == other.__value
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __repr__(self) -> str:
        return str(self.__value)

class UnionFind:
    def __init__(self, vertices: list[Vertex]) -> None:
        self.__p = [i for i in range(len(vertices))]
        self.__size = [1 for i in range(len(vertices))]

    def find(self, v: int) -> int: 
        if self.__p[v] == v: 
            return v
        else:
            return self.find(self.__p[v])

    def union_sets(self, s1: int, s2: int) -> None:
        r1 = self.find(s1)
        r2 = self.find(s2)
        if not r1 == r2:
            if self.__size[r1] < self.__size[r2]:
                self.__p[r1] = r2
                self.__size[r2] += self.__size[r1]
            else:
                self.__p[r2] = r1
                self.__size[r1] += self.__size[r2]

    def same_components(self, s1: int, s2: int):
        return self.find(s1) == self.find(s2)
    
class Graph:
    def __init__(self) -> None:
        self.__list = {}

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        self.__list[vertex] = {}

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: float = None) -> None:
        try:
            self.__list[vertex1][vertex2] = edge
        except KeyError:
            self.__list[vertex1] = {}
            self.__list[vertex1][vertex2] = edge
        try:
            self.__list[vertex2][vertex1] = edge
        except KeyError:
            self.__list[vertex2] = {}
            self.__list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex: Vertex) -> None:
        try:
            self.__list.pop(vertex)
            for i in self.vertices():
                try:
                    self.__list[i].pop(vertex)
                except KeyError:
                    pass
        except KeyError:
           pass

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        try:
            self.__list[vertex1].pop(vertex2)
        except KeyError:
            pass
        try:
            self.__list[vertex2].pop(vertex1)
        except KeyError:
            pass

    def neighbours(self, vertex_id: Vertex) -> ItemsView[Vertex, float]:
        return self.__list[vertex_id].items()
    
    def vertices(self) -> ItemsView[Vertex]:
        return self.__list.keys()

    def get_vertex(self, vertex_id: Vertex) -> Vertex:
        return vertex_id
    
    def get_vertex_id(self, value: Vertex) -> Vertex:
        return value
    
    def printGraph(self) -> None:
        print("------GRAPH------")
        for v in self.vertices():
            print(v, end = " -> ")
            for (n, w) in self.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")

def Kruskal(graph: Graph) -> Graph:
    edges = []
    result = Graph()

    for i in graph.vertices():
        for j in graph.neighbours(i):
            edges.append((str(i), str(j[0]), j[1]))

    edges = sorted(edges, key=lambda a : a[2])
    vertices = list(graph.vertices())
    edgesASCII = [(ord(i[0]) - 65, ord(i[1]) - 65, i[2]) for i in edges]
    unionfind = UnionFind(vertices)

    for i in range(len(edges)):
        if not unionfind.same_components(edgesASCII[i][0], edgesASCII[i][1]):
            unionfind.union_sets(edgesASCII[i][0], edgesASCII[i][1])
            result.insert_edge(edges[i][0], edges[i][1], edges[i][2])

    return result

