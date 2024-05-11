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
    
class Edge:
    def __init__(self, capacity: int, isResidual: bool) -> None:
        self._isResidual = isResidual
        if isResidual:
            self._flow = 0
            self._residual = 0
            self._capacity = 0
        else:
            self._flow = 0
            self._residual = capacity
            self._capacity = capacity

    def __repr__(self) -> str:
        return f'{self._capacity} {self._flow} {self._residual} {self._isResidual}'
    
class Graph:
    def __init__(self) -> None:
        self.__list = {}

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        self.__list[vertex] = {}

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge = None) -> None:
        try:
            self.__list[vertex1][vertex2] = edge
        except KeyError:
            self.__list[vertex1] = {}
            self.__list[vertex1][vertex2] = edge

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

    def neighbours(self, vertex_id: Vertex) -> ItemsView[Vertex, Edge]:
        return self.__list[vertex_id].items()
    
    def vertices(self) -> ItemsView[Vertex]:
        return self.__list.keys()

    def get_vertex(self, vertex_id: Vertex) -> Vertex:
        return vertex_id
    
    def get_vertex_id(self, value: Vertex) -> Vertex:
        return value
    
    def bfs(self) -> dict[Vertex, Vertex]:
        visited = [Vertex('s')]
        parent = {}
        queue = [Vertex('s')]
        while len(queue) != 0:
            current = queue.pop(0)
            for i in self.neighbours(current):
                if i[0] not in visited and i[1]._residual > 0:
                    visited.append(i[0])
                    parent[i[0]] = current
                    queue.append(i[0])
        return parent
    
    def minResidual(self, parent: dict[Vertex, Vertex]) -> int:
        current = Vertex('t')
        minResidual = float('inf')
        if current not in parent:
            return 0
        while current != Vertex('s'):
            if self.__list[parent[current]][current]._residual < minResidual:
                minResidual = self.__list[parent[current]][current]._residual
            current = parent[current]
        return minResidual
    
    def augumentation(self, parent: dict[Vertex, Vertex], minResidual: int) -> None:
        current = Vertex('t')
        while current != Vertex('s'):
            edge1 = self.__list[parent[current]][current]
            edge2 = self.__list[current][parent[current]]
            if not edge1._isResidual:
                edge1._flow += minResidual
                edge1._residual -= minResidual
                edge2._residual += minResidual
            else:
                edge1._residual -= minResidual
                edge2._flow -= minResidual
                edge2._residual += minResidual
            current = parent[current]

    def dsa(self) -> int:
        parent = self.bfs()
        minResidual = self.minResidual(parent)
        sum = 0
        while minResidual > 0:
            self.augumentation(parent, minResidual)
            parent = self.bfs()
            minResidual = self.minResidual(parent)
        for i in self.neighbours(Vertex('t')):
            sum += self.__list[i[0]][Vertex('t')]._flow
        return sum
    
    def printGraph(self):
        print("------GRAPH------")
        for v in self.vertices():
            print(v, end = " -> ")
            for (n, w) in self.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")