from graph import ALGraph, AMGraph, Vertex
from typing import Union

def color_graph(graph: Union[ALGraph, AMGraph], vertex: Vertex, method: str = 'dfs') -> tuple[str, str]:
    result = {}
    visited = set()
    container = []

    visited.add(vertex)
    container.append(vertex)

    while len(container) > 0:
        if method == 'dfs':
            v = container.pop()
        elif method == 'bfs':
            v = container.pop(0)

        colors = set()

        for i in [i[0] for i in graph.neighbours(v)]:
            try:
                colors.add(result[graph.get_vertex(i)])
            except KeyError:
                pass

        if len(colors) == 0:
            result[graph.get_vertex(v)] = 0
        else:
            color = 0
            while color in colors:
                color += 1
            result[graph.get_vertex(v)] = color

        for i in [i[0] for i in graph.neighbours(v)]:
            if i not in visited:
                visited.add(i)
                container.append(i)

    return [(str(i[0]), str(i[1])) for i in result.items()]