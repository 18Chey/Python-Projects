class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value: int):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, node1: int, node2: int, weight: int, directed: bool):
        self.add_node(node1)
        self.add_node(node2)

        self.nodes[node1].append((node2, weight))
        if not directed:
            self.nodes[node2].append((node1, weight))

    def __repr__(self):
        return "\n".join(f"{node}: {edges}" for node, edges in self.nodes.items())


def depth_first_traversal(graph: Graph, start: int) -> list[int]:
    to_visit = []
    visited = set()
    result = []

    to_visit.append(start)

    while to_visit:
        current = to_visit.pop(0)
        visited.add(current)
        result.append(current)

        to_visit = [
            neighbour
            for neighbour, weight in graph.nodes[current]
            if neighbour not in to_visit and neighbour not in visited
        ] + to_visit

    return result


def depth_first_search(graph: Graph, start: int, target: int) -> bool:
    to_visit = []
    visited = set()

    to_visit.append(start)

    while to_visit:
        current = to_visit.pop(0)
        visited.add(current)
        if current == target:
            return True

        to_visit = [
            neighbour
            for neighbour, weight in graph.nodes[current]
            if neighbour not in to_visit and neighbour not in visited
        ] + to_visit

    return False


def breadth_first_traversal(graph: Graph, start: int) -> list[int]:
    to_visit = []
    visited = set()
    result = []

    to_visit.append(start)

    while to_visit:
        current = to_visit.pop(0)
        visited.add(current)
        result.append(current)

        to_visit = to_visit + [
            neighbour
            for neighbour, weight in graph.nodes[current]
            if neighbour not in to_visit and neighbour not in visited
        ]

    return result


def breadth_first_search(graph: Graph, start: int, target: int) -> list[int]:
    to_visit = []
    visited = set()

    to_visit.append(start)

    while to_visit:
        current = to_visit.pop(0)
        visited.add(current)
        if current == target:
            return True

        to_visit = to_visit + [
            neighbour
            for neighbour, weight in graph.nodes[current]
            if neighbour not in to_visit and neighbour not in visited
        ]

    return False


def djikstras(graph: Graph, start: int, target: int):
    unvisited = {node: [float("inf"), None] for node in graph.nodes}
    visited = {}

    unvisited[start][0] = 0

    while unvisited:
        current = min(unvisited, key=lambda node: unvisited[node][0])
        visited[current] = unvisited[current]
        del unvisited[current]

        for neighbour, weight in graph.nodes[current]:
            if neighbour in unvisited:
                if unvisited[neighbour][0] > visited[current][0] + weight:
                    unvisited[neighbour][0] = visited[current][0] + weight
                    unvisited[neighbour][1] = current

    path = []
    previous = target
    while previous is not None:
        path.insert(0, previous)
        previous = visited[previous][1]

    return path


def main():
    graph = Graph()
    for i in range(1, 6):
        graph.add_node(i)
    graph.add_edge(1, 2, 7, False)
    graph.add_edge(1, 5, 1, False)
    graph.add_edge(2, 5, 8, False)
    graph.add_edge(2, 3, 3, False)
    graph.add_edge(3, 5, 2, False)
    graph.add_edge(3, 4, 6, False)
    graph.add_edge(4, 5, 7, False)

    print(djikstras(graph, 1, 4))


if __name__ == "__main__":
    main()
