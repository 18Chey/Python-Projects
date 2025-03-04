class Graph:
    def __init__(self) -> None:
        self.nodes: dict[int : list[int]] = {1: [2], 2: [1]}

    def add_node(self, value: int, connections: list[int]) -> None:
        self.nodes[value] = connections
        for node in connections:
            self.nodes[node].append(value)

    def breadth_first(self, start):
        to_visit = []
        visited = set()
        traversal = []

        to_visit.append(start)
        while to_visit:
            current = to_visit.pop(0)
            visited.add(current)
            traversal.append(current)
            for node in self.nodes[current]:
                if node not in visited and node not in to_visit:
                    to_visit.append(node)

        print(traversal)


mygraph = Graph()
mygraph.add_node(1, [])
mygraph.add_node(2, [1])
mygraph.add_node(3, [2])
mygraph.add_node(4, [3])
mygraph.add_node(5, [1, 2, 3, 4])
print(mygraph.nodes)
mygraph.breadth_first(1)
