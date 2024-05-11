from __future__ import annotations
from typing import Union, ItemsView

class Vertex:
    def __init__(self, value: Union[str, int]) -> None:
        self.__value = value

    def __hash__(self) -> int:
        return hash(self.__value)
    
    def __eq__(self, other: Vertex) -> bool:
        return self.__value == other.__value
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __repr__(self) -> str:
        return str(self.__value)
    
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

def prim(graph: Graph) -> tuple[Graph, float]:
    mst = Graph()

    intree = {}
    distance = {}
    parent = {}

    for i in graph.vertices():
        intree[i] = 0
        distance[i] = float('inf')
        parent[i] = None
        mst.insert_vertex(i)

    v = list(graph.vertices())[0]
    sum = 0
    while intree[v] == 0:
        intree[v] = 1
        
        for i in graph.neighbours(v):
            if i[1] < distance[i[0]] and intree[i[0]] == 0:
                distance[i[0]] = i[1]
                parent[i[0]] = v
        
        min_distance = float('inf')

        for i in graph.vertices():
            if distance[i] < min_distance and intree[i] == 0:
                min_distance = distance[i]
                v = i

        mst.insert_edge(v, parent[v], distance[v])
        sum += distance[v]
    sum -= distance[v]
    return mst, sum