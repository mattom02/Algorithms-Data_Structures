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
    
class ALGraph:
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

    def neighbours(self, vertex_id: Vertex) -> ItemsView[Vertex, Union[float, None]]:
        return self.__list[vertex_id].items()
    
    def vertices(self) -> ItemsView[Vertex]:
        return self.__list.keys()

    def get_vertex(self, vertex_id: Vertex) -> Vertex:
        return vertex_id
    
    def get_vertex_id(self, value: Vertex) -> Vertex:
        return value

class AMGraph:
    def __init__(self, default: int = 0) -> None:
        self.__list = []
        self.__values = []
        self.__default = default

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def insert_vertex(self, vertex: Vertex) -> None:
        for i in self.__list:
            i.append(self.__default)
        self.__list.append([self.__default for i in range(len(self.__list) + 1)])
        self.__values.append(vertex)

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge: float = 1) -> None:
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        if id1 is None:
            self.insert_vertex(vertex1)
            id1 = len(self.__values) - 1
        if id2 is None:
            self.insert_vertex(vertex2)
            id2 = len(self.__values) - 1
        self.__list[id1][id2] = edge
        self.__list[id2][id1] = edge

    def delete_vertex(self, vertex: Vertex) -> None:
        id = self.get_vertex_id(vertex)
        if id is not None:
            self.__list.pop(id)
            for i in self.vertices():
                self.__list[i].pop(id)
            self.__values.pop(id)

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        if id1 is not None and id2 is not None:
            self.__list[id1][id2] = self.__default
            self.__list[id2][id1] = self.__default

    def neighbours(self, vertex_id: int) -> list[tuple[int, int]]:
        return [(i, self.__list[vertex_id][i]) for i in range(len(self.__values)) if self.__list[vertex_id][i] != self.__default]
    
    def vertices(self) -> list[int]:
        return [i for i in range(len(self.__values) - 1)]

    def get_vertex(self, vertex_id: int) -> Vertex:
        return self.__values[vertex_id]
    
    def get_vertex_id(self, value: Vertex) -> Union[None, int]:
        id = 0
        for i in self.__values:
            if i == value:
                return id
            id += 1
        return None
