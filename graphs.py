class Graph:
    def __init__(self) -> None:
        self.nodes: dict[int : list[int]] = {}

    def add_node(self, value: int, connections: list[int]) -> None:
        self.nodes[value] = connections
        for node in connections:
            self.nodes[node].append(value)

    def depth_first(self, start):
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
                    to_visit.insert(0, node)

        print(traversal)

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
mygraph.add_node(5, [3])
mygraph.add_node(6, [2])
mygraph.add_node(7, [1])
mygraph.add_node(8, [7])
mygraph.add_node(9, [8])
mygraph.add_node(10, [7])


mygraph.breadth_first(1)
mygraph.depth_first(1)
